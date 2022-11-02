import import_declare_test
import sys
import json

from splunklib import modularinput as smi
from tesla_modinput import TeslaModInput

class TESLA_VEHICLE_DATA(TeslaModInput):

    def __init__(self):
        super(TESLA_VEHICLE_DATA, self).__init__(self.restPath, "tesla_vehicle_data", False)

    def get_scheme(self):
        scheme = smi.Scheme('tesla_vehicle_data')
        scheme.description = 'Vehicle Data Collector'
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

    def log_section(self, section):
        if self.wanted_sections == "" or section in self.wanted_sections.split(","):
            return True
        else:
            return False

    def collect_data(self,inputs,ew):
        for input_name, input_item in inputs.inputs.items():
            vehicle_id = input_item['vehicle_id']
            self.wanted_sections = input_item['sections']
            url = self.get_api_endpoint("vehicle_data").format(id=vehicle_id)
            self.log_info(f"Collecting car data for vehicle_id={vehicle_id}")
            accountName = input_item['account']

            response = self.get_owner_api(accountName, url)
            response_json = response.json()
            if 'error' in response_json:
                self.log_info(f"Error from API - error=\"{response_json['error']}\"")

            else:
                response_obj = response_json['response']

                for section in ["vehicle_state", "vehicle_config", "gui_settings", "drive_state", "climate_state", "charge_state"]:
                    if self.log_section(section) and section in response_obj:
                        # Add vehicle id to the data
                        response_obj[section]['vehicle'] = vehicle_id
                        response_obj[section]['account'] = accountName
                        event = self.new_event(source=self.get_input_type(), index=self.get_output_index(), sourcetype=f"tesla:vehicle:{section}", data=json.dumps(response_json['response'][section]))
                        ew.write_event(event)
                    if section in response_json['response']:
                        # Remove so it doesnt get logged in the left-over data
                        del(response_json['response'][section])

                event = self.new_event(source=self.get_input_type(), index=self.get_output_index(), sourcetype="tesla:vehicle:data", data=json.dumps(response_json['response']))
                ew.write_event(event)


if __name__ == '__main__':
    exit_code = TESLA_VEHICLE_DATA().run(sys.argv)
    sys.exit(exit_code)