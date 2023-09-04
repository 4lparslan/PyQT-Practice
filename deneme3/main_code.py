from PyQt5.QtWidgets import QApplication
from siparis import Siparispage

app = QApplication([])

pencere = Siparispage()
pencere.show()
app.exec_()