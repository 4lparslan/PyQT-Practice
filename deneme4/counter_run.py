from PyQt5.QtWidgets import *
from counter import Ui_Form

class CountPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.counting = Ui_Form()
        self.counting.setupUi(self)
        self.counter_value = 0

        self.counting.pushButton_inc.clicked.connect(self.ButtonInc)
        self.counting.pushButton_dec.clicked.connect(self.ButtonDec)

    def ButtonInc(self):
        self.counter_value += 1
        self.counting.label_number.setText(str(self.counter_value))
    def ButtonDec(self):
        self.counter_value -= 1
        self.counting.label_number.setText(str(self.counter_value))