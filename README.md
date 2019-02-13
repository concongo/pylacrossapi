# LA CROSSE MOBILE TX60U-IT API Wrapper

An easy way to monitor your LA CROSSE MOBILE Wireless Temperature and Humidity Sensor

Compatible with Python 3

## Install

`python setup.py install`

## Usage

### Create Device

`from pylacrossapi import lacrosse`

`<device> = lacrosse(<deviceid>,<Temp Unit -- (0) American (1) Metric -->,<timezone>)`

### Time Zone codes
`   "10": 'America/Denver', "4": 'America/Phoenix', "2": 'America/Chicago', "3": 'America/New_York',
    "8": 'America/Los_Angeles', "5": 'America/Anchorage', "6": 'Pacific/Honolulu', "7": 'America/Halifax',
    "9": 'America/Montreal', "1": 'America/Boise', "65": 'America/Adak', "55": 'America/Argentina/Buenos_Aires',
    "15": 'America/Aruba', "88": 'America/Atikokan', "26": 'America/Bogota', "37": 'America/Caracas',
    "69": 'America/Cayman', "81": 'America/Chihuahua', "70": 'America/Costa_Rica', "79": 'America/Creston',
    "29": 'America/Danmarkshavn', "36": 'America/Dawson', "27": 'America/Dawson_Creek', "100": 'America/Detroit',
    "16": 'America/Edmonton', "87": 'America/El_Salvador', "92": 'America/Fortaleza', "66": 'America/Glace_Bay',
    "82": 'America/Grenada', "38": 'America/Guayaquil', "12": 'America/Indiana/Indianapolis',
    "86": 'America/Indiana/Knox', "51": 'America/Indiana/Tell_City', "59": 'America/Indiana/Vincennes',
    "44": 'America/Indiana/Winamac', "97": 'America/Iqaluit', "30": 'America/Juneau',
    "39": 'America/Kentucky/Louisville',
    "32": 'America/Kentucky/Monticello', "42": 'America/La_Paz', "71": 'America/Lima', "74": 'America/Managua',
    "45": 'America/Matamoros', "47": 'America/Menominee', "53": 'America/Metlakatla', "95": 'America/Mexico_City',
    "22": 'America/Moncton', "94": 'America/Monterrey', "96": 'America/Noronha',
    "78": 'America/North_Dakota/Beulah',
    "34": 'America/North_Dakota/Center', "54": 'America/North_Dakota/New_Salem', "63": 'America/Port_of_Spain',
    "62": 'America/Puerto_Rico', "91": 'America/Rainy_River', "23": 'America/Regina', "19": 'America/Resolute',
    "20": 'America/Santiago', "52": 'America/Santo_Domingo', "25": 'America/Sao_Paulo',
    "41": 'America/Scoresbysund',
    "67": 'America/Shiprock', "72": 'America/Sitka', "46": 'America/St_Johns', "40": 'America/St_Kitts',
    "68": 'America/St_Thomas', "48": 'America/Swift_Current', "35": 'America/Thunder_Bay', "13": 'America/Tijuana',
    "17": 'America/Toronto', "85": 'America/Tortola', "18": 'America/Vancouver', "84": 'America/Whitehorse',
    "33": 'America/Winnipeg', "11": 'America/Yakutat', "50": 'America/Yellowknife', "58": 'Asia/Bahrain',
    "24": 'Asia/Dubai', "31": 'Asia/Hong_Kong', "89": 'Asia/Jerusalem', "57": 'Asia/Qatar',
    "43": 'Asia/Seoul', "80": 'Asia/Singapore', "77": 'Asia/Tokyo', "103": 'Asia/Vietnam',
    "98": 'Australia/Adelaide', "60": 'Australia/Brisbane', "49": 'Australia/Melbourne',
    "14": 'Australia/Perth', "76": 'Australia/Sydney', "102": 'Canada/Newfoundland', "93": 'Europe/Athens',
    "28": 'Europe/Berlin', "73": 'Europe/Brussels', "64": 'Europe/London', "99": 'Europe/London',
    "75": 'Europe/Moscow', "90": 'Europe/Oslo', "21": 'Europe/Rome', "56": 'Europe/Vatican',
    "83": 'Europe/Warsaw', "61": 'Europe/Zurich', "101": 'IndiaStandardTime', "104": 'Pacific/Auckland'`

### Example

`device_id = 02839203`

`unit_measure = 1`

`time_zone = 37`

`device1 = lacrosse(device_id,unit_measure,time_zone)`

### Get Observations

`device1.getObservation(n)`

Where n is the number of observations from the most recent one

## Returned Dictionary

The API returns an array of dict where each row is a measure and the dict has the following variables:

- `linkquality`: It's the RF signal strength of the device to the hub
- `lowbattery`: 0 or 1. It's a signal
- `ambient_temp`: it is the temperature measure by the device in the unit specified
- `humidity`: Percentage of the relative humidity
- `utctime`: Time in UTC
- `device_type`: returns the model
- `timestamp`: returns the time of the observation on the specified timezone
- `probe_temp`: if a probe is connected, returns the temperature measured

### Example of Usage

    from pylacrossapi import lacrosse

    device_id = 02839203
    unit_measure = 1
    time_zone = 37
    device1 = lacrosse(device_id,unit_measure,time_zone)

    obs=device1.getObservation(3)
    #Returns the last three observation

    print obs[1]["ambient_temp"]
    #Prints the second observation Temperature`


