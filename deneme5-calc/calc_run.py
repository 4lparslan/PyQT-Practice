from PyQt5.QtWidgets import *
from calc import Ui_Form

class Calculator(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.counting = Ui_Form()
        self.counting.setupUi(self)

