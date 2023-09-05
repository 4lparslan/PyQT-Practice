from PyQt5.QtWidgets import QApplication
from counter_run import CountPage

app = QApplication([])

win = CountPage()
win.show()
app.exec_()