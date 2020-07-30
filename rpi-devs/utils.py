import gspread
class WorkSheet:
    def __init__(self, worksheet, debug=False):
        print('main program started.')
        self.debug = debug
        self.worksheet = worksheet
    
    def get_last_row(self):
        if self.debug: print('get_data function')
        return len(self.worksheet.get_all_values()) # 2 including header.
        # values_list = self.worksheet.row_values(total_lists)
        #print(self.worksheet.cell(1,12).value)
    
    def post_data(self, data):
        if self.debug: print('post_data function')
        print(data)

    def post_batch(self, limiter, data_list, cloudUpdate=True):
        if self.debug: print('post batch function')
        #if self.debug: 
        print(limiter)
        print(data_list)
        self.worksheet.update(limiter, [data_list]) if cloudUpdate else print('cloudUpdate bypassed.')

def get_wsheet():
    gc = gspread.service_account('./decent-bird-service-key.json')
    sh = gc.open_by_key('1gpKJUcVOu1Bc4qD1ITlBPY2K8sTd4G4mv0M60f9XyvY')
    return sh.get_worksheet(0)