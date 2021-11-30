from HCMK import *
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
        self.pushButton.clicked.connect(self.dangkychua)
        self.pushButton_2.clicked.connect(self.napchua)
        self.pushButton_3.clicked.connect(self.tainapchua)
        self.pushButton_4.clicked.connect(self.cokhong)
        self.pushButton_5.clicked.connect(self.conchoikhong)
        self.pushButton_6.clicked.connect(self.trangthaitk)
        self.pushButton_7.clicked.connect(self.chuyenlinkchua)
        self.pushButton_8.clicked.connect(self.tainap90chua)
        self.pushButton_9.clicked.connect(self.clinkbietdanh)        
        self.pushButton_20.clicked.connect(self.monapmail)
        #Cài đặt event click cho nút bấm K
        self.pushButton_10.clicked.connect(self.dangky)
        self.pushButton_11.clicked.connect(self.taiappku)
        self.pushButton_12.clicked.connect(self.taiapptha)
        self.pushButton_13.clicked.connect(self.laylaitk)
        self.pushButton_14.clicked.connect(self.monapku)
        self.pushButton_15.clicked.connect(self.monaptha)
        self.pushButton_16.clicked.connect(self.nhandiem)
        self.pushButton_17.clicked.connect(self.naptien)
        self.pushButton_18.clicked.connect(self.tainap)
        self.pushButton_19.clicked.connect(self.ruttien)
        self.pushButton_21.clicked.connect(self.kiemtra)
        self.pushButton_22.clicked.connect(self.napdulieu)
        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Enter"), self)
        self.shortcut.activated.connect(self.kiemtra)
        self.setWindowIcon(QtGui.QIcon('logo_kiemkhach1.ico'))


    def dangkychua(self):
        x=("Kiểm tra giúp {} tài khoản: {} *đăng ký* thành công chưa {} *({})*".format("e" if self.comboBox_2.currentText() == "em" else "mình"\
            ,self.lineEdit.text(),"ạ" if self.comboBox_2.currentText() == "em" else "nhé",self.comboBox.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)

    def napchua(self):
        x=("Kiểm tra giúp {} tài khoản: {} *nạp chơi* thành công chưa {} *({})*".format("e" if self.comboBox_2.currentText() == "em" else "mình"\
            ,self.lineEdit.text(),"ạ" if self.comboBox_2.currentText() == "em" else "nhé",self.comboBox.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def tainapchua(self):
        x=("Kiểm tra giúp {} tài khoản: {} *tái nạp chưa* {} *({})*".format("e" if self.comboBox_2.currentText() == "em" else "mình"\
            ,self.lineEdit.text(),"ạ" if self.comboBox_2.currentText() == "em" else "nhé",self.comboBox.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
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
    def chuyenlinkchua(self):
        x=("Kiểm tra giúp {} tài khoản: {} *chuyển về* thành công chưa {} *({})*".format("e" if self.comboBox_2.currentText() == "em" else "mình"\
            ,self.lineEdit.text(),"ạ" if self.comboBox_2.currentText() == "em" else "nhé",self.comboBox.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def tainap90chua(self):
        x=("Kiểm tra giúp {} tài khoản: {} *nạp lại sau 90 ngày* thành công chưa {} *({})*".format("e" if self.comboBox_2.currentText() == "em" else "mình"\
            ,self.lineEdit.text(),"ạ" if self.comboBox_2.currentText() == "em" else "nhé",self.comboBox.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def clinkbietdanh(self):
        x=("Tên tài khoản: {}\nBiệt danh: {}\nVui lòng hỗ trợ chuyển về {} giúp mình nhé!".format(self.lineEdit.text(),self.lineEdit_2.text(),self.comboBox.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def monapmail(self):
        x=("Mail KU: openbet999@gmail.com\nTk KU: {}\nMail khách: {}\nKhách cần hỗ trợ vấn đề mở nạp. Vui lòng kiểm và xử lý giúp mình. Xin cảm ơn!".format(self.lineEdit.text(),self.lineEdit_4.text()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    #Code nút bấm K team
    def dangky(self):
        x=("{} {} hướng dẫn *đăng ký* giúp {} nhé. *({})*".format("Zl" if self.comboBox_3.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_3.currentText() == "Facebook" else "Tl",self.lineEdit_5.text(),self.comboBox_4.currentText(),self.comboBox_5.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def taiappku(self):
        x=("{} {} hướng dẫn *tải app KU* giúp {} nhé.".format("Zl" if self.comboBox_3.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_3.currentText() == "Facebook" else "Tl",self.lineEdit_5.text(),self.comboBox_4.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x) 
    def taiapptha(self):
        x=("{} {} hướng dẫn *tải app THA* giúp {} nhé.".format("Zl" if self.comboBox_3.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_3.currentText() == "Facebook" else "Tl",self.lineEdit_5.text(),self.comboBox_4.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x) 
    def laylaitk(self):
        x=("{} {} hướng dẫn *lấy lại mật khẩu* giúp {} nhé.".format("Zl" if self.comboBox_3.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_3.currentText() == "Facebook" else "Tl",self.lineEdit_5.text(),self.comboBox_4.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x) 
    def monapku(self):
        x=("{} {} hướng dẫn *mở nạp KU* giúp {} nhé.".format("Zl" if self.comboBox_3.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_3.currentText() == "Facebook" else "Tl",self.lineEdit_5.text(),self.comboBox_4.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)  
    def monaptha(self):
        x=("{} {} hướng dẫn *mở nạp THA* giúp {} nhé.".format("Zl" if self.comboBox_3.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_3.currentText() == "Facebook" else "Tl",self.lineEdit_5.text(),self.comboBox_4.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)  
    def nhandiem(self):
        x=("{} {} hướng dẫn *nhận điểm* giúp {} nhé.".format("Zl" if self.comboBox_3.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_3.currentText() == "Facebook" else "Tl",self.lineEdit_5.text(),self.comboBox_4.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def naptien(self):
        x=("{} {} hướng dẫn *nạp tiền* giúp {} nhé.".format("Zl" if self.comboBox_3.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_3.currentText() == "Facebook" else "Tl",self.lineEdit_5.text(),self.comboBox_4.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)  
    def tainap(self):
        x=("{} {} hướng dẫn *tái nạp* giúp {} nhé.".format("Zl" if self.comboBox_3.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_3.currentText() == "Facebook" else "Tl",self.lineEdit_5.text(),self.comboBox_4.currentText()))
        self.textBrowser.setText(x)
        a = QtWidgets.QApplication.clipboard()
        a.setText(x)
    def ruttien(self):
        x=("{} {} hướng dẫn *rút tiền* giúp {} nhé.".format("Zl" if self.comboBox_3.currentText() == "Zalo" \
            else  "Fb" if self.comboBox_3.currentText() == "Facebook" else "Tl",self.lineEdit_5.text(),self.comboBox_4.currentText()))
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
        