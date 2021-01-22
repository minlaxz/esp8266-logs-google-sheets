"""
src/-> https://github.com/minlaxz/logs-to-sheets
edited/-> ~/.bashrc 'to auto activate python enviroment named (g)'
"""

from worksheet import WorkSheet
import datacollector as dc
import time
import pylaxz


def main():
    """you can extract any data from here
    `data`  variable is list type.
    according to anydata.py
    very first element of `data` will be datetime.now()
    ### FOR EXAMPLE
    date_time = data [0]
    temperature = date [1]
    humidity = data [2]
    is_raining = data [3]
    temperature_from_api = data [4]
    hu....._api = data [5]
    wind_kph = data [6]
    """
    while(True):
        try:
            data = data_obj.get()  # getting sensor data

            row_limiter = str(ws.get_last_row()+1)
            if cloudUpdate: 
                ws.post_batch(limiter='A'+row_limiter+':N' + row_limiter, data_list=data, cloudUpdate=cloudUpdate)
            else:
                WorkSheet.show(['update bypassed', row_limiter, data])
            time.sleep(3)
            if not deadlock:
                break
        except KeyboardInterrupt:
            pylaxz.printf('user stopped', _int=1)
            break
        except Exception as e:
            print(e)
            break


if __name__ == "__main__":
    debug = False  # debugging
    u_l = False  # location update
    cloudUpdate = True
    # Create WorkSheet Object.
    ws = WorkSheet(debug=debug)

    # creat data collector Object
    data_obj = dc.NewData(update_location=u_l, debug=debug)

    deadlock = True if input('loop forever:[T]/F: ') in ('T','t') else False
    main()
