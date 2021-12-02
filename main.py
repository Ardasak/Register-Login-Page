import sys
from PyQt5 import QtWidgets
import sqlite3


baglanti = sqlite3.connect("Database.db")
cursor = baglanti.cursor()
cursor.execute("Create Table if not exists Kullanıcılar(kullanici_adi TEXT, parola TEXT)")
baglanti.commit()
class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giriş = QtWidgets.QPushButton("Giriş")
        self.yazi = QtWidgets.QLabel("")
        self.yeni = QtWidgets.QPushButton("Oluştur")



        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi)
        v_box.addStretch()
        v_box.addWidget(self.giriş)
        v_box.addWidget(self.yeni)
        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)

        h_box.addStretch()

        self.giriş.clicked.connect(self.login)
        self.yeni.clicked.connect(self.yenikullanici)

        self.setLayout(h_box)

        self.setGeometry(500,100,1000,800)
        self.setWindowTitle("Kullanıcı Girişi")
        self.show()
    def login(self):
        adi = self.kullanici_adi.text()
        par = self.parola.text()
        cursor.execute("Select * From Kullanıcılar where kullanici_adi = ? and parola =?",(adi,par))
        data = cursor.fetchall()
        if (len(data) == 0):
            self.yazi.setText("Böyle bir kullanıcı yok.\nLütfen tekrar deneyin.")
        else:
            self.yazi.setText("Hoşgeldiniz. " + adi)
    def yenikullanici(self):
        try:
            adi1 = self.kullanici_adi.text()
            par1 = self.parola.text()
            cursor.execute("Select * From Kullanıcılar where kullanici_adi = ?",(adi1,))
            data = cursor.fetchall()
            if len(par1)<6:
                self.yazi.setText("Parola 6 hane ya da daha büyük olmalı.")

            if len(data) != 0:
                self.yazi.setText("Bu kullanıcı kayıtlarımızda var.")
            if len(par1) > 6 and len(data)==0:
                cursor.execute("Insert into Kullanıcılar Values(?,?)",(adi1,par1))
                self.yazi.setText("Kullanıcı Oluşturuldu.")
                baglanti.commit()

        except:
            self.yazi.setText("Bir hata oluştu.")



















app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
