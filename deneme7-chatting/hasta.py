# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hasta.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HastaEkrani(object):
    def setupUi(self, HastaEkrani):
        HastaEkrani.setObjectName("HastaEkrani")
        HastaEkrani.resize(400, 505)
        self.label = QtWidgets.QLabel(HastaEkrani)
        self.label.setGeometry(QtCore.QRect(90, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(239, 41, 41)")
        self.label.setObjectName("label")
        self.label_hasta = QtWidgets.QLabel(HastaEkrani)
        self.label_hasta.setGeometry(QtCore.QRect(30, 90, 341, 131))
        self.label_hasta.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.label_hasta.setWordWrap(True)
        self.label_hasta.setObjectName("label_hasta")
        self.textEdit_hasta = QtWidgets.QTextEdit(HastaEkrani)
        self.textEdit_hasta.setGeometry(QtCore.QRect(50, 260, 301, 141))
        self.textEdit_hasta.setObjectName("textEdit_hasta")
        self.pushButton_hasta = QtWidgets.QPushButton(HastaEkrani)
        self.pushButton_hasta.setGeometry(QtCore.QRect(110, 440, 201, 41))
        self.pushButton_hasta.setObjectName("pushButton_hasta")

        self.retranslateUi(HastaEkrani)
        QtCore.QMetaObject.connectSlotsByName(HastaEkrani)

    def retranslateUi(self, HastaEkrani):
        _translate = QtCore.QCoreApplication.translate
        HastaEkrani.setWindowTitle(_translate("HastaEkrani", "Hasta Ekranı"))
        self.label.setText(_translate("HastaEkrani", "Hasta Bilgi Mesajı"))
        self.label_hasta.setText(_translate("HastaEkrani", "Şu anda doktordan mesaj bulunmuyor."))
        self.pushButton_hasta.setText(_translate("HastaEkrani", "Doktora Mesaj İlet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HastaEkrani = QtWidgets.QWidget()
    ui = Ui_HastaEkrani()
    ui.setupUi(HastaEkrani)
    HastaEkrani.show()
    sys.exit(app.exec_())
