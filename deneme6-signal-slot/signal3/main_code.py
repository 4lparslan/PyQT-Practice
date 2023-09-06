from PyQt5.QtWidgets import *
from signal import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot

class SignalSlotPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mypage = Ui_MainWindow()
        self.mypage.setupUi(self)

    @pyqtSlot(int)
    def on_verticalScrollBar_valueChanged(self,the_value):
        self.mypage.progressBar.setValue(the_value)

uygulama = QApplication([])
pencere = SignalSlotPage()
pencere.show()
uygulama.exec_()