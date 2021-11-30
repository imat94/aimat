from HCMK import *
import sys
import gspread
import requests
import pandas as pd

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
ok = requests.get('https://raw.githubusercontent.com/imat94/aimat/main/ok.json').json()
client = gspread.service_account_from_dict(ok)

class Main(QtWidgets.QMainWindow,Ui_MainWindow):
    def  __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setupButton()


    def setupButton(self):

        #Cài đặt event click cho nút bấm M
        self.pushButton_42.clicked.connect(self.dangkychua)
        self.pushButton_41.clicked.connect(self.napchua)
        self.pushButton_35.clicked.connect(self.tainapchua)
        self.pushButton_36.clicked.connect(self.cokhong)
        self.pushButton_46.clicked.connect(self.cokhong2)
        self.pushButton_39.clicked.connect(self.conchoikhong)
        self.pushButton_47.clicked.connect(self.conchoikhong2)
        self.pushButton_34.clicked.connect(self.trangthaitk)
        self.pushButton_48.clicked.connect(self.trangthaitk2)
        self.pushButton_37.clicked.connect(self.chuyenlinkchua)
        self.pushButton_38.clicked.connect(self.tainap90chua)
        self.pushButton_33.clicked.connect(self.clinkbietdanh)        
        self.pushButton_40.clicked.connect(self.monapmail)
        #Cài đặt event click cho nút bấm K
        self.pushButton_29.clicked.connect(self.dangky)
        self.pushButton_32.clicked.connect(self.taiappku)
        self.pushButton_24.clicked.connect(self.taiapptha)
        self.pushButton_28.clicked.connect(self.laylaitk)
        self.pushButton_26.clicked.connect(self.monapku)
        self.pushButton_31.clicked.connect(self.monaptha)
        self.pushButton_25.clicked.connect(self.nhandiem)
        self.pushButton_27.clicked.connect(self.naptien)
        self.pushButton_30.clicked.connect(self.tainap)
        self.pushButton_23.clicked.connect(self.ruttien)


        self.pushButton_43.clicked.connect(lambda: self.kiemtra(self.lineEdit_10))
        self.pushButton_49.clicked.connect(lambda: self.kiemtra(self.lineEdit_17))
        self.pushButton_44.clicked.connect(self.napdulieu)
        self.pushButton_45.clicked.connect(self.napdulieu)

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Enter"), self)



        self.setWindowIcon(QtGui.QIcon('logo_kiemkhach1.ico'))



        self.pushButton_50.clicked.connect(self.thugon)

        self.pushButton_51.clicked.connect(self.moRong)


    def thugon(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
        height = self.groupBox_4.height()
        self.setFixedHeight(height)
        self.shortcut.activated.connect(lambda: self.kiemtra(self.lineEdit_17))

    def moRong(self):
        self.stackedWidget.setCurrentWidget(self.page)
        self.setFixedHeight(189)
        self.shortcut.activated.connect(lambda: self.kiemtra(self.lineEdit_10))





    def dangkychua(self):
        x=("Kiểm tra giúp {} tài khoản: {} *đăng ký* thành công chưa {} *({})*".format("e" if self.comboBox_10.currentText() == "em" else "mình"\
            ,self.lineEdit_10.text(),"ạ" if self.comboBox_10.currentText() == "em" else "nhé",self.comboBox_9.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)

    def napchua(self):
        x=("Kiểm tra giúp {} tài khoản: {} *nạp chơi* thành công chưa {} *({})*".format("e" if self.comboBox_10.currentText() == "em" else "mình"\
            ,self.lineEdit_10.text(),"ạ" if self.comboBox_10.currentText() == "em" else "nhé",self.comboBox_9.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def tainapchua(self):
        x=("Kiểm tra giúp {} tài khoản: {} *tái nạp chưa* {} *({})*".format("e" if self.comboBox_10.currentText() == "em" else "mình"\
            ,self.lineEdit_10.text(),"ạ" if self.comboBox_10.currentText() == "em" else "nhé",self.comboBox_9.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)

    def cokhong(self):
        x=("Kiểm tra giúp {} tài khoản: {} *có không* {} *({})*".format("e" if self.comboBox_10.currentText() == "em" else "mình"\
            ,self.lineEdit_10.text(),"ạ" if self.comboBox_10.currentText() == "em" else "nhé",self.comboBox_9.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def cokhong2(self):
        x=("Kiểm tra giúp {} tài khoản: {} *có không* {} *({})*".format("e" if self.comboBox_12.currentText() == "em" else "mình"\
            ,self.lineEdit_17.text(),"ạ" if self.comboBox_12.currentText() == "em" else "nhé",self.comboBox_11.currentText()))
        self.textBrowser_2.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)



    def conchoikhong(self):
        x=("Kiểm tra giúp {} tài khoản: {} *còn chơi* không {} *({})*".format("e" if self.comboBox_10.currentText() == "em" else "mình"\
            ,self.lineEdit_10.text(),"ạ" if self.comboBox_10.currentText() == "em" else "nhé",self.comboBox_9.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def conchoikhong2(self):
        x=("Kiểm tra giúp {} tài khoản: {} *còn chơi* không {} *({})*".format("e" if self.comboBox_12.currentText() == "em" else "mình"\
            ,self.lineEdit_17.text(),"ạ" if self.comboBox_12.currentText() == "em" else "nhé",self.comboBox_11.currentText()))
        self.textBrowser_2.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)

    def trangthaitk(self):
        x=("Kiểm tra giúp {} *trang thái* tài khoản: {} {} *({})*".format("e" if self.comboBox_10.currentText() == "em" else "mình"\
            ,self.lineEdit_10.text(),"ạ" if self.comboBox_10.currentText() == "em" else "nhé",self.comboBox_9.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def trangthaitk2(self):
        x=("Kiểm tra giúp {} *trang thái* tài khoản: {} {} *({})*".format("e" if self.comboBox_12.currentText() == "em" else "mình"\
            ,self.lineEdit_17.text(),"ạ" if self.comboBox_12.currentText() == "em" else "nhé",self.comboBox_11.currentText()))
        self.textBrowser_2.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)

    def chuyenlinkchua(self):
        x=("Kiểm tra giúp {} tài khoản: {} *chuyển về* thành công chưa {} *({})*".format("e" if self.comboBox_10.currentText() == "em" else "mình"\
            ,self.lineEdit_10.text(),"ạ" if self.comboBox_10.currentText() == "em" else "nhé",self.comboBox_9.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def tainap90chua(self):
        x=("Kiểm tra giúp {} tài khoản: {} *nạp lại sau 90 ngày* thành công chưa {} *({})*".format("e" if self.comboBox_10.currentText() == "em" else "mình"\
            ,self.lineEdit_10.text(),"ạ" if self.comboBox_10.currentText() == "em" else "nhé",self.comboBox_9.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def clinkbietdanh(self):
        x=("Tên tài khoản: {}\nBiệt danh: {}\nVui lòng hỗ trợ chuyển về {} giúp mình nhé!".format(self.lineEdit_10.text(),self.lineEdit_9.text(),self.comboBox_9.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def monapmail(self):
        x=("Mail KU: openbet999@gmail.com\nTk KU: {}\nMail khách: {}\nKhách cần hỗ trợ vấn đề mở nạp. Vui lòng kiểm và xử lý giúp mình. Xin cảm ơn!".format(self.lineEdit_10.text(),self.lineEdit_12.text()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    #Code nút bấm K team
    def dangky(self):
        x=("{} {} hướng dẫn *đăng ký* giúp {} nhé. *({})*".format("Zl" if self.comboBox_7.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_7.currentText() == "Facebook" else "Tl",self.lineEdit_8.text(),self.comboBox_8.currentText(),self.comboBox_6.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def taiappku(self):
        x=("{} {} hướng dẫn *tải app KU* giúp {} nhé.".format("Zl" if self.comboBox_7.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_7.currentText() == "Facebook" else "Tl",self.lineEdit_8.text(),self.comboBox_8.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x) 
    def taiapptha(self):
        x=("{} {} hướng dẫn *tải app THA* giúp {} nhé.".format("Zl" if self.comboBox_7.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_7.currentText() == "Facebook" else "Tl",self.lineEdit_8.text(),self.comboBox_8.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x) 
    def laylaitk(self):
        x=("{} {} hướng dẫn *lấy lại mật khẩu* giúp {} nhé.".format("Zl" if self.comboBox_7.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_7.currentText() == "Facebook" else "Tl",self.lineEdit_8.text(),self.comboBox_8.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x) 
    def monapku(self):
        x=("{} {} hướng dẫn *mở nạp KU* giúp {} nhé.".format("Zl" if self.comboBox_7.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_7.currentText() == "Facebook" else "Tl",self.lineEdit_8.text(),self.comboBox_8.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)  
    def monaptha(self):
        x=("{} {} hướng dẫn *mở nạp THA* giúp {} nhé.".format("Zl" if self.comboBox_7.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_7.currentText() == "Facebook" else "Tl",self.lineEdit_8.text(),self.comboBox_8.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)  
    def nhandiem(self):
        x=("{} {} hướng dẫn *nhận điểm* giúp {} nhé.".format("Zl" if self.comboBox_7.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_7.currentText() == "Facebook" else "Tl",self.lineEdit_8.text(),self.comboBox_8.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def naptien(self):
        x=("{} {} hướng dẫn *nạp tiền* giúp {} nhé.".format("Zl" if self.comboBox_7.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_7.currentText() == "Facebook" else "Tl",self.lineEdit_8.text(),self.comboBox_8.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)  
    def tainap(self):
        x=("{} {} hướng dẫn *tái nạp* giúp {} nhé.".format("Zl" if self.comboBox_7.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_7.currentText() == "Facebook" else "Tl",self.lineEdit_8.text(),self.comboBox_8.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def ruttien(self):
        x=("{} {} hướng dẫn *rút tiền* giúp {} nhé.".format("Zl" if self.comboBox_7.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_7.currentText() == "Facebook" else "Tl",self.lineEdit_8.text(),self.comboBox_8.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)  

    def napdulieu(self): 
        self.all_ku = []
        self.all_tha = []
        try:
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
        except Exception as e :
            msgBox = QtWidgets.QMessageBox()

            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText("Lỗi kết nối")
            msgBox.setWindowTitle("Cảnh báo")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()   
            return         

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

    def kiemtra(self,input_name):
        self.lineEdit_13.setText('')
        self.lineEdit_14.setText('')
        self.lineEdit_15.setText('')
        self.lineEdit_16.setText('')
        username = input_name.text().upper()
        a = False
        if username =='':
            return 
        for khach in self.all_ku:
            if username in khach:
                self.lineEdit_13.setText(' | '.join(khach))
                self.lineEdit_15.setText(' | '.join(khach))
                a = True
                break

        for khach in self.all_tha:
            if username in khach:
                self.lineEdit_14.setText(' | '.join(khach))
                self.lineEdit_16.setText(' | '.join(khach))
                a = True
                return

        if a == False:        
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText("KHÔNG CÓ NHÉ")
            msgBox.setWindowTitle("Xin chia buồn")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_() 






    def closeEvent(self, event):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Đã đủ chỉ tiêu chưa mà về?")
        msgBox.setWindowTitle("Xác nhận")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok| QtWidgets.QMessageBox.No)
        return_vl = msgBox.exec_()
        if msgBox.clickedButton() is msgBox.button(QtWidgets.QMessageBox.Ok):
            event.accept()
        else:
            event.ignore()    















if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec_())
        