import gspread
class WorkSheet:
    def __init__(self, debug=False):
        self.debug = debug
        self.get_wsheet()

    def get_last_row(self):
        return len(self.worksheet.get_all_values()) # 2 including header.
        
        # values_list = self.worksheet.row_values(total_lists)
        #log.this(self.worksheet.cell(1,12).value)
    
    def post_data(self, data):
        log.this(data)

    def post_batch(self, limiter, data_list, cloudUpdate=True):
        log.this(limiter)
        log.this(data_list)
        self.worksheet.update(limiter, [data_list]) if cloudUpdate else log.this('cloudUpdate bypassed.')
        if self.debug: log.this('data posted.')

    def get_wsheet(self):
        gc = gspread.service_account('./service-key.json')
        sh = gc.open_by_key('1NrWpVEM_BgzVnSMemE7ZGrNUdwRibCW8feSKzS5bRds')
        self.worksheet = sh.get_worksheet(0)
