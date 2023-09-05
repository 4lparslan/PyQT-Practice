from PyQt5.QtWidgets import QApplication
from calc_run import Calculator

app = QApplication([])

win = Calculator()
win.show()
app.exec_()