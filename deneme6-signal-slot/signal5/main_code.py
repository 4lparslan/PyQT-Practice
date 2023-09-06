from PyQt5.QtWidgets import QMainWindow, QApplication
from signal import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal

class SignalSlotPage(QMainWindow):

    signal1 = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.mypage = Ui_MainWindow()
        self.mypage.setupUi(self)
        self.mypage.verticalScrollBar.valueChanged[int].connect(self.slot1)
        self.signal1.connect(self.slot2)

    def slot1(self, val):
        self.signal1.emit(val)

    def slot2(self, valid):
        self.mypage.progressBar.setValue(valid)

app = QApplication([])
win = SignalSlotPage()
win.show()
app.exec_()
