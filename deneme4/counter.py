# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'counter.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(415, 300)
        self.pushButton_inc = QtWidgets.QPushButton(Form)
        self.pushButton_inc.setGeometry(QtCore.QRect(70, 60, 101, 51))
        self.pushButton_inc.setObjectName("pushButton_inc")
        self.pushButton_dec = QtWidgets.QPushButton(Form)
        self.pushButton_dec.setGeometry(QtCore.QRect(240, 60, 101, 51))
        self.pushButton_dec.setObjectName("pushButton_dec")
        self.label_number = QtWidgets.QLabel(Form)
        self.label_number.setGeometry(QtCore.QRect(200, 180, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_number.setFont(font)
        self.label_number.setObjectName("label_number")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Counter"))
        self.pushButton_inc.setText(_translate("Form", "Increase"))
        self.pushButton_dec.setText(_translate("Form", "Decrease"))
        self.label_number.setText(_translate("Form", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
