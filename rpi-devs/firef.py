from datetime import datetime, time
from keys import weatherapikey as key # weatherapi.com
import requests, json, time
import Adafruit_DHT
from gpiozero import InputDevice as d
import math
import worksheet as utils
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import r2_score
 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
r = d(18).is_active

rhum, temp = Adafruit_DHT.read(DHT_SENSOR, 4)
url = 'http://api.weatherapi.com/v1/current.json?key='+key+'&q='+loca
res = requests.get(url)
weather = json.loads(res.text)['current']
wind =weather['wind_kph']
#print(r)
#print(type(r))



rainT=int(r==True)
rainF=int(r==False)
#print(rainT,rainF)

if True:
    prcp=rainT
else:
    prcp=rainF
    
#print(temp,rhum,wind,prcp)
#for ffmc

ffmc0=85.0
mo = (147.2*(101.0 - ffmc0))/(59.5 + ffmc0)
if (prcp > 0.5):
    rf = prcp - 0.5
if (mo<=150.0):
    mr=mo+42.5*rf*math.exp(-100.0*(251.0-mo))*(1-math.exp(-6.93/rf))
elif (mo>150.0):
    mr=mo+42.5*rf*math.exp(-100.0*(251.0-mo))*(1-math.exp(-6.93/rf))+(0.0015*(mo-150.0)**2)*math.sqrt(rf)
    ed = .942*(rhum**0.679) + (11.0*math.exp((rhum-100.0)/10.0))+0.18*(21.1-temp) \
                                 *(1.0 - 1.0/math.exp(.1150 * rhum))
ew = .618*(rhum**0.753) + (10.0*math.exp((rhum-100.0)/10.0))\
                                 + 0.18*(21.1-temp)*(1.0 - 1.0/math.exp(.115 * rhum))
kl = .424*(1.0-((100.0-rhum)/100.0)**1.7)+(.0694*math.sqrt(wind)) \
                                     *(1.0 - ((100.0 - rhum)/100.0)**8)
kw = kl * (.581 * math.exp(.0365 * temp))
m = ew - (ew - mo)/10.0**kw
ffmc=59.5*(250.0-m)/(147.2+m)
#print(ffmc)
#for DMC
dmc0 = 6.0
el= 8.0
if (prcp > 1.5):
    ro = (prcp*0.92)-1.27
elif (prcp<=1.5):
    pr=dmc0
    rk = 1.894*(temp+1.1) * (100.0-rhum) * (el*0.0001)
dmc=pr+rk
#for DC
dc0 = 15.0
fl = 2.2
pe = (0.36*(temp+2.8) + fl )/2
dc = dc0 + pe
#for ISI
mo = 147.2*(101.0-ffmc) / (59.5+ffmc)
ff = 19.115*math.exp(mo*-0.1386) * (1.0+(mo**5.31)/49300000.0)
isi = ff * math.exp(0.05039*wind)
#rainr= 0.5
wk = utils.WorkSheet(worksheet=utils.get_wsheet())




dataset = pd.read_csv(r'/home/pi/Desktop/forestfires.csv')
X = dataset.iloc[:, 0:12].values
y = dataset.iloc[:, 12].values
dataset


labelencoder_X_1 = LabelEncoder()
X[:, 2] = labelencoder_X_1.fit_transform(X[:, 2]) 
labelencoder_X_2 = LabelEncoder()
X[:, 3] = labelencoder_X_2.fit_transform(X[:, 3]) 
columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [2])],     remainder='passthrough')
X=np.array(columnTransformer.fit_transform(X),dtype=np.str)
X = X[:, 1:]
columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [13])],     remainder='passthrough')
X=np.array(columnTransformer.fit_transform(X),dtype=np.str)
X = X[:, 1:]

regr = RandomForestRegressor(max_depth=2, random_state=0, n_estimators=100)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)


#y_pred = model.predict(X_test)



#print('MSE =', mse(y_pred, y_test))
#print('MAE =', mae(y_pred, y_test))
#print('Predic =', r2_score(y_pred, y_test))



while  True:
    dd=str(datetime.now())
    data = dd,temp,rhum,wind,prcp,ffmc,dmc,dc,isi,mae(y_pred, y_test),r2_score(y_pred, y_test)
    print(data)
    if r2_score(y_pred, y_test)< 0:
        print('safe')
    else:
        print('alert')

    row_limiter = str(wk.get_last_row()+1)
    wk.post_batch(limiter='A'+row_limiter+':N'+row_limiter, data_list=data , cloudUpdate=True)
    time.sleep(10)
