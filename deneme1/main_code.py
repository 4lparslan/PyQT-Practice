from PyQt5.QtWidgets import *
from form import Ui_MainWindow

class main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.qtTasarim = Ui_MainWindow()
        self.qtTasarim.setupUi(self)

        self.qtTasarim.pushButton_ekle.clicked.connect(self.EkleTikla)
        self.qtTasarim.pushButton.clicked.connect(self.DuzenleTikla)

    def EkleTikla(self):
        isim = self.qtTasarim.lineEdit_isim.text()
        gsm = self.qtTasarim.lineEdit_gsm.text()
        print(isim + " " + gsm)
    def DuzenleTikla(self):
        print("Düzenle Çalıştı")

app = QApplication([])
pencere = main()
pencere.show()
app.exec_()

