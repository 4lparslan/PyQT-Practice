from PyQt5.QtWidgets import *
from signal import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal

class SignalSlotPage(QMainWindow):

    signal1 = pyqtSignal(int)
    signal2 = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.mypage = Ui_MainWindow()
        self.mypage.setupUi(self)
        self.mypage.verticalScrollBar.valueChanged[int].connect(self.signal1[int])
        self.signal1[int].connect(self.signal2[int])
        self.signal2[int].connect(self.slot)
    def slot(self, val):
        self.mypage.progressBar.setValue(val)


app = QApplication([])
win = SignalSlotPage()
win.show()
app.exec_()