from PyQt5.QtWidgets import *
from doktor import Ui_DoktorEkrani
from hasta_run import HastaPage

class HastaneSistemi(QWidget):
    def __init__(self):
        super().__init__()
        self.doktor = Ui_DoktorEkrani()
        self.doktor.setupUi(self)
        self.hasta = HastaPage()
        self.hasta.show()
        self.hasta.hastasignal.connect(self.HastaBilgi)
        self.doktor.pushButton_doktor.clicked.connect(self.DoktorBilgi)

    def HastaBilgi(self, bilgi):
        self.doktor.label_doktor.setText(bilgi)

    def DoktorBilgi(self):
        info = self.doktor.textEdit_doktor.toPlainText()
        self.hasta.hastaFormu.label_hasta.setText(info)


app =QApplication([])
win = HastaneSistemi()
win.show()
app.exec_()
