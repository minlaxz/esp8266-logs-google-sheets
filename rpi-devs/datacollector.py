from datetime import datetime
from keys import weatherapikey, location  # weatherapi.com
import requests, json, pylaxz
import Adafruit_DHT as ada
from gpiozero import InputDevice as in_device



class NewData:
    def __init__(self, update_location=False, debug=False):
        self.debug = debug

        self.rain = in_device(18).is_active
        self.location = location if not update_location else self.update_loca()
        self.url = 'http://api.weatherapi.com/v1/current.json?key='+weatherapikey+'&q='+self.location
        self.get_weather()

    def get_temp(self):
        if self.debug:
            pylaxz.printf('get_temp: getting h & t ... ', _int=1)
        return ada.read_retry(ada.DHT11, 4)

    def update_loca(self):
        lat = input('lat: ')
        lon = input('lon: ')
        return lat+','+lon

    def get_weather(self):
        res = requests.get(url=self.url)
        self.weather = json.loads(res.text)['current']

    def get(self):
        new_data = list()
        h, t = None, None

        new_data.append(str(datetime.now())) # 0
        if self.debug:
            pylaxz.printf('sensors: date ... done.')

        h, t = self.get_temp()
        new_data.append(t)  # 1
        new_data.append(h)  # 2

        if self.debug:
            if h and t is not None:
                pylaxz.printf('sensors: HT ... done.', _int=1) 
            else:
                pylaxz.printf('sensors: HT sensors error.', _int=1, _err=1)

        new_data.append(0) if self.rain else new_data.append(1)  # 3
        if self.debug:
            pylaxz.printf('sensors: is_raining ... done.', _int=1)

        new_data.append(self.weather['temp_c'])  # 4
        new_data.append(self.weather['humidity'])  # 5
        new_data.append(self.weather['wind_kph'])  # 6

        if self.debug:
            pylaxz.printf('sensors: weather data ... done', _int=1)

        # new_data.append('--Decision--')  # 7

        if self.debug:
            pylaxz.printf('sensors: all done.', _int=1)

        return new_data
