from PyQt5.QtWidgets import QApplication
from login import LoginPage

app = QApplication([])

pencere = LoginPage()
pencere.show()
app.exec_()