# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doktor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DoktorEkrani(object):
    def setupUi(self, DoktorEkrani):
        DoktorEkrani.setObjectName("DoktorEkrani")
        DoktorEkrani.resize(400, 505)
        self.label = QtWidgets.QLabel(DoktorEkrani)
        self.label.setGeometry(QtCore.QRect(60, 20, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(239, 41, 41);")
        self.label.setObjectName("label")
        self.textEdit_doktor = QtWidgets.QTextEdit(DoktorEkrani)
        self.textEdit_doktor.setGeometry(QtCore.QRect(50, 260, 301, 141))
        self.textEdit_doktor.setObjectName("textEdit_doktor")
        self.pushButton_doktor = QtWidgets.QPushButton(DoktorEkrani)
        self.pushButton_doktor.setGeometry(QtCore.QRect(100, 440, 201, 41))
        self.pushButton_doktor.setObjectName("pushButton_doktor")
        self.label_doktor = QtWidgets.QLabel(DoktorEkrani)
        self.label_doktor.setGeometry(QtCore.QRect(30, 90, 341, 131))
        self.label_doktor.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.label_doktor.setWordWrap(True)
        self.label_doktor.setObjectName("label_doktor")

        self.retranslateUi(DoktorEkrani)
        QtCore.QMetaObject.connectSlotsByName(DoktorEkrani)

    def retranslateUi(self, DoktorEkrani):
        _translate = QtCore.QCoreApplication.translate
        DoktorEkrani.setWindowTitle(_translate("DoktorEkrani", "Doktor Ekranı"))
        self.label.setText(_translate("DoktorEkrani", "Hastadan Gelen Mesaj"))
        self.pushButton_doktor.setText(_translate("DoktorEkrani", "Hasta Ekranına Mesaj İlet"))
        self.label_doktor.setText(_translate("DoktorEkrani", "Şu anda hastadan mesaj bulunmuyor. "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DoktorEkrani = QtWidgets.QWidget()
    ui = Ui_DoktorEkrani()
    ui.setupUi(DoktorEkrani)
    DoktorEkrani.show()
    sys.exit(app.exec_())