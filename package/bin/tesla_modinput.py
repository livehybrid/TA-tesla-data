import import_declare_test
from splunktaucclib.modinput_wrapper.base_modinput import BaseModInput
from splunktaucclib.splunk_aoblib.setup_util import Setup_Util
import splunk.Intersplunk as si
from solnlib import conf_manager
from splunklib import client as client
import json

class TeslaModInput(BaseModInput):
    appName = "TA-tesla-data"
    restPath = "ta_tesla_data"

    def get_api_endpoint(self, name):
        if name == "token":
            return "https://auth.tesla.com/oauth2/v3/token"
        api_endpoints = {
            "vehicle_data" : "/api/1/vehicles/{id}/vehicle_data",
            "vehicle_list" : "/api/1/vehicles",
            "supercharger" : "/api/1/vehicles/{id}/nearby_charging_sites",
        }
        return "https://owner-api.teslamotors.com" + api_endpoints.get(name)

    def refresh_access_token(self, refresh_token):
        refresh_url = self.get_api_endpoint("token")
        self.log_debug(f"Using url={refresh_url}")
        refresh_request = {
            'payload' : {
                'grant_type':'refresh_token',
                'client_id': 'ownerapi',
                'scope': 'openid email offline_access',
                'refresh_token': refresh_token
            },
            'verify' : True
        }

        refresh_response = self.send_http_request(refresh_url, "POST", **refresh_request)
        refresh_response.raise_for_status()
        response_json = refresh_response.json()
        if 'access_token' in response_json:
            return response_json['access_token'], response_json['refresh_token']
        else:
            return ""

    def get_access_token_legacy(self, accountName):
        token_realm = f"__REST_CREDENTIAL__#{self.appName}#configs/conf-{self.restPath}_account"
        tesla_username = accountName

        splunkService = client.connect(token=self.session_key)
        storage_passwords = splunkService.storage_passwords
        returned_credential = "".join([k['clear_password'] for k in storage_passwords if k.content.get('realm')==token_realm and k.content.get('username').startswith(f"{tesla_username}``splunk_cred_sep")])
        returned_credential = returned_credential.replace("``splunk_cred_sep``S``splunk_cred_sep``P``splunk_cred_sep``L``splunk_cred_sep``U``splunk_cred_sep``N``splunk_cred_sep``K``splunk_cred_sep``","")
        returned_credential_json = json.loads(returned_credential)
        try:
            token = returned_credential_json['access_token']
            return token
        except(Exception) as e:
            self.log_warning("No token found")
            self.log_warning(e)
            return False

    def collect_data(self, inputs, ew):
        pass

    def stream_events(self, inputs, ew):
        self.context_meta = inputs.metadata
        self.session_key = inputs.metadata['session_key']
        self.splunk_uri = inputs.metadata['server_uri']
        self.setup_util = Setup_Util(self.splunk_uri, self.session_key)
        self.collect_data(inputs,ew)

    def get_refresh_token(self, accountName):
        return self.get_account_credentials(accountName=accountName)['refresh_token']

    def get_access_token(self, accountName):
        return self.get_account_credentials(accountName=accountName)['access_token']

    def get_account_credentials(self, accountName):
        account_cfm = conf_manager.ConfManager(
            self.session_key,
            self.appName,
            realm=f"__REST_CREDENTIAL__#{self.appName}#configs/conf-{self.restPath}_account"
        )

        # Check if account is empty
        if not accountName:  # pylint: disable=E1101
            si.generateErrorResults("Enter Tesla account name.")
            raise Exception(
                "Account name cannot be empty. Enter a configured account name or "
                "create new account by going to Configuration page of the Add-on."
            )
        # Get account details

        self.log_info("Getting details for account '{}'".format(accountName) )
        self.account_conf = account_cfm.get_conf(
            f"{self.restPath}_account"
        )
        account_details = self.account_conf.get(accountName)
        return account_details

    def get_owner_api(self, accountName, url):
        access_token = self.get_access_token(accountName)
        request = {
            'verify' : False,
            "headers" : {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type':  'application/json'
            }
        }
        response = self.send_http_request(url, "GET", **request)
        try:
            response.raise_for_status()
        except:
            uri = f"{self.splunk_uri}/services/messages/new"
            headers = {}
            headers['Authorization'] = 'Splunk ' + self.session_key
            data ={'name':"Tesla App",'value':"Unable to renew auth token",'severity':"warn"}
            message_req = {
                "headers":headers,
                "payload":data,
                "verify":False
            }
            r = self.send_http_request(uri,"POST", headers=headers, payload=data, verify=False)
            if r.status_code<300:
                self.log_info("Logged message to UI")
            else:
                self.log_info(f"Resp from message API - status_code={r.status_code}")
            # {"error":"invalid bearer token"}
            self.log_warning("Error from API")
        return response
