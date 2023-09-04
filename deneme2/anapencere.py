from PyQt5.QtWidgets import *
from anapencere_python import Ui_MainWindow
from urun_listele import UrunListelePage
from urun_kategori import KategoriEkle

class AnapencerePage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.anapencereform = Ui_MainWindow()
        self.anapencereform.setupUi(self)
        self.urunlisteleform = UrunListelePage()
        self.kategoriekleform = KategoriEkle()
        self.anapencereform.urunlistele.triggered.connect(self.urunlisteleFormu)
        self.anapencereform.kategoriekle.triggered.connect(self.kategoriEkleFormu)
    def urunlisteleFormu(self):
        self.urunlisteleform.show()
    def kategoriEkleFormu(self):
        self.kategoriekleform.show()