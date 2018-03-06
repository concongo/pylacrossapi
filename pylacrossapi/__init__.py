import urllib
import urllib2
import json
import sys


class lacrosse:
    __device = ''
    __metric = 0
    __timezone = 0


    def __init__(self, device, metric, timezone):
        self.__device = device
        self.__metric = metric
        self.__timezone = timezone
        self.__url_base =  'http://decent-destiny-704.appspot.com/laxservices/device_info.php'
        self.__timezones = {
            "10": 'America/Denver', "4": 'America/Phoenix', "2": 'America/Chicago', "3": 'America/New_York',
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
            "83": 'Europe/Warsaw', "61": 'Europe/Zurich', "101": 'IndiaStandardTime', "104": 'Pacific/Auckland'
        }


    def getObservation(self, n):
        headers = {
            'User-agent': 'Mozilla/4.0 (compatible; Lacrosse API Client; ' +
                          str(sys.platform) + '; ' + str(sys.version).replace('\n', '') + ')'
        }

        params = { 'deviceid' : self.__device,
                   'limit':n,
                   'metric':self.__metric,
                   'timezone':self.__timezone
                   }
        data = urllib.urlencode(params)

        if len(data) > 0:
            req = urllib2.Request(self.__url_base + '?' + data, None, headers)
        else:
            req = urllib2.Request(self.__url_base, None, headers)

        page = urllib2.urlopen(req).read()

        return json.loads(page)["device0"]["obs"]

        #retuns an array of n observation with this structure
        #linkquality, lowbattery, success, s_interval, ambient_temp, u_timestamp, \
        #humidity, utctime, device_type, timestamp, probe_temp, id, deviced_id

