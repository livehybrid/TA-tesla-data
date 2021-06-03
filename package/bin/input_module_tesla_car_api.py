# encoding = utf-8

import ta_tesla_data_declare


import os
import sys
import time
import datetime
import json
import splunklib.client as client
from teslapy import Tesla as teslapy
from teslapy import BASE_URL, CLIENT_ID, SSO_BASE_URL, SSO_CLIENT_ID
from hashlib import md5
from requests.exceptions import *


class spltes(teslapy):
    def __init__(self, *args, **kwargs):
        self.helper = kwargs.get('helper')
        del(kwargs['helper'])
        super(spltes, self).__init__(*args, **kwargs)

    def get_encoded_checkpoint_path(self, username):
        # encode the username
        name = ""
        for i in range(len(username)):
            if username[i].isalnum():
                name += username[i]
            else:
                name += "_"

        # MD5 the URL
        m = md5()
        m.update(username.encode('utf-8'))
        name += "_" + m.hexdigest()

        return os.path.join(self.helper.context_meta["checkpoint_dir"], name)

    @property
    def checkpoint_file(self):
        return self.get_encoded_checkpoint_path(self.email)

    def _token_updater(self):
        """ Overwrides the default teslapy token persistency """

        chk_file = self.checkpoint_file

        # Open checkpoint
        try:
            with open(chk_file) as infile:
                cache = json.load(infile)
        except (IOError, ValueError):
            cache = {}
        # Write token to cache file
        if self.authorized:
            cache[self.email] = {'url': self.sso_base, 'sso': self.sso_token,
                                 SSO_CLIENT_ID: self.token}
            try:
                with open(chk_file, 'w') as outfile:
                    json.dump(cache, outfile)
            except IOError as e:
                self.helper.log_error('Cache not updated - {}'.format(e))
            else:
                self.helper.log_debug('Updated cache')
        # Read token from cache
        elif self.email in cache:
            self.sso_base = cache[self.email].get('url', SSO_BASE_URL)
            self.sso_token = cache[self.email].get('sso', {})
            self.token = cache[self.email].get(SSO_CLIENT_ID, {})
            if not self.token:
                return
            self.expires_at = (self.token['created_at']
                               + self.token['expires_in'])
            self.authorized = True
            # Log the token validity
            if 0 < self.expires_at < time.time():
                self.helper.log_debug('Cached JWT bearer expired')
            else:
                self.helper.log_debug("Cached JWT bearer, expires at {}".format(time.ctime(self.expires_at)))


def validate_input(helper, definition):
    data_collector = definition.parameters.get('data_collector', None)
    vehicle_id = definition.parameters.get('vehicle_id', None)
    if (data_collector!="vehicle_list" and vehicle_id==""):
        helper.log_error("You must enter a vehicle ID for this data collector")
        print("You must enter a vehicle ID for this data collector")

def get_api_endpoint(name):
    api_endpoints = {
            "vehicle_data" : "/api/1/vehicles/{id}/vehicle_data",
            "vehicle_list" : "/api/1/vehicles",
            "supercharger" : "/api/1/vehicles/{id}/nearby_charging_sites",
            "auth"         : "/oauth/token"
        }
    return "https://owner-api.teslamotors.com" + api_endpoints.get(name)

def do_login(helper):
    helper.log_warning("SSL verify is {}".format(helper.get_global_setting("verify_ssl")))
    with spltes(
        helper.get_arg('tesla_email'),
        helper.get_arg('tesla_password'),
        #proxy="https://192.168.0.190:9999",
        helper=helper,
        verify = False if helper.get_global_setting("verify_ssl") == "0" else True
    ) as tesla:
        tesla.fetch_token()
        helper.log_warning("Found token={}".format(tesla.token))
        return tesla.token['access_token']


# def do_login(helper):
#     token_realm = helper.get_input_type()
#     tesla_username = helper.get_arg('tesla_email')
#
#     splunkService = client.connect(token=helper.context_meta['session_key'])
#     storage_passwords = splunkService.storage_passwords
#     returned_credential = [k for k in storage_passwords if k.content.get('realm')==token_realm and k.content.get('username')==tesla_username]
#
#     token = get_api_session(helper=helper)
#     return token

def collect_events(helper, ew):

    global_verify_ssl = False if helper.get_global_setting("verify_ssl") == "0" else True
    global_retries = 3

    loglevel = helper.get_log_level()

    tesla_username = helper.get_arg('tesla_email')
    tesla_password = helper.get_arg('tesla_password')
    data_collector = helper.get_arg('data_collector')
    vehicle_id = helper.get_arg('vehicle_id')

    if (data_collector!="vehicle_list" and vehicle_id==""):
        helper.log_error("You must enter a vehicle ID for this data collector")
        exit(1)

    token = do_login(helper)

    url = get_api_endpoint(data_collector).format(id=vehicle_id)

    helper.log_info("Collecting data from url={}".format(url))

    request = {
        'verify' : global_verify_ssl,
        "headers" : {
            'Authorization': 'Bearer ' + token,
            'Content-Type':  'application/json'
        }
    }

    response = helper.send_http_request(
        url,
        "GET",
        use_proxy=True,
        **request
    )

    try:
        response.raise_for_status()
    except:
        helper.log_warning("Error from API - {}".format(response.content))
        try:
            response_json = response.json()
            if 'error' in response_json:
                if response_json['error'] == 'vehicle unavailable: {:error=>"vehicle unavailable:"}':
                    helper.log_warning("Vehicle is offline - Ending poll")
                    exit(0)
        except:
            pass


    response_json = response.json()

    if data_collector=="supercharger":
        for data in response_json["response"]["superchargers"]:
            event = helper.new_event(source=helper.get_input_type(), index=helper.get_output_index(), sourcetype=data_collector, data=json.dumps(data))
            ew.write_event(event)
    else:
        #helper.log_info("Logging payload")
        #helper.log_info(response_json)
        event = helper.new_event(source=helper.get_input_type(), index=helper.get_output_index(), sourcetype=data_collector, data=json.dumps(response_json['response']))
        ew.write_event(event)
