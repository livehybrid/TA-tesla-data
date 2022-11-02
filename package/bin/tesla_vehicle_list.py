import import_declare_test
import sys
import json

from splunklib import modularinput as smi
from tesla_modinput import TeslaModInput

class TESLA_VEHICLE_LIST(TeslaModInput):

    def __init__(self):
        super(TESLA_VEHICLE_LIST, self).__init__(self.restPath, "tesla_vehicle_list", False)

    def get_scheme(self):
        scheme = smi.Scheme('tesla_vehicle_list')
        scheme.description = 'Vehicle List'
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
        
        return scheme

    def validate_input(self, definition):
        return

    def collect_data(self, inputs, ew):
        for input_name, input_item in inputs.inputs.items():
            accountName = input_item['account']

            url = self.get_api_endpoint("vehicle_list")
            response = self.get_owner_api(accountName, url)
            response_json = response.json()
            for vehicle in response_json['response']:
                event = self.new_event(source=self.get_input_type(), index=self.get_output_index(), sourcetype="tesla:vehicle:list", data=json.dumps(vehicle))
                ew.write_event(event)

if __name__ == '__main__':
    exit_code = TESLA_VEHICLE_LIST().run(sys.argv)
    sys.exit(exit_code)