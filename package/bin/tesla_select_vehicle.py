import import_declare_test
import splunk.admin as admin
import splunk.clilib.cli_common as scc
import logging

from splunktaucclib.splunk_aoblib.setup_util import Setup_Util
from tesla_modinput import TeslaModInput

logger = logging.getLogger()

import splunktaucclib.common.log as stulog
APPNAME = "TA-tesla-data"
FIELDS = ["account"]

class TeslaVehicleSelect(admin.MConfigHandler):

    def setup(self):
        stulog.logger.error("SETUP")
        for arg in FIELDS:
            self.supportedArgs.addOptArg(arg)


    @staticmethod
    def validate_params(must_params, opt_params, **params):
        pass

    def handleList(self, confInfo):
        if not self.callerArgs or not self.callerArgs.get("account"):
            logger.error("Missing Tesla credentials")
            raise Exception("Missing Tesla credentials")
        tesla_account =self.callerArgs["account"][0]
        tesla_helper = TeslaModInput(app_namespace="TA-tesla-data", input_name="SelectVehicle")
        tesla_helper.session_key = self.getSessionKey()
        tesla_helper.splunk_uri = scc.getMgmtUri()
        tesla_helper.setup_util = Setup_Util(tesla_helper.splunk_uri, tesla_helper.session_key)

        url = tesla_helper.get_api_endpoint("vehicle_list")
        response = tesla_helper.get_owner_api(tesla_account, url)

        response_json = response.json()
        if 'error' in response_json:
            confInfo["error"]['vehicle_name'] = "Error from Tesla API - Check token is valid"
            logger.error(f"Error from API - error={response_json['error']}")
            return
        for vehicle in response_json['response']:
            confInfo[vehicle['id_s']]['vehicle_name'] = f"{tesla_account} - {vehicle['display_name']} ({vehicle['vin']})"
        return


if __name__ == "__main__":
    admin.init(TeslaVehicleSelect, admin.CONTEXT_APP_AND_USER)