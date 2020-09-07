import gspread
class WorkSheet:
    def __init__(self, worksheet, debug=False):
        print('main program started.')
        self.debug = debug
        self.get_wsheet()

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
        print(limiter)
        print(data_list)
        self.worksheet.update(limiter, [data_list]) if cloudUpdate else print('cloudUpdate bypassed.')
        if self.debug: print('data posted.')

    def get_wsheet(self):
        gc = gspread.service_account('./service-key.json')
        sh = gc.open_by_key('1NrWpVEM_BgzVnSMemE7ZGrNUdwRibCW8feSKzS5bRds')
        self.worksheet = sh.get_worksheet(0)
