# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Source\timesheet\timesheet.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(480, 480)
        self.buttonBox = QtGui.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 600, 461, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 30, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.dateEdit = QtGui.QDateEdit(dialog)
        self.dateEdit.setGeometry(QtCore.QRect(90, 20, 91, 31))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.dateEdit_2 = QtGui.QDateEdit(dialog)
        self.dateEdit_2.setGeometry(QtCore.QRect(310, 20, 91, 31))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.importSOHOWH_Button = QtGui.QPushButton(dialog)
        self.importSOHOWH_Button.setGeometry(QtCore.QRect(10, 70, 71, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        font.setUnderline(True)
        self.importSOHOWH_Button.setFont(font)
        self.importSOHOWH_Button.setAutoFillBackground(True)
        self.importSOHOWH_Button.setFlat(False)
        self.importSOHOWH_Button.setObjectName(_fromUtf8("importSOHOWH_Button"))
        self.importHoliday_Button = QtGui.QPushButton(dialog)
        self.importHoliday_Button.setGeometry(QtCore.QRect(190, 70, 75, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setUnderline(True)
        self.importHoliday_Button.setFont(font)
        self.importHoliday_Button.setObjectName(_fromUtf8("importHoliday_Button"))
        self.calc_Button = QtGui.QPushButton(dialog)
        self.calc_Button.setGeometry(QtCore.QRect(10, 140, 75, 51))
        self.calc_Button.setObjectName(_fromUtf8("calc_Button"))
        self.textBrowser = QtGui.QTextBrowser(dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 200, 461, 271))
        self.textBrowser.setAcceptRichText(False)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.importOuting2_Button = QtGui.QPushButton(dialog)
        self.importOuting2_Button.setGeometry(QtCore.QRect(270, 70, 75, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setUnderline(True)
        self.importOuting2_Button.setFont(font)
        self.importOuting2_Button.setObjectName(_fromUtf8("importOuting2_Button"))
        self.importOuting_Button = QtGui.QPushButton(dialog)
        self.importOuting_Button.setGeometry(QtCore.QRect(350, 70, 75, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setUnderline(True)
        self.importOuting_Button.setFont(font)
        self.importOuting_Button.setObjectName(_fromUtf8("importOuting_Button"))
        self.importSHFAWH_Button = QtGui.QPushButton(dialog)
        self.importSHFAWH_Button.setGeometry(QtCore.QRect(80, 70, 71, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        font.setUnderline(True)
        self.importSHFAWH_Button.setFont(font)
        self.importSHFAWH_Button.setAutoFillBackground(True)
        self.importSHFAWH_Button.setFlat(False)
        self.importSHFAWH_Button.setObjectName(_fromUtf8("importSHFAWH_Button"))
        self.importOT_Button = QtGui.QPushButton(dialog)
        self.importOT_Button.setGeometry(QtCore.QRect(190, 110, 75, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setUnderline(True)
        self.importOT_Button.setFont(font)
        self.importOT_Button.setObjectName(_fromUtf8("importOT_Button"))

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "卡法考勤程序", None))
        self.label.setText(_translate("dialog", "开始时间", None))
        self.label_2.setText(_translate("dialog", "结束时间", None))
        self.dateEdit.setDisplayFormat(_translate("dialog", "yyyy-MM-dd", None))
        self.dateEdit_2.setDisplayFormat(_translate("dialog", "yyyy-MM-dd", None))
        self.importSOHOWH_Button.setText(_translate("dialog", "导入考勤\n"
"(SOHO)", None))
        self.importHoliday_Button.setText(_translate("dialog", "导入请假", None))
        self.calc_Button.setText(_translate("dialog", "开始统计", None))
        self.importOuting2_Button.setText(_translate("dialog", "导入出差", None))
        self.importOuting_Button.setText(_translate("dialog", "导入外勤", None))
        self.importSHFAWH_Button.setText(_translate("dialog", "导入考勤\n"
"（同普工厂）", None))
        self.importOT_Button.setText(_translate("dialog", "导入加班", None))

