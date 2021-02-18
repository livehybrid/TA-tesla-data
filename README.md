![Splunkbase Downloads](https://img.shields.io/endpoint?url=https%3A%2F%2Fsplunkbasebadge.livehybrid.com%2Fv1%2Fdownloads%2F4660?1)  ![Splunkbase Installs](https://img.shields.io/endpoint?url=https%3A%2F%2Fsplunkbasebadge.livehybrid.com%2Fv1%2Finstalls%2F4660?1)  ![Splunkbase AppInspect](https://img.shields.io/endpoint?url=https%3A%2F%2Fsplunkbasebadge.livehybrid.com%2Fv1%2Fappinspect%2F4660?1)  ![Splunkbase Compatibility](https://img.shields.io/endpoint?url=https%3A%2F%2Fsplunkbasebadge.livehybrid.com%2Fv1%2Flatest_compat%2F4660)  


# Introduction

This app collects data from the Tesla owners API. Can be configured for multiple vehicles and accounts - Perfect for visualising your usage, or fleets of cars.

After installing the app, please go to the app's Configuration page and enter the API Key/Secret key which can be found at https://akrion.docs.apiary.io/#reference/authentication

Note: The Car/Charging data collection require your Tesla to be awake, if vehicle is not awake the API returns a HTTP 408 with "Vehicle Unavailable". The script will not wake the vehicle, *however* if the vehicle is awake then running the script may keep it awake. This can cause "Phantom Drain" as various car computer systems remain online. 

## Whats in the App?
* Input - List Cars in Tesla Account
* Input - Collect data on availability of nearest Superchargers
* Input - Collect data from the car (incl Mileage, Charging, Climate - see below for more info)
* Sample Dashboards - Historic Journeys/Charging, current status, driving efficiency over time.

# Data Retrieved

## List Vehicles Data
Returns a *list* of cars in your account.  
You will need the `id_s` value for setting up the Car data collector.

```
[{
	"id": <REDACTED_FOR_README>,
	"vehicle_id": <REDACTED_FOR_README>,
	"vin": "<REDACTED_FOR_README>",
	"display_name": "MyTeslasName",
	"option_codes": "AD15,MDL3,PBSB,RENA,BT37,ID3W,RF3G,S3PB,DRLH,DV2W,W39B,APF0,COUS,BC3B,CH07,PC30,FC3P,FG31,GLFR,HL31,HM31,IL31,LTPB,MR31,FM3B,RS3H,SA3P,STCP,SC04,SU3C,T3CA,TW00,TM00,UT3P,WR00,AU3P,APH3,AF00,ZCST,MI00,CDM0",
	"color": null,
	"access_type": "OWNER",
	"tokens": ["<REDACTED_FOR_README>", "<REDACTED_FOR_README>"],
	"state": "asleep",
	"in_service": false,
	"id_s": "<REDACTED_FOR_README>",
	"calendar_enabled": true,
	"api_version": 14,
	"backseat_token": null,
	"backseat_token_updated_at": null,
	"vehicle_config": null
}]
```

## Car Data
```{
   	"response": {
   		"id": <REDACTED_FOR_README>,
   		"user_id": <REDACTED_FOR_README>,
   		"vehicle_id": <REDACTED_FOR_README>,
   		"vin": "<REDACTED_FOR_README>",
   		"display_name": "MyTeslasName",
   		"option_codes": "AD15,MDL3,PBSB,RENA,BT37,ID3W,RF3G,S3PB,DRLH,DV2W,W39B,APF0,COUS,BC3B,CH07,PC30,FC3P,FG31,GLFR,HL31,HM31,IL31,LTPB,MR31,FM3B,RS3H,SA3P,STCP,SC04,SU3C,T3CA,TW00,TM00,UT3P,WR00,AU3P,APH3,AF00,ZCST,MI00,CDM0",
   		"color": null,
   		"access_type": "OWNER",
   		"tokens": ["<REDACTED_FOR_README>", "<REDACTED_FOR_README>"],
   		"state": "online",
   		"in_service": false,
   		"id_s": "<REDACTED_FOR_README>",
   		"calendar_enabled": true,
   		"api_version": 14,
   		"backseat_token": null,
   		"backseat_token_updated_at": null,
   		"vehicle_config": {
   			"can_accept_navigation_requests": true,
   			"can_actuate_trunks": true,
   			"car_special_type": "base",
   			"car_type": "model3",
   			"charge_port_type": "CCS",
   			"default_charge_to_max": false,
   			"ece_restrictions": true,
   			"eu_vehicle": true,
   			"exterior_color": "DeepBlue",
   			"exterior_trim": "Chrome",
   			"has_air_suspension": false,
   			"has_ludicrous_mode": false,
   			"key_version": 2,
   			"motorized_charge_port": true,
   			"plg": false,
   			"rear_seat_heaters": 1,
   			"rear_seat_type": null,
   			"rhd": true,
   			"roof_color": "Glass",
   			"seat_type": null,
   			"spoiler_type": "Passive",
   			"sun_roof_installed": null,
   			"third_row_seats": "<invalid>",
   			"timestamp": 1610786032732,
   			"use_range_badging": true,
   			"wheel_type": "Stiletto20"
   		},
   		"charge_state": {
   			"battery_heater_on": false,
   			"battery_level": 61,
   			"battery_range": 164.52,
   			"charge_current_request": 16,
   			"charge_current_request_max": 16,
   			"charge_enable_request": true,
   			"charge_energy_added": 3.77,
   			"charge_limit_soc": 90,
   			"charge_limit_soc_max": 100,
   			"charge_limit_soc_min": 50,
   			"charge_limit_soc_std": 90,
   			"charge_miles_added_ideal": 15.5,
   			"charge_miles_added_rated": 15.5,
   			"charge_port_cold_weather_mode": false,
   			"charge_port_door_open": false,
   			"charge_port_latch": "Engaged",
   			"charge_rate": 0.0,
   			"charge_to_max_range": false,
   			"charger_actual_current": 0,
   			"charger_phases": null,
   			"charger_pilot_current": 16,
   			"charger_power": 0,
   			"charger_voltage": 1,
   			"charging_state": "Disconnected",
   			"conn_charge_cable": "<invalid>",
   			"est_battery_range": 86.96,
   			"fast_charger_brand": "<invalid>",
   			"fast_charger_present": false,
   			"fast_charger_type": "<invalid>",
   			"ideal_battery_range": 164.52,
   			"managed_charging_active": false,
   			"managed_charging_start_time": null,
   			"managed_charging_user_canceled": false,
   			"max_range_charge_counter": 0,
   			"minutes_to_full_charge": 0,
   			"not_enough_power_to_heat": null,
   			"scheduled_charging_pending": false,
   			"scheduled_charging_start_time": null,
   			"time_to_full_charge": 0.0,
   			"timestamp": 1610786032732,
   			"trip_charging": false,
   			"usable_battery_level": 56,
   			"user_charge_enable_request": null
   		},
   		"climate_state": {
   			"battery_heater": false,
   			"battery_heater_no_power": null,
   			"climate_keeper_mode": "off",
   			"defrost_mode": 0,
   			"driver_temp_setting": 20.0,
   			"fan_status": 0,
   			"inside_temp": 0.3,
   			"is_auto_conditioning_on": false,
   			"is_climate_on": false,
   			"is_front_defroster_on": false,
   			"is_preconditioning": false,
   			"is_rear_defroster_on": false,
   			"left_temp_direction": 1009,
   			"max_avail_temp": 28.0,
   			"min_avail_temp": 15.0,
   			"outside_temp": 0.5,
   			"passenger_temp_setting": 20.0,
   			"remote_heater_control_enabled": false,
   			"right_temp_direction": 1009,
   			"seat_heater_left": 0,
   			"seat_heater_rear_center": 0,
   			"seat_heater_rear_left": 0,
   			"seat_heater_rear_right": 0,
   			"seat_heater_right": 0,
   			"side_mirror_heaters": false,
   			"timestamp": 1610786032732,
   			"wiper_blade_heater": false
   		},
   		"drive_state": {
   			"gps_as_of": 1610785841,
   			"heading": 304,
   			"latitude": <REDACTED_FOR_README>,
   			"longitude": <REDACTED_FOR_README>,
   			"native_latitude": <REDACTED_FOR_README>,
   			"native_location_supported": 1,
   			"native_longitude": <REDACTED_FOR_README>,
   			"native_type": "wgs",
   			"power": 0,
   			"shift_state": null,
   			"speed": null,
   			"timestamp": 1610786032732
   		},
   		"gui_settings": {
   			"gui_24_hour_time": true,
   			"gui_charge_rate_units": "kW",
   			"gui_distance_units": "mi/hr",
   			"gui_range_display": "Rated",
   			"gui_temperature_units": "C",
   			"show_range_units": false,
   			"timestamp": 1610786032732
   		},
   		"vehicle_state": {
   			"api_version": 14,
   			"autopark_state_v2": "unavailable",
   			"calendar_supported": true,
   			"car_version": "2020.48.30 040912887bad",
   			"center_display_state": 0,
   			"df": 0,
   			"dr": 0,
   			"fd_window": 0,
   			"fp_window": 0,
   			"ft": 0,
   			"is_user_present": false,
   			"locked": true,
   			"media_state": {
   				"remote_control_enabled": true
   			},
   			"notifications_supported": true,
   			"odometer": 10972.046274,
   			"parsed_calendar_supported": true,
   			"pf": 0,
   			"pr": 0,
   			"rd_window": 0,
   			"remote_start": false,
   			"remote_start_enabled": true,
   			"remote_start_supported": true,
   			"rp_window": 0,
   			"rt": 0,
   			"sentry_mode": false,
   			"sentry_mode_available": true,
   			"software_update": {
   				"download_perc": 0,
   				"expected_duration_sec": 2700,
   				"install_perc": 1,
   				"status": "",
   				"version": "2020.48.30"
   			},
   			"speed_limit_mode": {
   				"active": false,
   				"current_limit_mph": 50.0,
   				"max_limit_mph": 90,
   				"min_limit_mph": 50,
   				"pin_code_set": true
   			},
   			"timestamp": 1610786032732,
   			"valet_mode": false,
   			"vehicle_name": "MyTeslasName"
   		}
   	}
   }
```

# Local* Supercharger Data
Returns your nearest 4 Superchargers and Destination Chargers, along with availability information for the Superchargers (Stalls/Availability).

```$xslt
{
	"response": {
		"congestion_sync_time_utc_secs": 1610794377,
		"destination_charging": [{
			"location": {
				"lat": 53.802178,
				"long": -1.543019
			},
			"name": "CitiPark Merrion Centre",
			"type": "destination",
			"distance_miles": 4.684237
		}, {
			"location": {
				"lat": 53.790416,
				"long": -1.530348
			},
			"name": "CitiPark Leeds Dock",
			"type": "destination",
			"distance_miles": 5.635666
		}, {
			"location": {
				"lat": 53.973773,
				"long": -1.492644
			},
			"name": "Rudding Park Hotel",
			"type": "destination",
			"distance_miles": 9.87527
		}, {
			"location": {
				"lat": 53.996658,
				"long": -1.540473
			},
			"name": "The Camberley",
			"type": "destination",
			"distance_miles": 10.493266
		}],
		"superchargers": [{
			"location": {
				"lat": 53.784556,
				"long": -1.532498
			},
			"name": "Leeds-Whitehouse Street, UK",
			"type": "supercharger",
			"distance_miles": 5.894953,
			"available_stalls": 6,
			"total_stalls": 8,
			"site_closed": false
		}, {
			"location": {
				"lat": 53.732774,
				"long": -1.585622
			},
			"name": "Leeds, UK",
			"type": "supercharger",
			"distance_miles": 8.377563,
			"available_stalls": 0,
			"total_stalls": 2,
			"site_closed": false
		}, {
			"location": {
				"lat": 53.489393,
				"long": -1.486223
			},
			"name": "Barnsley, UK",
			"type": "supercharger",
			"distance_miles": 25.666967,
			"available_stalls": 2,
			"total_stalls": 2,
			"site_closed": false
		}, {
			"location": {
				"lat": 53.430272,
				"long": -2.179346
			},
			"name": "Manchester-South, UK",
			"type": "supercharger",
			"distance_miles": 37.071037,
			"available_stalls": 6,
			"total_stalls": 8,
			"site_closed": false
		}],
		"timestamp": 1610794545215
	}
}
```


# Installation
Download the latest release from [SplunkBase](https://splunkbase.splunk.com/app/4660/) or [Github](https://github.com/livehybrid/TA-tesla-data/releases).  
The app was designed to run on a single Splunk instance or a single Search Head as part of a bigger system, however other deployment combinations will work.  

Once installed, visit https://akrion.docs.apiary.io/#reference/authentication to get the latest API Client Key/Secret and enter this in the Application's configuration page->Add-On Settings (http://yourSplunkInstance:8000/en-US/app/TA-tesla-data/configuration#add-on-settings).  

Create a new app from the Inputs screen and select "Vehicle List" to collect basic details about the vehicle(s) in your account.  
Once setup it will run immediately, after ~30 seconds you should see the data in the index you selected when creating the input. Search this index for the newly collected data and obtain the value of the `id_s` field.  

Now create a new input for `Specific Vehicle Data` and/or `Specific Vehicle Supercharger details` depending on your requirements.

# Dashboards
The dashboards within the app are Work-In-Progress and do not necessarily follow best practice.
Further work is required to make better use of base searches
Some dashboards make use of the [Location Tracker App](https://splunkbase.splunk.com/app/3164/) 

## Screenshots
#### Overview
![Overview](https://user-images.githubusercontent.com/5527349/104831042-eb315580-587c-11eb-840f-eff44f7524dd.png)

#### Charging Events
Click-through to see single event  
![Charging Events](https://user-images.githubusercontent.com/5527349/104831030-b7563000-587c-11eb-9212-f08aae94b17b.png)

#### Single Charging Event
![Single Charging Event](https://user-images.githubusercontent.com/5527349/104831039-db197600-587c-11eb-9604-a4db96e7b1f3.png)


# ToDo
New modular input to write only metrics, this will improve performance of searches.  
Additional Journey plotting dashboard(s) 
Battery Health / Efficiency Dashboard  
Use base searches within Dashboards  
Use Macros within the Dashboards
