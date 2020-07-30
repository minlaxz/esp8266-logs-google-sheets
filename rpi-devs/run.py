import utils
import collector as c
wk = utils.WorkSheet(worksheet=utils.get_wsheet() , debug=True)

row_limiter = str(wk.get_last_row()+1)

new_data = c.NewData(debug=True)

wk.post_batch(limiter='A'+row_limiter+':N'+row_limiter, data_list=new_data.get(), cloudUpdate=True)
