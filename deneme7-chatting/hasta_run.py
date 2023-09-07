from PyQt5.QtWidgets import *
from hasta import Ui_HastaEkrani
from PyQt5.QtCore import pyqtSignal

class HastaPage(QWidget):
    hastasignal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.hastaFormu = Ui_HastaEkrani()
        self.hastaFormu.setupUi(self)
        self.hastaFormu.pushButton_hasta.clicked.connect(self.HastaMesaj)

    def HastaMesaj(self):
        bilgi = self.hastaFormu.textEdit_hasta.toPlainText()
        self.hastasignal.emit(bilgi)