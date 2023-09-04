from PyQt5.QtWidgets import *
from urun_listele_python import Ui_Form

class UrunListelePage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.urunlisteleform = Ui_Form()
        self.urunlisteleform.setupUi(self)