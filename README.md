![Splunkbase Downloads](https://img.shields.io/endpoint?url=https%3A%2F%2Fsplunkbasebadge.livehybrid.com%2Fv1%2Fdownloads%2F4660?1)  ![Splunkbase AppInspect](https://img.shields.io/endpoint?url=https%3A%2F%2Fsplunkbasebadge.livehybrid.com%2Fv1%2Fappinspect%2F4660?1)  ![Splunkbase Compatibility](https://img.shields.io/endpoint?url=https%3A%2F%2Fsplunkbasebadge.livehybrid.com%2Fv1%2Flatest_compat%2F4660)


# Introduction

This app collects data from the Tesla owners API. Can be configured for multiple vehicles and accounts - Perfect for visualising your usage, or fleets of cars.

Note: The Car/Charging data collection require your Tesla to be awake, if vehicle is not awake the API returns a HTTP 408 with "Vehicle Unavailable". The script will not wake the vehicle, *however* if the vehicle is awake then running the script may keep it awake. This can cause "Phantom Drain" as various car computer systems remain online.

*Important* - This app requires ucc-gen to build a ready-to-run app, this repo only contains the files to produce the app. Details on how to build the app yourself will be updated in the near future. Please use SplunkBase or the Releases section of this repo for the produced app.

## What's in the box?
### Configuration

### Inputs
The app contains 5 modular inputs which can be used for pulling data from the Tesla API relating to your vehicle(s):
1. **Vehicle Data Collector** - This collects a wealth of data from the vehicle API, such as charge state,  vehicle state, vehicle configurations and more. See the sample data below for more info.
2. **Vehicle List** - A list of vehicles in your account, this was originally helpful for detecting your vehicle ID for use in other inputs, but does show other helpful information such as if the vehicle is online.
3. **Nearby SuperCharger Stats** - This returns the Supercharger and Destination chargers that are displayed within the Tesla App, along with availability (where possible), helpful for determining when chargers nearby are quiet/busy.
4. **Token Refresher** - This critical component refreshes the *access_token* and stores it for use by other components. Run one of these per Account configured.
5. **GraphQL Supercharger data collection** - This returns information from Tesla's GraphQL API service and shows the availability and further information about Superchargers which are open for [Non-Tesla charging](https://www.tesla.com/en_GB/support/non-tesla-supercharging), currently being pilotted in selected UK and European locations.

### Dashboards
1. Tesla Car Overview (/en-US/app/TA-tesla-data/tesla_car)
2. Tesla - Non-Tesla Capable Superchargers (/en-US/app/TA-tesla-data/tesla_nontes_supercharging)

## Recommended additional apps:
* [Maps+ for Splunk](https://splunkbase.splunk.com/app/3124)
* [Location Tracker - Custom Visualization](https://splunkbase.splunk.com/app/3164)

These apps are used to display location visualisations on the Car overview and Supercharger dashboards.

## Configuration
The first thing you will need to do is head over to the configuration page and hit the **green** "Add" button to setup access to your Tesla account.

You need to give your Tesla account a unique name and add your *refresh* and *access* token. Strictly speaking you do not need to add the access token, as this can be retrieved with the `Token Refresher` modinput but it will speed up your setup to include it here. These tokens are [stored securely](https://www.splunk.com/en_us/blog/tips-and-tricks/store-encrypted-secrets-in-a-splunk-app.html) on your Splunk instance.

**Wait, how do I find my Tesla authentication tokens?**  
The easiest way to get your authentication tokens is using an app (below), but can also be extracted [other ways](https://tesla-info.com/tesla-token.php).

### Auth Token apps:

[Auth app for Tesla (iOS, macOS)](https://apps.apple.com/us/app/auth-app-for-tesla/id1552058613)  
[Tesla Tokens (Android)](https://play.google.com/store/apps/details?id=net.leveugle.teslatokens)  
[Tesla Auth (macOS, Linux, Windows)](https://github.com/adriankumpf/tesla_auth)

## Setup Inputs
Go to the Inputs page to setup your data collectors.

**Important** - The Token Refresher input should be setup first in order to ensure that your *access_token* is updated and available for use by the other inputs. Typically tokens last for 8 hours but the default refresh interval is set to 1 hour in the Splunk input config.

Most of the inputs configuration is straight forward, the "Vehicle Data Collector" and "Nearby SuperCharger Stats" requires you to enter your Vehicle ID, however after selecting your Tesla account from the dropdown the modal will update with a dropdown list of your vehicles using the API to populate the list, making it simple to select your vehicle and continue.

The "GraphQL Supercharger data collection" inputs require additional parameters, the Center point is typically what is used as your "current location" (or the center of the area you want to search), the North-West is the top-left of a square area you want to cover, and South-East is the bottom-right of the square area to cover. The value of these fields should be `lat,long`, comma-separated with no space.  
Two example inputs for the UK and Europe have been configured but need updating to select your Tesla Account for authentication.

# Data Retrieved

## "Vehicle Data Collector"
## tesla:vehicle:vehicle_state
```
{
   account: MyTeslaAccountName
   api_version: 45
   autopark_state_v2: unavailable
   calendar_supported: true
   car_version: 2022.28.1 f69f4df0ff1f
   center_display_state: 0
   dashcam_clip_save_available: true
   dashcam_state: Recording
   df: 0
   dr: 0
   fd_window: 0
   feature_bitmask: b9ff,0
   fp_window: 0
   ft: 0
   is_user_present: false
   locked: true
   media_state: {
     remote_control_enabled: true
   }
   notifications_supported: true
   odometer: 23648.004545
   parsed_calendar_supported: true
   pf: 0
   pr: 0
   rd_window: 0
   remote_start: false
   remote_start_enabled: true
   remote_start_supported: true
   rp_window: 0
   rt: 0
   santa_mode: 0
   sentry_mode: true
   sentry_mode_available: true
   service_mode: false
   service_mode_plus: false
   software_update: {
     download_perc: 100
     expected_duration_sec: 1500
     install_perc: 10
     status: available
     version: 2022.36.6
   }
   speed_limit_mode: {
     active: false
     current_limit_mph: 50
     max_limit_mph: 120
     min_limit_mph: 50
     pin_code_set: true
   }
   timestamp: 1667383461962
   tpms_hard_warning_fl: false
   tpms_hard_warning_fr: false
   tpms_hard_warning_rl: false
   tpms_hard_warning_rr: false
   tpms_last_seen_pressure_time_fl: 1667381602
   tpms_last_seen_pressure_time_fr: 1667381606
   tpms_last_seen_pressure_time_rl: 1667381606
   tpms_last_seen_pressure_time_rr: 1667381606
   tpms_pressure_fl: 2.525
   tpms_pressure_fr: 2.55
   tpms_pressure_rl: 2.7
   tpms_pressure_rr: 2.625
   tpms_rcp_front_value: 2.9
   tpms_rcp_rear_value: 2.9
   tpms_soft_warning_fl: false
   tpms_soft_warning_fr: false
   tpms_soft_warning_rl: false
   tpms_soft_warning_rr: false
   valet_mode: false
   valet_pin_needed: true
   vehicle: 12345678910111213
   vehicle_name: MyCarsName
   vehicle_self_test_progress: 0
   vehicle_self_test_requested: false
   webcam_available: true
}
```

## tesla:vehicle:charge_state
```
{
   account: MyTeslaAccountName
   battery_heater_on: false
   battery_level: 69
   battery_range: 198.31
   charge_amps: 16
   charge_current_request: 16
   charge_current_request_max: 16
   charge_enable_request: true
   charge_energy_added: 15.5
   charge_limit_soc: 70
   charge_limit_soc_max: 100
   charge_limit_soc_min: 50
   charge_limit_soc_std: 90
   charge_miles_added_ideal: 63.5
   charge_miles_added_rated: 63.5
   charge_port_cold_weather_mode: false
   charge_port_color: <invalid>
   charge_port_door_open: false
   charge_port_latch: Engaged
   charge_rate: 0
   charge_to_max_range: false
   charger_actual_current: 0
   charger_phases: null
   charger_pilot_current: 16
   charger_power: 0
   charger_voltage: 2
   charging_state: Disconnected
   conn_charge_cable: <invalid>
   est_battery_range: 110.31
   fast_charger_brand: <invalid>
   fast_charger_present: false
   fast_charger_type: <invalid>
   ideal_battery_range: 198.31
   managed_charging_active: false
   managed_charging_start_time: null
   managed_charging_user_canceled: false
   max_range_charge_counter: 0
   minutes_to_full_charge: 0
   not_enough_power_to_heat: null
   off_peak_charging_enabled: false
   off_peak_charging_times: all_week
   off_peak_hours_end_time: 360
   preconditioning_enabled: false
   preconditioning_times: all_week
   scheduled_charging_mode: Off
   scheduled_charging_pending: false
   scheduled_charging_start_time: null
   scheduled_charging_start_time_app: 0
   scheduled_departure_time: 1603958400
   scheduled_departure_time_minutes: 480
   supercharger_session_trip_planner: false
   time_to_full_charge: 0
   timestamp: 1667383041781
   trip_charging: false
   usable_battery_level: 68
   user_charge_enable_request: null
   vehicle: 12345678910111213
}
```

## tesla:vehicle:vehicle_config
```
{
   account: MyTeslaAccountName
   aux_park_lamps: Eu
   badge_version: 0
   can_accept_navigation_requests: true
   can_actuate_trunks: true
   car_special_type: base
   car_type: model3
   charge_port_type: CCS
   dashcam_clip_save_supported: true
   default_charge_to_max: false
   driver_assist: TeslaAP3
   ece_restrictions: true
   efficiency_package: Default
   eu_vehicle: true
   exterior_color: DeepBlue
   exterior_trim: Chrome
   exterior_trim_override: Chrome
   has_air_suspension: false
   has_ludicrous_mode: false
   has_seat_cooling: false
   headlamp_type: Premium
   interior_trim_type: Black
   key_version: 2
   motorized_charge_port: true
   paint_color_override: 0,9,26,0.9,0.01
   performance_package: Performance
   plg: false
   pws: false
   rear_drive_unit: PM216MOSFET
   rear_seat_heaters: 1
   rear_seat_type: 0
   rhd: true
   roof_color: RoofColorGlass
   seat_type: null
   spoiler_type: Passive
   sun_roof_installed: null
   supports_qr_pairing: false
   third_row_seats: None
   timestamp: 1667383041781
   trim_badging: p74d
   use_range_badging: true
   utc_offset: 3600
   vehicle: 1492931016169247
   webcam_supported: true
   wheel_type: Stiletto20
}
```

## tesla:vehicle:climate_state
```
{
   account: MyTeslaAccountName
   allow_cabin_overheat_protection: true
   auto_seat_climate_left: true
   auto_seat_climate_right: true
   battery_heater: false
   battery_heater_no_power: null
   cabin_overheat_protection: Off
   cabin_overheat_protection_actively_cooling: false
   climate_keeper_mode: off
   defrost_mode: 0
   driver_temp_setting: 20.5
   fan_status: 0
   hvac_auto_request: On
   inside_temp: 10.5
   is_auto_conditioning_on: false
   is_climate_on: false
   is_front_defroster_on: false
   is_preconditioning: false
   is_rear_defroster_on: false
   left_temp_direction: 0
   max_avail_temp: 28
   min_avail_temp: 15
   outside_temp: 8.5
   passenger_temp_setting: 20.5
   remote_heater_control_enabled: false
   right_temp_direction: 0
   seat_heater_left: 0
   seat_heater_rear_center: 0
   seat_heater_rear_left: 0
   seat_heater_rear_right: 0
   seat_heater_right: 0
   side_mirror_heaters: false
   supports_fan_only_cabin_overheat_protection: true
   timestamp: 1667383041781
   vehicle: 12345678910111213
   wiper_blade_heater: false
}
```

## tesla:vehicle:gui_settings
```
{
   account: MyTeslaAccountName
   gui_24_hour_time: true
   gui_charge_rate_units: kW
   gui_distance_units: mi/hr
   gui_range_display: Rated
   gui_temperature_units: C
   gui_tirepressure_units: Psi
   show_range_units: false
   timestamp: 1667383041781
   vehicle: 1492931016169247
}
```

## tesla:vehicle:data
```
{ 
   access_type: OWNER  
   api_version: 45  
   backseat_token: null  
   backseat_token_updated_at: null  
   calendar_enabled: true  
   color: null  
   display_name: MyCarsName  
   id: 12345678910111213  
   id_s: 12345678910111213  
   in_service: false  
   option_codes: AD15,MDL3,PBSB,RENA,BT37,ID3W,RF3G,S3PB,DRLH,DV2W,W39B,APF0,COUS,BC3B,CH07,PC30,FC3P,FG31,GLFR,HL31,HM31,IL31,LTPB,MR31,FM3B,RS3H,SA3P,STCP,SC04,SU3C,T3CA,TW00,TM00,UT3P,WR00,AU3P,APH3,AF00,ZCST,MI00,CDM0  
   state: online  
   tokens: [ 
     xxxxxxxxxxxxxxxx
     yyyyyyyyyyyyyyyy
   ]  
   user_id: 123456  
   vehicle_id: 0123456789  
   vin: 5YJ3F7EBXKF123456  
}
```

## "GraphQL Supercharger data"
## tesla:suc:locations
```
{
   activeOutages: [
   ]
   availableStalls: 2
   centroid: {
     latitude: 50.928282
     longitude: 1.811838
   }
   drivingDistanceMiles: null
   entryPoint: {
     latitude: 50.929973
     longitude: 1.813182
   }
   haversineDistanceMiles: 281.7208162123432
   id: 20e3945e-ae3f-409a-b23f-c74bd77d5d1f
   localizedSiteName: Tesla Supercharger Eurotunnel, France -  Flexiplus Lounge
   maxPowerKw: 125
   totalStalls: 2
}
```

## "Nearby SuperCharger Stats"
## tesla:suc:locations
```
{
   activeOutages: [
   ]
   availableStalls: 2
   centroid: {
     latitude: 50.928282
     longitude: 1.811838
   }
   drivingDistanceMiles: null
   entryPoint: {
     latitude: 50.929973
     longitude: 1.813182
   }
   haversineDistanceMiles: 281.7208162123432
   id: 20e3945e-ae3f-409a-b23f-c74bd77d5d1f
   localizedSiteName: Tesla Supercharger Eurotunnel, France -  Flexiplus Lounge
   maxPowerKw: 125
   totalStalls: 2
}
```

## tesla:vehicle:destinationcharger
```
{
   distance_miles: 9.874345
   location: {
     lat: 53.973773
     long: -1.492644
   }
   name: Rudding Park Hotel
   type: destination
}
```

## "Vehicle List"
## tesla:vehicle:list
```
{
   access_type: OWNER
   api_version: 45
   backseat_token: null
   backseat_token_updated_at: null
   calendar_enabled: true
   color: null
   display_name: MyCarsName
   id: 12345678910111213
   id_s: 12345678910111213
   in_service: false
   option_codes: AD15,MDL3,PBSB,RENA,BT37,ID3W,RF3G,S3PB,DRLH,DV2W,W39B,APF0,COUS,BC3B,CH07,PC30,FC3P,FG31,GLFR,HL31,HM31,IL31,LTPB,MR31,FM3B,RS3H,SA3P,STCP,SC04,SU3C,T3CA,TW00,TM00,UT3P,WR00,AU3P,APH3,AF00,ZCST,MI00,CDM0
   state: online
   tokens: [ [+]
   ]
   vehicle_id: 1234567890
   vin: 5YJ3F7EBXKF123456
}
```

## Screenshots
#### Overview
![Overview](https://user-images.githubusercontent.com/5527349/104831042-eb315580-587c-11eb-840f-eff44f7524dd.png)

# ToDo
* Props to extract specific metrics into metrics index
* Additional Journey plotting dashboard(s)
* Battery Health / Efficiency Dashboard  
