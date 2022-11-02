import import_declare_test
import sys
import json

from splunklib import modularinput as smi
from tesla_modinput import TeslaModInput

class TESLA_NEARBY_SUC(TeslaModInput):

    def __init__(self):
        super(TESLA_NEARBY_SUC, self).__init__(self.restPath, "tesla_nearby_suc", False)

    def get_scheme(self):
        scheme = smi.Scheme('tesla_nearby_suc')
        scheme.description = 'Nearby SuperCharger Stats'
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
                'vehicle_id',
                required_on_create=False,
            )
        )
        
        return scheme

    def validate_input(self, definition):
        return

    def collect_data(self, inputs, ew):
        input_items = [{'count': len(inputs.inputs)}]
        for input_name, input_item in inputs.inputs.items():
            vehicle_id = input_item['vehicle_id']
            accountName = input_item['account']
            access_token = self.get_access_token(accountName)
            input_item['name'] = input_name
            url = self.get_api_endpoint("supercharger").format(id=vehicle_id)
            response = self.get_owner_api(accountName, url)
            response_json = response.json()['response']
            self.log_warning(response_json)
            for supercharger in response_json['superchargers']:
                event = self.new_event(source=self.get_input_type(), index=self.get_output_index(), sourcetype="tesla:vehicle:nearbysupercharger", data=json.dumps(supercharger))
                ew.write_event(event)

            for destcharger in response_json['destination_charging']:
                event = self.new_event(source=self.get_input_type(), index=self.get_output_index(), sourcetype="tesla:vehicle:destinationcharger", data=json.dumps(destcharger))
                ew.write_event(event)



if __name__ == '__main__':
    exit_code = TESLA_NEARBY_SUC().run(sys.argv)
    sys.exit(exit_code)