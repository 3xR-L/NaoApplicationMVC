# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaLogin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vista import imgNaoAplication

class Ui_VentanaLogin(object):
    def setupUi(self, VentanaLogin):
        VentanaLogin.setObjectName("VentanaLogin")
        VentanaLogin.resize(331, 423)
        VentanaLogin.setMinimumSize(QtCore.QSize(331, 423))
        VentanaLogin.setMaximumSize(QtCore.QSize(331, 423))
        self.lblLogo = QtWidgets.QLabel(VentanaLogin)
        self.lblLogo.setGeometry(QtCore.QRect(60, 30, 201, 41))
        self.lblLogo.setStyleSheet("image: url(:/login/logo);")
        self.lblLogo.setText("")
        self.lblLogo.setObjectName("lblLogo")
        self.label_2 = QtWidgets.QLabel(VentanaLogin)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 91, 16))
        self.label_2.setStyleSheet("color: rgb(5, 33, 68);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(VentanaLogin)
        self.label_4.setGeometry(QtCore.QRect(70, 270, 121, 21))
        self.label_4.setStyleSheet("color: rgb(7, 34, 64);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.btnAceptar = QtWidgets.QPushButton(VentanaLogin)
        self.btnAceptar.setGeometry(QtCore.QRect(100, 310, 121, 31))
        self.btnAceptar.setMouseTracking(False)
        self.btnAceptar.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(7, 34, 64);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.btnAceptar.setObjectName("btnAceptar")
        self.tbNombre = QtWidgets.QLineEdit(VentanaLogin)
        self.tbNombre.setGeometry(QtCore.QRect(70, 130, 181, 31))
        self.tbNombre.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(79, 82, 85);")
        self.tbNombre.setObjectName("tbNombre")
        self.lblFondo = QtWidgets.QLabel(VentanaLogin)
        self.lblFondo.setGeometry(QtCore.QRect(-10, -10, 361, 441))
        self.lblFondo.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.lblFondo.setText("")
        self.lblFondo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFondo.setObjectName("lblFondo")
        self.label_3 = QtWidgets.QLabel(VentanaLogin)
        self.label_3.setGeometry(QtCore.QRect(70, 200, 91, 16))
        self.label_3.setStyleSheet("color: rgb(5, 33, 68);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.tbPassword = QtWidgets.QLineEdit(VentanaLogin)
        self.tbPassword.setGeometry(QtCore.QRect(70, 220, 181, 31))
        self.tbPassword.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(79, 82, 85);")
        self.tbPassword.setObjectName("tbPassword")
        self.checkBoxRecordar = QtWidgets.QCheckBox(VentanaLogin)
        self.checkBoxRecordar.setGeometry(QtCore.QRect(230, 270, 21, 17))
        self.checkBoxRecordar.setText("")
        self.checkBoxRecordar.setObjectName("checkBoxRecordar")
        self.btnCrear = QtWidgets.QPushButton(VentanaLogin)
        self.btnCrear.setGeometry(QtCore.QRect(100, 360, 121, 31))
        self.btnCrear.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 1px;\n"
";\n"
"border-color: rgb(250, 124, 39);\n"
"background-color: rgb(250, 124, 39);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.btnCrear.setObjectName("btnCrear")
        self.btnOjoAbierto = QtWidgets.QPushButton(VentanaLogin)
        self.btnOjoAbierto.setGeometry(QtCore.QRect(250, 220, 41, 31))
        self.btnOjoAbierto.setStyleSheet("image: url(:/login/ojoAbierto);\n"
"background-color: rgb(255, 255, 255);")
        self.btnOjoAbierto.setText("")
        self.btnOjoAbierto.setObjectName("btnOjoAbierto")
        self.btnOjoCerrado = QtWidgets.QPushButton(VentanaLogin)
        self.btnOjoCerrado.setGeometry(QtCore.QRect(250, 220, 41, 31))
        self.btnOjoCerrado.setStyleSheet("image: url(:/login/ojoCerrado);\n"
"background-color: rgb(255, 255, 255);")
        self.btnOjoCerrado.setText("")
        self.btnOjoCerrado.setObjectName("btnOjoCerrado")
        self.lblFondo.raise_()
        self.lblLogo.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.btnAceptar.raise_()
        self.tbNombre.raise_()
        self.label_3.raise_()
        self.tbPassword.raise_()
        #self.checkBoxRecordar.raise_()
        self.btnCrear.raise_()
        self.btnOjoAbierto.raise_()
        self.btnOjoCerrado.raise_()

        self.retranslateUi(VentanaLogin)
        QtCore.QMetaObject.connectSlotsByName(VentanaLogin)

    def retranslateUi(self, VentanaLogin):
        _translate = QtCore.QCoreApplication.translate
        VentanaLogin.setWindowTitle(_translate("VentanaLogin", "NaoAplication"))
        self.label_2.setText(_translate("VentanaLogin", "Nombre"))
        #self.label_4.setText(_translate("VentanaLogin", "Recordar contraseña"))
        self.btnAceptar.setText(_translate("VentanaLogin", "Aceptar"))
        self.label_3.setText(_translate("VentanaLogin", "Password"))
        self.btnCrear.setText(_translate("VentanaLogin", "Crear Usuario"))



#if __name__ == "__main__":
    #import sys
    #app = QtWidgets.QApplication(sys.argv)
    #VentanaLogin = QtWidgets.QDialog()
    #ui = Ui_VentanaLogin()
    #ui.setupUi(VentanaLogin)
    #VentanaLogin.show()
    #sys.exit(app.exec_())

