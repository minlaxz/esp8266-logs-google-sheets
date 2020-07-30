from datetime import datetime, time
from keys import weatherapikey as key # weatherapi.com
from keys import loca  # location in lat,lon
import requests, json
now_time = datetime.now().time()
#import Adafruit_DHT
#keys lib is ignored.

class NewData:
    def __init__(self, debug=False):
        self.url = 'http://api.weatherapi.com/v1/current.json?key='+key+'&q='+loca
        self.debug = debug
        self.get_weather()

    def get_temp(self):
        #if self.debug: print('get_temp: getting h & t ... ')
        #return Adafruit_DHT.read_retry(Adafruit_DHT.DHT11 , 23)
        return 90.2, 26.8
    
    def get_weather(self):
        res = requests.get(url=self.url)
        self.weather = json.loads(res.text)['current']

    def is_raining(self):
        return 0

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
        new_data.append(0) if now_time >= time(18,00) or now_time <= time(6,00) else new_data.append(1) # D Done Day Time
        if self.debug: print('sensors: is_day append done.')
        new_data.append(self.is_raining()) # E Done Raining
        if self.debug: print('sensors: is_raining append done.')

        if self.debug: print('collecting weather data.')
        temp_c = self.weather['temp_c']
        humidity = self.weather['humidity']
        wind_kph = self.weather['wind_kph']
        wind_dir = self.weather['wind_dir']
        pressure_in = self.weather['pressure_in']
        cloud = self.weather['cloud']
        vis_km = self.weather['vis_km']
        uv = self.weather['uv']

        new_data.append(temp_c)    #F
        new_data.append(humidity)  #G
        new_data.append(wind_kph)  #H
        new_data.append(wind_dir)  #I
        new_data.append(vis_km)    #J
        new_data.append(cloud)     #K
        new_data.append(uv)        #L
        new_data.append('--Decision--')
        new_data.append('Bongo!') #N

        if self.debug: print('sensors: all done.')
        return new_data

