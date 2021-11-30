from HCMKgon import *
import sys
import sys
import gspread
import pandas as pd

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
client = gspread.service_account('ok.json')

class Main(QtWidgets.QMainWindow,Ui_MainWindow):
    def  __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setupButton()


    def setupButton(self):

        #Cài đặt event click cho nút bấm M
        self.pushButton_4.clicked.connect(self.cokhong)
        self.pushButton_5.clicked.connect(self.conchoikhong)
        self.pushButton_6.clicked.connect(self.trangthaitk)
        #Cài đặt event click cho nút bấm K
        self.pushButton_21.clicked.connect(self.kiemtra)
        self.pushButton_22.clicked.connect(self.napdulieu)
        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Enter"), self)
        self.shortcut.activated.connect(self.kiemtra)
        self.setWindowIcon(QtGui.QIcon('logo_kiemkhach2.ico'))

    def cokhong(self):
        x=("Kiểm tra giúp {} tài khoản: {} *có không* {} *({})*".format("e" if self.comboBox_2.currentText() == "em" else "mình"\
            ,self.lineEdit.text(),"ạ" if self.comboBox_2.currentText() == "em" else "nhé",self.comboBox.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def conchoikhong(self):
        x=("Kiểm tra giúp {} tài khoản: {} *còn chơi* không {} *({})*".format("e" if self.comboBox_2.currentText() == "em" else "mình"\
            ,self.lineEdit.text(),"ạ" if self.comboBox_2.currentText() == "em" else "nhé",self.comboBox.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def trangthaitk(self):
        x=("Kiểm tra giúp {} *trang thái* tài khoản: {} {} *({})*".format("e" if self.comboBox_2.currentText() == "em" else "mình"\
            ,self.lineEdit.text(),"ạ" if self.comboBox_2.currentText() == "em" else "nhé",self.comboBox.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    

    def napdulieu(self): 
        self.all_ku = []
        self.all_tha = []
        values1 = client.open('1.C- KHÁCH').worksheet('KU (19-21)').get_all_values()
        values3 = client.open('1.H_KHÁCH').worksheet('KU (19-21)').get_all_values()
        values5 = client.open('H-C KHÁCH THÁNG').worksheet('C- KU  T12').get_all_values()
        values7 = client.open('H-C KHÁCH THÁNG').worksheet('H- KU T12').get_all_values()
        ku = [values1,values3,values5,values7]
        values2 = client.open('1.C- KHÁCH').worksheet('THA (20-21)').get_all_values()
        values4 = client.open('1.H_KHÁCH').worksheet('THA (20-21)').get_all_values()
        values6 = client.open('H-C KHÁCH THÁNG').worksheet('C-THA T12').get_all_values()
        values8 = client.open('H-C KHÁCH THÁNG').worksheet('H- THA T12').get_all_values()
        tha = [values2,values4,values6,values8]

        for kudata in ku :
           self.all_ku.extend(kudata)
        for thadata in tha :
           self.all_tha.extend(thadata)


        msgBox = QtWidgets.QMessageBox()

        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Đã nạp xong dữ liệu")
        msgBox.setWindowTitle("Thông báo")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def kiemtra(self):
        self.lineEdit_6.setText('')
        self.lineEdit_7.setText('')
        username = self.lineEdit.text().upper()
        a = False
        if username =='':
            return 
        for khach in self.all_ku:
            if username in khach:
                self.lineEdit_6.setText(' | '.join(khach))
                a = True
                break

        for khach in self.all_tha:
            if username in khach:
                self.lineEdit_7.setText(' | '.join(khach))
                a = True
                return

        if a == False:        
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText("KHÔNG CÓ NHÉ")
            msgBox.setWindowTitle("Xin chia buồn")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_() 



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec_())
        