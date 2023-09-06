from PyQt5.QtWidgets import *
from signal import Ui_MainWindow

class SignalSlotPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mypage = Ui_MainWindow()
        self.mypage.setupUi(self)

    def slot1(self,val):
        print(val)
        self.mypage.progressBar.setValue(val)

app = QApplication([])
win = SignalSlotPage()
win.show()
app.exec_()