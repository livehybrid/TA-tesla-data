import import_declare_test
import sys
import json

from tesla_modinput import TeslaModInput
from splunklib import modularinput as smi

class TOKEN_REFRESHER(TeslaModInput):
    def __init__(self):
        super(TOKEN_REFRESHER, self).__init__(self.restPath, "token_refresher")

    def get_scheme(self):
        scheme = smi.Scheme('token_refresher')
        scheme.description = 'Token Refresher'
        scheme.use_external_validation = True
        scheme.streaming_mode_xml = True
        scheme.use_single_instance = False

        scheme.add_argument(
            smi.Argument(
                'name',
                title='Name',
                description='Name',
                required_on_create=True
            )
        )

        scheme.add_argument(
            smi.Argument(
                'account',
                required_on_create=True,
            )
        )

        scheme.add_argument(
            smi.Argument(
                'help_link',
                required_on_create=False,
            )
        )

        return scheme

    def validate_input(self, definition):
        return


    def collect_data(self, inputs, ew):
        for input_name, input_item in inputs.inputs.items():
            self.account=input_item['account']

            refresh_token = self.get_refresh_token(self.account)

            # Do refresh
            isSuccess = False
            try:
                access_token, refresh_token = self.refresh_access_token(refresh_token)
                if access_token != "":
                    isSuccess=True
                    self.account_conf.update(self.account, {"access_token":access_token, "refresh_token": refresh_token},["access_token","refresh_token"])
                    self.log_info("Updated access and refresh token for Tesla account")

            finally:
                event_output = {}
                event_output['name'] = input_name
                event_output['action'] = "token_refresh"
                event_output['success'] = isSuccess

                event = smi.Event(
                    data=json.dumps(event_output),
                    sourcetype='tesla_token_refresher',
                )
                ew.write_event(event)

if __name__ == '__main__':
    exit_code = TOKEN_REFRESHER().run(sys.argv)
    sys.exit(exit_code)