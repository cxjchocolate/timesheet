# coding=gbk
'''
Created on 2016年2月5日

@author: 大雄
'''
from datetime import datetime
import logging
import os
import sys
import time

from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from peewee import SqliteDatabase

from command import createCommand
import timesheet
from utils import getHome
import utils


class TimeSheetDialog(QDialog,timesheet.Ui_dialog):  
    def __init__(self,parent=None):  
        super(TimeSheetDialog,self).__init__(parent)  
        self.setupUi(self)
        self.dateEdit.setDate(datetime.now())
        self.dateEdit_2.setDate(datetime.now())
        self.connect(self.importSOHOWH_Button,SIGNAL("clicked()"),self.importSOHOWorkHour)
        self.connect(self.importSHFAWH_Button,SIGNAL("clicked()"),self.importSHFAWorkHour)
        self.connect(self.importHoliday_Button,SIGNAL("clicked()"),self.importHoliday)
        self.connect(self.importOuting_Button,SIGNAL("clicked()"),self.importOuting)
        self.connect(self.importOuting2_Button,SIGNAL("clicked()"),self.importOuting2)
        self.connect(self.importOT_Button,SIGNAL("clicked()"),self.importOverTime)
        self.connect(self.calc_Button,SIGNAL("clicked()"),self.calc)
        
        if not os.path.isdir(getHome() + "/db/"):
            os.mkdir(getHome() + "/db/")
            
        self.dbname = getHome() + "/db/" + str(time.time()) + ".db"

    def openFile(self, title):
        s=QFileDialog.getOpenFileName(self,title,getHome(),"Excel工作簿(*.xlsx)")    
        return s
     
    def importSOHOWorkHour(self):
        file = self.openFile("导入考勤(SOHO)")
        if file:
            try:
                out = importExcel2SQLite3(file, self.dbname, "t_checking_in_soho")
                self.appendLog(out.decode())
            except Exception as e:
                self.appendLog(str(e))

    def importSHFAWorkHour(self):
        file = self.openFile("导入考勤（同普工厂）")
        if file:
            try:
                out = importExcel2SQLite3(file, self.dbname, "t_checking_in_tongpu")
                self.appendLog(out.decode())
            except Exception as e:
                self.appendLog(str(e))
                
    def importHoliday(self):
        file = self.openFile("导入请假")
        if file:
            try:
                out = importExcel2SQLite3(file, self.dbname, "t_user_holiday")
                self.appendLog(out.decode())
            except Exception as e:
                self.appendLog(str(e))

    def importOverTime(self):
        file = self.openFile("导入加班")
        if file:
            try:
                out = importExcel2SQLite3(file, self.dbname, "t_overtime")
                self.appendLog(out.decode())
            except Exception as e:
                self.appendLog(str(e))
    
    def importOuting(self):
        file = self.openFile("导入外出")
        if file:
            try: 
                out = importExcel2SQLite3(file, self.dbname, "t_outing")
                self.appendLog(out.decode())
            except Exception as e:
                self.appendLog(str(e))

    def importOuting2(self):
        file = self.openFile("导入出差")
        if file:
            try:
                out = importExcel2SQLite3(file, self.dbname, "t_outing2")
                self.appendLog(out.decode())
            except Exception as e:
                self.appendLog(str(e))
           
    def appendLog(self, content):
        self.textBrowser.append(content)
        
    def calc(self):
        if self.check():
            try:
                self.appendLog("step 1: 创建基础数据")
                initialDates(self.dbname, self.dateEdit.date().toPyDate(), self.dateEdit_2.date().toPyDate())
                self.appendLog("OK")
 
