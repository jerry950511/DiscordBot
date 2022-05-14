from openpyxl import Workbook,load_workbook
from os.path import join



class Classes:
    def __init__(self):
        #初始化
        self.wb = load_workbook(join("classes.xlsx"))
        self.ws = self.wb.active
        