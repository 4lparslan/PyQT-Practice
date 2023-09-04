from PyQt5.QtWidgets import *
from siparis_python import Ui_Form

class Siparispage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.siparisver = Ui_Form()
        self.siparisver.setupUi(self)
        self.SiparisName = [None, None]

        self.siparisver.pushButton.clicked.connect(self.ButonSiparis)

    def ButonSiparis(self):
        if self.siparisver.radioButton_kucuk.isChecked():
            print("küçük")
            self.SiparisName[0] = "küçük"
        if self.siparisver.radioButton_orta.isChecked():
            print("orta")
        if self.siparisver.radioButton_buyuk.isChecked():
            print("buyuk")
        if self.siparisver.radioButton_su.isChecked():
            print("su")
            self.SiparisName[1] = "su"
        if self.siparisver.radioButton_ayran.isChecked():
            print("ayran")
        if self.siparisver.radioButton_kola.isChecked():
            print("kola")

        if self.SiparisName[0] != None and self.SiparisName[1] != None:
            print(self.SiparisName[0] + " " + self.SiparisName[1])