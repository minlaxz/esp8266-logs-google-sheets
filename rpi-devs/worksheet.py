import gspread
import pylaxz

class WorkSheet:
    def __init__(self, debug=False):
        self.debug = debug
        _gc = gspread.service_account('./service-key.json')
        sh = _gc.open_by_key('1NrWpVEM_BgzVnSMemE7ZGrNUdwRibCW8feSKzS5bRds')
        self.worksheet = sh.get_worksheet(0)

    def get_last_row(self):
        return len(self.worksheet.get_all_values()) # 2 including header.
        
        # values_list = self.worksheet.row_values(total_lists)
        #log.this(self.worksheet.cell(1,12).value)
    
    @staticmethod
    def show(data):
        for i in data:
            pylaxz.printf(i, _int=1)

    def post_batch(self, limiter, data_list, cloudUpdate=True):
        if self.debug: pylaxz.printf(limiter, _int=1)
        if self.debug: pylaxz.printf(data_list, _int=1)
        if cloudUpdate: self.worksheet.update(limiter, [data_list])
        if self.debug: pylaxz.printf('data is processed.', _int=1)

