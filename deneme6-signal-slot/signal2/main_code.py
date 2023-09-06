from PyQt5.QtWidgets import *
from signal import Ui_MainWindow

class SignalSlotPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mypage = Ui_MainWindow()
        self.mypage.setupUi(self)

        self.mypage.verticalScrollBar.valueChanged[int].connect(self.Progbar)
    def Progbar(self, myvalue):
        self.mypage.progressBar.setValue(myvalue)

uygulama = QApplication([])
pencere = SignalSlotPage()
pencere.show()
uygulama.exec_()