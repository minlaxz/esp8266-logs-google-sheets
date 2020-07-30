import utils
import sensors as s
wk = utils.WSheet(worksheet=utils.get_wsheet() , debug=False)
last_row = wk.get_last_row()
limiter = str(last_row+1)
wk.post_batch(limiter='A'+limiter+':F'+limiter, data_list=s.get_data_list())