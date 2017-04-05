# -*- coding: utf-8 -*-
import xlrd  
  
class ExcelUtil(object):  
  
    def __init__(self, excelPath, sheetName):  
        self.data = xlrd.open_workbook(excelPath)  
        self.table = self.data.sheet_by_name(sheetName)  
          
        #获取标题 
        self.row = self.table.row_values(0)  
          
        #获取行数  
        self.rowNum = self.table.nrows  
          
        #获取列数 
        self.colNum = self.table.ncols  
          
        #当前列
        self.curRowNo = 1  
          
    def next(self):  
        r = []  
        while self.hasNext():  
            s = {}  
            col = self.table.row_values(self.curRowNo)  
            i = self.colNum  
            for x in range(i):  
                s[self.row[x]] = col[x]  
            r.append(s)  
            self.curRowNo += 1  
        return r         
      
    def hasNext(self):  
        if self.rowNum == 0 or self.rowNum <= self.curRowNo :  
            return False  
        else:  
            return True 