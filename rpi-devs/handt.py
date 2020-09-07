import Adafruit_DHT
import time
 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
 

rhum, temp = Adafruit_DHT.read(DHT_SENSOR, 4)
print(rhum, temp)
#print(rhum)
#print(temp)
#while True:
    #if rhum is not None and temp is not None:
        #print("Temp={0:1}C Humidity={1:1}%".format(temp, rhum))
#new_temp = float(format(temp))



    #else:
        #print("Sensor failure. Check wiring.");
#     time.sleep(3);