# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_python.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 70, 91, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 67, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit_kullaniciadi = QtWidgets.QLineEdit(Form)
        self.lineEdit_kullaniciadi.setGeometry(QtCore.QRect(160, 70, 131, 25))
        self.lineEdit_kullaniciadi.setObjectName("lineEdit_kullaniciadi")
        self.lineEdit_parola = QtWidgets.QLineEdit(Form)
        self.lineEdit_parola.setGeometry(QtCore.QRect(160, 120, 131, 25))
        self.lineEdit_parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_parola.setObjectName("lineEdit_parola")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 210, 101, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Kullanıcı Adı:"))
        self.label_2.setText(_translate("Form", "Parola:"))
        self.pushButton.setText(_translate("Form", "Giriş Yap"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
