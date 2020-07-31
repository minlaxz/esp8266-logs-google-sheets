import utils
import collector as c
import time

debug = False
update = False

print('debug: ', str(debug)) 

wk = utils.WorkSheet(worksheet=utils.get_wsheet() , debug=debug)

new_data = c.NewData(update=update, debug=debug)

deadlock = input('loop forever:[T]/F: ')
if deadlock == 'T' or deadlock == 'True':
    deadlock = True
else:
    deadlock = False
while True:
    try:
        row_limiter = str(wk.get_last_row()+1)
        wk.post_batch(limiter='A'+row_limiter+':N'+row_limiter, data_list=new_data.get(), cloudUpdate=True)
        time.sleep(10)
        if not deadlock: break
    except KeyboardInterrupt:
        print('user stopped')
        break
    except Exception as e:
        print(e)
        break
