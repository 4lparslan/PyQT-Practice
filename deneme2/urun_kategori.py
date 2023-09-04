from PyQt5.QtWidgets import *
from urun_listele_python import Ui_Form

class KategoriEkle(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.kategoriekleform = Ui_Form()
        self.kategoriekleform.setupUi(self)