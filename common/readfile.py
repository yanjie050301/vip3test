#coding:utf-8
import xlrd
# data = xlrd.open_workbook(r'F:\test\code\vip3test\data.xls')
# tables = data.sheet_by_index(0)
# print(tables.nrows)
# print((tables.ncols))
# a = tables.cell(1,1).value
# print(a)
class Openexcel():
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = 'F:\\test\\code\\vip3test\\data.xls'
            self.sheet_id =0
        self.data = self.get_data()
    # 获取Excel列表
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheet_by_index(self.sheet_id)
        return tables
    # 获取表格中的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows
    # 获取表格的某个单元格的值
    def get_cell_value(self,row,col):
        value= self.data.cell(row,col)
        return value
if __name__ == '__main__':
    a = Openexcel()
    print(a.get_cell_value(1,3))









