import sys

from PyQt5.QtWidgets import QApplication,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QWidget,QMainWindow,QScrollArea
from PyQt5.QtGui import QFont,QPixmap,QIcon
from PyQt5.QtCore import QSize
import win32gui, win32con

hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)

class gonder():
    def __init__(self,a):
        self.iade=a
    def son(self):
        return self.iade

class tasicerik(QWidget):
    def __init__(self,sayi,renk):
        super().__init__()
        self.layout=QHBoxLayout(self)
        self.layout.addStretch()
        self.dosyaisimi=""
        if renk=="blue":
            renk="mavi"
        elif renk=="red":
            renk="kirmizi"
        elif renk=="black":
            renk="siyah"
        elif renk=="yellow":
            renk="sari"
        elif renk=="sahteokey":
            sayi=""

        self.image=QPixmap("Taşlar\\"+str(renk)+str(sayi)+".png")
        self.imagelabel=QLabel()
        self.imagelabel.setPixmap(self.image)
        self.layout.addWidget(self.imagelabel)
        self.layout.addStretch()

class taslik(QWidget):
    def __init__(self,sayi,renk,parent):
        super().__init__()
        self.ui(sayi,renk,parent)

    def ui(self,sayi,renk,parent):
        self.vlayout=QVBoxLayout()
        self.label=QLabel("2")
        self.labelwidgeti=QWidget()
        self.labellayoutu=QHBoxLayout(self.labelwidgeti)
        self.labellayoutu.addStretch()
        self.labellayoutu.addWidget(self.label)
        self.labellayoutu.addStretch()
        self.label.setFont(QFont("Calibri",15))
        self.btsatiri=QWidget()
        self.hlayout=QHBoxLayout(self.btsatiri)
        self.bt1=QPushButton("-")
        self.bt2=QPushButton("+")
        self.bt1.setFixedSize(25,22)
        self.bt2.setFixedSize(25,22)
        self.bt1.clicked.connect(lambda: self.tiklama(parent))
        self.bt2.clicked.connect(lambda: self.tiklama(parent))
        self.hlayout.addWidget(self.bt1)
        self.hlayout.addWidget(self.bt2)
        self.tasicerigi=tasicerik(sayi,renk)
        self.vlayout.addWidget(self.tasicerigi)
        self.vlayout.addWidget(self.labelwidgeti)
        self.vlayout.addWidget(self.btsatiri)
        self.vlayout.setSpacing(1)
        self.setLayout(self.vlayout)

        self.labelwidgeti.setStyleSheet("background-color:lightgreen")

    def tiklama(self,parent):
        sender=self.sender().text()
        self.labeldegeri=int(self.label.text())
        if sender=="+":
            if self.labeldegeri==0 or self.labeldegeri==1:
                self.label.setText(str(self.labeldegeri+1))
                self.labelwidgeti.setStyleSheet("background-color:lightgreen")
        elif sender=="-":
            if self.labeldegeri==2 or self.labeldegeri==1:
                if self.labeldegeri==2:
                    self.label.setText("1")
                elif self.labeldegeri==1:
                    self.label.setText("0")
                    self.labelwidgeti.setStyleSheet("background-color:grey")
                    # if parent==1:
                    #     s1.tasliksil(self)
                    # elif parent==2:
                    #     s2.tasliksil(self)
                    # elif parent==3:
                    #     s3.tasliksil(self)
                    # elif parent==4:
                    #     s4.tasliksil(self)
                    # elif parent=="sahteokey":
                    #     s5.tasliksil(self)


class satir(QWidget):
    def __init__(self,renk,satirsayisi):
        super().__init__()
        self.ui(renk,satirsayisi)
    def ui(self,renk,satirsayisi):

        self.hlayout=QHBoxLayout()
        self.taslik1=taslik(1,renk,satirsayisi)
        self.taslik2=taslik(2,renk,satirsayisi)
        self.taslik3=taslik(3,renk,satirsayisi)
        self.taslik4=taslik(4,renk,satirsayisi)
        self.taslik5=taslik(5,renk,satirsayisi)
        self.taslik6=taslik(6,renk,satirsayisi)
        self.taslik7=taslik(7,renk,satirsayisi)
        self.taslik8=taslik(8,renk,satirsayisi)
        self.taslik9=taslik(9,renk,satirsayisi)
        self.taslik10=taslik(10,renk,satirsayisi)
        self.taslik11=taslik(11,renk,satirsayisi)
        self.taslik12=taslik(12,renk,satirsayisi)
        self.taslik13=taslik(13,renk,satirsayisi)



        self.hlayout.addWidget(self.taslik1)
        self.hlayout.addWidget(self.taslik2)
        self.hlayout.addWidget(self.taslik3)
        self.hlayout.addWidget(self.taslik4)
        self.hlayout.addWidget(self.taslik5)
        self.hlayout.addWidget(self.taslik6)
        self.hlayout.addWidget(self.taslik7)
        self.hlayout.addWidget(self.taslik8)
        self.hlayout.addWidget(self.taslik9)
        self.hlayout.addWidget(self.taslik10)
        self.hlayout.addWidget(self.taslik11)
        self.hlayout.addWidget(self.taslik12)
        self.hlayout.addWidget(self.taslik13)
        self.setLayout(self.hlayout)

    def tasliksil(self,obje):
        self.hlayout.removeWidget(obje)
        self.hlayout.addWidget(QLabel(""))

class sahteokeysatiri(QWidget):
    def __init__(self,renk,satirsayisi):
        super().__init__()
        self.ui(renk,satirsayisi)
    def ui(self,renk,satirsayisi):

        self.hlayout=QHBoxLayout()
        self.taslik1=taslik(1,renk,satirsayisi)
        self.hlayout.addWidget(self.taslik1)
        self.setLayout(self.hlayout)

    def tasliksil(self,obje):
        self.hlayout.removeWidget(obje)
        self.hlayout.addWidget(QLabel(""))



s1=""
s2=""
s3=""
s4=""
s5=""

class Anapencere(QMainWindow):


    def __init__(self):
        super(Anapencere, self).__init__()
        self.ui()
        self.setWindowTitle("Okey Taş Sayacı")
        self.setWindowIcon(QIcon("icon.ico"))
    def ui(self):
        global s1
        global s2
        global s3
        global s4
        global s5

        satir1 = satir("blue", 1)
        satir2 = satir("black", 2)
        satir3 = satir("red", 3)
        satir4 = satir("yellow", 4)
        satir5 = sahteokeysatiri("sahteokey", "sahteokey")
        s1=satir1
        s2=satir2
        s3=satir3
        s4=satir4
        s5=satir5

        scrolliciwidget=QWidget()
        scricilayout=QVBoxLayout(scrolliciwidget)
        scricilayout.addWidget(satir1)
        scricilayout.addWidget(satir2)
        scricilayout.addWidget(satir3)
        scricilayout.addWidget(satir4)
        scricilayout.addWidget(satir5)



        self.scrollwidgeti=QWidget()
        self.scrollwidgetlayoutu=QHBoxLayout(self.scrollwidgeti)
        self.scrollarea=QScrollArea()
        self.scrollarea.setWidget(scrolliciwidget)
        self.scrollwidgetlayoutu.addWidget(self.scrollarea)
        self.setStyleSheet("background-color:grey")
        scrolliciwidget.setStyleSheet("background-color:silver")
        self.setCentralWidget(self.scrollwidgeti)
        self.setFixedWidth(1341)





app=QApplication(sys.argv)
anapencere=Anapencere()
anapencere.show()
sys.exit(app.exec_())