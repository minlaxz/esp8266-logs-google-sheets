from datetime import datetime, time
from keys import weatherapikey as key # weatherapi.com
from keys import loca
import requests, json
now_time = datetime.now().time()
import Adafruit_DHT
from gpiozero import InputDevice as d

#keys lib is ignored.

class NewData:
    def __init__(self, update=False, debug=False):
        self.debug = debug
        self.rain = d(18).is_active
        self.loca = loca if not update else self.update_loca()
        self.url = 'http://api.weatherapi.com/v1/current.json?key='+key+'&q='+self.loca
        self.get_weather()

    def get_temp(self):
        if self.debug: print('get_temp: getting h & t ... ')
        return Adafruit_DHT.read_retry(Adafruit_DHT.DHT11 , 14)

    def update_loca(self):
        lat = input('lat: ')
        lon = input('lon: ')
        return lat+','+lon

    def get_weather(self):
        res = requests.get(url=self.url)
        self.weather = json.loads(res.text)['current']

    def get(self):
        h, t= None, None

        if self.debug: print('sensors.get function')
        new_data = list()
        if self.debug: print('sensors: getting sensor data.')
        new_data.append(str(datetime.now())) # A Done DATE
        if self.debug: print('sensors: date append done.')
        h, t = self.get_temp()
        if self.debug: print('sensors: getting h & t ... done.') if h and t is not None else print('sensors: sensor error.')
        new_data.append(t) # B Done TEMP
        new_data.append(h) # C Done HUMIDITY
        if self.debug: print('sensors: h & t append done.') if not h is None else print ('sensor error.')
        # new_data.append(0) if now_time >= time(18,00) or now_time <= time(6,00) else new_data.append(1) # D Done Day Time
        # if self.debug: print('sensors: is_day append done.')
        new_data.append(0) if self.rain else new_data.append(1) # D Done Raining
        if self.debug: print('sensors: is_raining append done.')

        if self.debug: print('collecting weather data.')
        temp_c = self.weather['temp_c']
        humidity = self.weather['humidity']
        wind_kph = self.weather['wind_kph']
        # wind_dir = self.weather['wind_dir']
        # pressure_in = self.weather['pressure_in']
        # cloud = self.weather['cloud']
        # vis_km = self.weather['vis_km']
        # uv = self.weather['uv']

        new_data.append(temp_c)    #E
        new_data.append(humidity)  #F
        new_data.append(wind_kph)  #G
        # new_data.append(wind_dir) 
        # new_data.append(vis_km)   
        # new_data.append(cloud)    
        # new_data.append(uv)       
        new_data.append('--Decision--') #H
        # new_data.append('Bongo!') 

        if self.debug: print('sensors: all done.')
        return new_data

