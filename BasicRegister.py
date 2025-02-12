import sys
import sqlite3
from PyQt5 import  QtWidgets

class Pencere(QtWidgets.QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.baglanti()

        self.init_ui()
    
    def baglanti(self):
        baglanti = sqlite3.connect("database.db")
        
        self.cursor= baglanti.cursor()
        
        self.cursor.execute("CREATE TABLE IF NOT EXISTS kayıt (Ad TEXT, Soyad TEXT, Şifre TEXT)")
        baglanti.commit()
    
    def init_ui(self):
        
        self.ad = QtWidgets.QLineEdit()
        self.soyad = QtWidgets.QLineEdit()
        self.sifre = QtWidgets.QLineEdit()
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.kayıt = QtWidgets.QPushButton("Kayıt")
        self.göster = QtWidgets.QPushButton("Göster")
        self.yazi = QtWidgets.QLabel("")
        
        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.ad)
        v_box.addWidget(self.soyad)
        v_box.addWidget(self.sifre)
        v_box.addWidget(self.yazi)
        v_box.addStretch()
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.kayıt)
        v_box.addWidget(self.göster)

        
        h_box = QtWidgets.QHBoxLayout()
        
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        
        
        self.setWindowTitle("Kullanıcı Girişi")     

        self.setLayout(v_box)
        self.setLayout(h_box)
        
        self.temizle.clicked.connect(self.register)
        self.kayıt.clicked.connect(self.register)
        self.göster.clicked.connect(self.click)
        
        
        self.show()
        
    def register(self):
        sender = self.sender() 
    
        if sender.text() == "Temizle":
            self.ad.clear()
            self.soyad.clear()
            self.sifre.clear()
        else:
            adı = self.ad.text()
            soyadı = self.soyad.text()
            
        
            self.cursor.execute("Select * from kayıt where ad = ? and soyad = ?", (adı,soyadı))
        
            data = self.cursor.fetchall()
        
            if len(data) == 0 :
                self.yazi.setText("Kullanıcı Bulunamadı")
            else:
                self.yazi.setText("Hoşgeldin " + adı)
        
    def click(self):
        
            print("""
                     Ad : {}
                     Soyad : {}
                     Sifre : {}
                     
                """.format(self.ad.text(),self.soyad.text(),self.sifre.text()))

app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

pencere.setGeometry(200,200,500,500)

sys.exit(app.exec_())
