from PyQt5.QtWidgets import *
from login_python import Ui_Form
from anapencere import AnapencerePage

class LoginPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_Form()
        self.loginform.setupUi(self)
        self.anapencereac = AnapencerePage()

        self.loginform.pushButton.clicked.connect(self.GirisYap)

    def GirisYap(self):
        username = self.loginform.lineEdit_kullaniciadi.text()
        password = self.loginform.lineEdit_parola.text()
        if username == "alp" and password == "123" :
            self.close()
            self.anapencereac.show()

