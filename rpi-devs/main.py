"""
src/-> https://github.com/minlaxz/logs-to-sheets
edited/-> ~/.bashrc 'to auto activate python enviroment named (g)'
"""


from worksheet import WorkSheet as green_apple
import anydata as rake
import time

def main():
    while(True):
        try:
            """you can extract any data from here
            `data`  variable is list type.
            according to anydata.py 
            very first element of `data` will be datetime.now()
            # FOR EXAMPLE
            date_time = data [0]
            temperature = date [1]
            humidity = data [2]
            is_raining = data [3]
            temperature_from_api = data [4]
            hu....._api = data [5]
            wind_kph = data [6]
            """

            data = data_stack.get() # getting data from prviously created object in __main__ 

            row_limiter = str(wk.get_last_row()+1)
            wk.post_batch(limiter='A'+row_limiter+':N'+row_limiter, data_list=data , cloudUpdate=True)
            time.sleep(3)
            if not deadlock: break
        except KeyboardInterrupt:
            print('user stopped')
            break
        except Exception as e:
            print(e)
            break


if __name__ == "__main__":
    wth_is_goingon = False  #debugging
    location_update = False #location update

    """ WorkSheet Object. """
    wk = green_apple(debug = False) 

    """ creating data collector Object """
    data_stack = rake.NewData(update=location_update, debug=wth_is_goingon)

    choice = input('loop forever:[T]/F: ')
    deadlock = True if choice == 'T' else False
    main()