import import_declare_test
import sys
import json
import requests
from splunklib import modularinput as smi
from tesla_modinput import TeslaModInput
import uuid

class COLLECT_SUC_DATA(TeslaModInput):
    def __init__(self):
        super(COLLECT_SUC_DATA, self).__init__(self.restPath, "tesla_collect_tp_suc_data", False)

    def get_scheme(self):
        scheme = smi.Scheme('tesla_collect_tp_suc_data')
        scheme.description = 'GraphQL Supercharger data collection'
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
                'user_lat_long',
                required_on_create=True,
            )
        )

        scheme.add_argument(
            smi.Argument(
                'northwest_lat_long',
                required_on_create=True,
            )
        )

        scheme.add_argument(
            smi.Argument(
                'southeast_lat_long',
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
            self.stanza = input_item
            access_token = self.get_access_token(self.account)
            headers = {
                "content-type" : "application/json",
                "accept" : "*/*",
                "authorization" : f"Bearer {access_token}",
                "accept-language" : "en-GB",
                "x-txid" : str(uuid.uuid4()),
                "user-agent" : "Tesla/1067 CFNetwork/1333.0.4 Darwin/21.5.0",
                "x-tesla-user-agent" : "TeslaApp/4.9.1/6284bd0192/ios/15.5",
            }
            # url = "https://ownership.tesla.com/graphql?deviceLanguage=en&deviceCountry=GB&vin=5YJ3F7EBXKF439354&operationName=GetChargingSiteDetails"
            # body = "{\"query\":\"\\n    query GetChargingSiteDetails($siteId: String!, $deviceLanguage: String!, $deviceCountry: String!) {\\n  charging {\\n    siteDetails(\\n      siteId: $siteId\\n      deviceCountry: $deviceCountry\\n      deviceLanguage: $deviceLanguage\\n    ) {\\n      siteStatic {\\n        ...SiteStaticFragment\\n      }\\n      siteDynamic {\\n        ...SiteDynamicFragment\\n      }\\n    }\\n  }\\n}\\n    \\n    fragment SiteStaticFragment on ChargingSiteStaticType {\\n  address {\\n    ...AddressFragment\\n  }\\n  amenities\\n  centroid {\\n    ...EnergySvcCoordinateTypeFields\\n  }\\n  entryPoint {\\n    ...EnergySvcCoordinateTypeFields\\n  }\\n  id {\\n    text\\n  }\\n  accessCode {\\n    value\\n  }\\n  localizedSiteName {\\n    value\\n  }\\n  maxPowerKw {\\n    value\\n  }\\n  name\\n  openToPublic\\n  posts {\\n    id {\\n      text\\n    }\\n    label {\\n      value\\n    }\\n  }\\n  holdAmount {\\n    currencyCode\\n    holdAmount\\n  }\\n  publicStallCount\\n  timeZone {\\n    id\\n    version\\n  }\\n}\\n    \\n    fragment AddressFragment on EnergySvcAddressType {\\n  streetNumber {\\n    value\\n  }\\n  street {\\n    value\\n  }\\n  district {\\n    value\\n  }\\n  city {\\n    value\\n  }\\n  state {\\n    value\\n  }\\n  postalCode {\\n    value\\n  }\\n  country\\n}\\n    \\n\\n    fragment EnergySvcCoordinateTypeFields on EnergySvcCoordinateType {\\n  latitude\\n  longitude\\n}\\n    \\n\\n    fragment SiteDynamicFragment on ChargingSiteDynamicType {\\n  id {\\n    text\\n  }\\n  activeOutages {\\n    message\\n  }\\n  postsAvailable {\\n    value\\n  }\\n  postAvailabilities {\\n    post {\\n      id {\\n        text\\n      }\\n      label {\\n        value\\n      }\\n      name\\n    }\\n    availability\\n  }\\n}\\n    \",\"variables\":{\"siteId\":\"d9bf299d-d671-4f01-a47f-d933acd80520\",\"deviceLanguage\":\"en\",\"deviceCountry\":\"GB\"},\"operationName\":\"GetChargingSiteDetails\"}"
            # resp = requests.post(
            #     url,
            #     data=body,
            #     headers = headers,
            #     # proxies={"http":"http://192.168.0.129:8888","https":"http://192.168.0.129:8888"},
            #     # verify=False
            # )

            user_lat_long = self.stanza['user_lat_long'].split(",")
            southeast_lat_long = self.stanza['southeast_lat_long'].split(",")
            northwest_lat_long = self.stanza['northwest_lat_long'].split(",")
            url = "https://ownership.tesla.com/graphql?deviceLanguage=en&deviceCountry=GB&vin=&operationName=GetNearbyChargingSites"
            body = "{\"query\":\"\\n    query GetNearbyChargingSites($args: GetNearbyChargingSitesRequestType!) {\\n  charging {\\n    nearbySites(args: $args) {\\n      sitesAndDistances {\\n        ...ChargingNearbySitesFragment\\n      }\\n    }\\n  }\\n}\\n    \\n    fragment ChargingNearbySitesFragment on ChargerSiteAndDistanceType {\\n  activeOutages {\\n    message\\n  }\\n  availableStalls {\\n    value\\n  }\\n  centroid {\\n    ...EnergySvcCoordinateTypeFields\\n  }\\n  drivingDistanceMiles {\\n    value\\n  }\\n  entryPoint {\\n    ...EnergySvcCoordinateTypeFields\\n  }\\n  haversineDistanceMiles {\\n    value\\n  }\\n  id {\\n    text\\n  }\\n  localizedSiteName {\\n    value\\n  }\\n  maxPowerKw {\\n    value\\n  }\\n  totalStalls {\\n    value\\n  }\\n}\\n    \\n    fragment EnergySvcCoordinateTypeFields on EnergySvcCoordinateType {\\n  latitude\\n  longitude\\n}\\n    \",\"variables\":{\"args\":{\"userLocation\":{\"latitude\":"+user_lat_long[0]+",\"longitude\":"+user_lat_long[1]+"},\"northwestCorner\":{\"latitude\":"+northwest_lat_long[0]+",\"longitude\":"+northwest_lat_long[1]+"},\"southeastCorner\":{\"latitude\":"+southeast_lat_long[0]+",\"longitude\":"+southeast_lat_long[1]+"},\"languageCode\":\"en\",\"countryCode\":\"GB\"}},\"operationName\":\"GetNearbyChargingSites\"}"
            resp = requests.post(
                url,
                data=body,
                headers = headers,
                #proxies={"http":"http://192.168.0.129:8888","https":"http://192.168.0.129:8888"},
                #verify=False
            )
            for site in resp.json()['data']['charging']['nearbySites']['sitesAndDistances']:
                for el in site:
                    site[el] = site[el]['value'] if isinstance(site[el], dict) and 'value' in site[el] else site[el]
                    site[el] = site[el]['text'] if isinstance(site[el], dict) and 'text' in site[el] else site[el]
                event = smi.Event(
                    data=json.dumps(site),
                    sourcetype='tesla:suc:locations',
                )
                ew.write_event(event)



if __name__ == '__main__':
    exit_code = COLLECT_SUC_DATA().run(sys.argv)
    sys.exit(exit_code)