
# encoding = utf-8

import os
import sys
import time
import datetime
import json
import splunklib.client as client



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

def get_api_session(helper):
    login_url = get_api_endpoint("auth")
    
    login_request = {
        'payload' : {
            'grant_type':'password',
            'email':helper.get_arg('tesla_email'), 
            'password':helper.get_arg('tesla_password'),
            'client_id':helper.get_global_setting("api_clientid"),
            'client_secret':helper.get_global_setting("api_client_secret")
        },
        'verify' : False
    }
# bool(helper.get_global_setting("verify_ssl"))
    
    login_response = helper.send_http_request(login_url, "POST", **login_request)
    login_response.raise_for_status()
    
    return login_response.json()['access_token']

def do_login(helper):
    token_realm = helper.get_input_type()
    tesla_username = helper.get_arg('tesla_email')

    splunkService = client.connect(token=helper.context_meta['session_key'])
    storage_passwords = splunkService.storage_passwords
    returned_credential = [k for k in storage_passwords if k.content.get('realm')==token_realm and k.content.get('username')==tesla_username]

    try:
        token = returned_credential[0].content.get('clear_password')
    except:
        helper.log_warning("No token found - doing login...")
        token = get_api_session(helper=helper)
        try:
            splunkService.storage_passwords.delete(username=tesla_username, realm=token_realm)
        except:
            pass

        splunkService.storage_passwords.create(token, tesla_username, realm=token_realm)
    return token    

def collect_events(helper, ew):

    global_verify_ssl = helper.get_global_setting("verify_ssl")
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
    
 #bool(helper.get_global_setting("verify_ssl")),
    
    request = {
        'verify' : False, 
        "headers" : {
            'Authorization': 'Bearer ' + token,
            'Content-Type':  'application/json'
        }
    }
    
    
        
    response = helper.send_http_request(url, "GET", **request)

    try:
        response.raise_for_status()
    except:
        helper.log_warning(response.content)
        helper.log_warning("Error from API - Deleting existing token")
        helper.log_warning(response.json()['error'])
        try:
            response_json = response.json()
            if 'error' in response_json:
                helper.log_error(response_json['error'])
        except:
            pass

        #TODO - Check if auth error (401) or other?
        splunkService = client.connect(token=helper.context_meta['session_key'])
        token_realm = helper.get_input_type()
        try:
            splunkService.storage_passwords.delete(username=tesla_username, realm=token_realm)
        except:
            helper.log_warning("Could not delete existing token from password store")
            exit(1)
    response_json = response.json()
    
    if data_collector=="supercharger":
        for data in response_json["response"]["superchargers"]:
            event = helper.new_event(source=helper.get_input_type(), index=helper.get_output_index(), sourcetype=data_collector, data=json.dumps(data))
            ew.write_event(event)
    else:
        
        event = helper.new_event(source=helper.get_input_type(), index=helper.get_output_index(), sourcetype=data_collector, data=json.dumps(response_json['response']))
        ew.write_event(event)
    
