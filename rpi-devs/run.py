import worksheet
import collector as c
import time
import equation as e

debug = False  #debugging
update = False #location update

print('debug: ', str(debug)) 

wk = worksheet.WorkSheet(debug = False)

data_constr = c.NewData(update=update, debug=debug)

eqn = e.FWICLASS(main)

deadlock = input('loop forever:[T]/F: ')
if deadlock == 'T' or deadlock == 'True':
    deadlock = True
else:
    deadlock = False
while True:
    try:
        data = data_constr.get()
        t = data[1]
        h = data[2]
        # TODO something = data[somthing]
        #eq = e.FWICLASS()
        #some_throw_back = eq.somemethod()
        #TODO pass new throw back(s) as list  to ``wk.post_batch`` 
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