#                 self.appendLog("step 2: 合并指纹考勤")
#                 executeSQL(self.dbname, getHome() + "/sql/2-合并soho-tongpu.sql")
#                 self.appendLog("OK")
#  
#                 self.appendLog("step 3: groupby上下班时间")
#                 executeSQL(self.dbname, getHome() + "/sql/3-groupby上下班时间.sql")
#                 self.appendLog("OK")
#  
#                 self.appendLog("step 4: 制作考勤表")
#                 executeSQL(self.dbname, getHome() + "/sql/4-制作考勤表.sql")
#                 self.appendLog("OK")
#  
#                 self.appendLog("step 5: 杂项处理")
#                 executeSQL(self.dbname, getHome() + "/sql/5-杂项处理.sql")
#                 self.appendLog("OK")

                root = getHome() + "/sql/"
                files = os.listdir(root)
                files.sort()
                for i in files:
                    if os.path.isfile(os.path.join(root,i)):
                        self.appendLog("Execute SQL: " + i)
                        executeSQL(self.dbname, os.path.join(root,i))
                        self.appendLog("OK")
                
                self.appendLog("step 6: 导出考勤表(考勤结果.xlsx)")
                #导出考勤excel表
                exportSQLite32Excel(self.dbname, "t_checking_in_all", "考勤结果.xlsx")
                self.appendLog("OK")
                 
            except Exception as e:
                self.appendLog("发生异常，异常消息:" + str(e))
        else:
            self.appendLog("异常退出!")
        
    def check(self):
        table_flag = checkTables(self.dbname, ['t_checking_in_soho', 't_checking_in_tongpu','t_overtime','t_user_holiday','t_outing','t_outing2'])
        self.appendLog("checking imported data: " + str(table_flag))
        
        startDate = self.dateEdit.date()
        endDate = self.dateEdit_2.date()
        if (startDate >= endDate):
            date_flag = False
            self.appendLog("checking date: Error, 开始日期大于等于结束日期")
        else:
            date_flag = True
            self.appendLog("checking date: OK")
            
        return table_flag and date_flag        

def checkTables(dbname, tables):
    db = SqliteDatabase(dbname)
    if db:
        param = "','".join(tables)
        param = "'" + param + "'"
        sql = "SELECT count(*) FROM sqlite_master WHERE type='table' and tbl_name in ({0})".format(param,)    
        result = db.execute_sql(sql)
        for e in result:
            count = e[0]
        if count != len(tables):
            return False
        else:
            return True
    else:
        return False
    
def initialDates(dbname, startDate, endDate):
    try:
        db = SqliteDatabase(dbname)
        days = (endDate - startDate).days
        db.execute_sql("drop table if exists t_date_temp")
        db.execute_sql("create table t_date_temp (mydate text, week text, weekday text)")
        db.execute_sql("insert into t_date_temp values( ?, ?, ? )", (startDate.strftime('%Y-%m-%d'),startDate.isoweekday(),''))
        for i in range(days):
            db.execute_sql("insert into t_date_temp  select date(max(mydate), '+1 day'),  strftime('%w', date(max(mydate), '+1 day')), '' from t_date_temp")
    except Exception as e:
        logging.debug(e)
    finally:
        db.close()
        
def importExcel2SQLite3(file, dbname, tablename):
    if not os.path.isdir(os.path.dirname(file) + "/temp/"):
        os.mkdir(os.path.dirname(file) + "/temp/")
        
    csvfile = os.path.dirname(file) + "/temp/" + os.path.basename(file).split(".")[0] + ".csv"
    utils.Excel2CSV(file, csvfile)
    sql = "\".mode csv\" \".import {0} {1}\""
    return createCommand(dbname, sql.format(csvfile, tablename), type="SQLite3_Win32").execute()

def executeSQL(dbname, file):
    return createCommand(dbname, file, type="SQLite3_Win32").execute()

def exportSQLite32Excel(dbname, tblname, file):
    try:
        db = SqliteDatabase(dbname)
        sql =  "select * from {0}".format(tblname,)
        result = db.execute_sql(sql)
        utils.writeExcel(result, file, 6, 2)
        utils.writeCreateTime(file, 2, 4)
    except Exception as e:
        logging.debug(e)
    finally:
        db.close() 
   
if __name__ == "__main__":
    logfile = getHome() + "/timesheet.log"
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(filename)s[line:%(lineno)d] %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=logfile)
    app=QApplication(sys.argv)
    dialog=TimeSheetDialog()
    dialog.show()
    app.exec_()
