# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vistaCrearTerapeuta.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(527, 464)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 170, 91, 16))
        self.label_2.setStyleSheet("color: rgb(5, 33, 68);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.tbterapeutaNombre = QtWidgets.QLineEdit(Dialog)
        self.tbterapeutaNombre.setGeometry(QtCore.QRect(60, 190, 421, 31))
        self.tbterapeutaNombre.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(79, 82, 85);")
        self.tbterapeutaNombre.setObjectName("tbterapeutaNombre")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 240, 91, 21))
        self.label_3.setStyleSheet("color: rgb(5, 33, 68);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.tbTerapeutaApellidos = QtWidgets.QLineEdit(Dialog)
        self.tbTerapeutaApellidos.setGeometry(QtCore.QRect(60, 270, 421, 31))
        self.tbTerapeutaApellidos.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(79, 82, 85);")
        self.tbTerapeutaApellidos.setObjectName("tbTerapeutaApellidos")
        self.tbTerapeutaTelefono = QtWidgets.QLineEdit(Dialog)
        self.tbTerapeutaTelefono.setGeometry(QtCore.QRect(60, 340, 181, 31))
        self.tbTerapeutaTelefono.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(79, 82, 85);")
        self.tbTerapeutaTelefono.setObjectName("tbTerapeutaTelefono")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 310, 91, 21))
        self.label_4.setStyleSheet("color: rgb(5, 33, 68);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.tbTerapeutaCorreo = QtWidgets.QLineEdit(Dialog)
        self.tbTerapeutaCorreo.setGeometry(QtCore.QRect(270, 340, 211, 31))
        self.tbTerapeutaCorreo.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(79, 82, 85);")
        self.tbTerapeutaCorreo.setObjectName("tbTerapeutaCorreo")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(270, 310, 91, 21))
        self.label_5.setStyleSheet("color: rgb(5, 33, 68);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.tbTerapeutaUsuario = QtWidgets.QLineEdit(Dialog)
        self.tbTerapeutaUsuario.setGeometry(QtCore.QRect(60, 130, 181, 31))
        self.tbTerapeutaUsuario.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(79, 82, 85);")
        self.tbTerapeutaUsuario.setObjectName("tbTerapeutaUsuario")
        self.tbTerapeutaContrasena = QtWidgets.QLineEdit(Dialog)
        self.tbTerapeutaContrasena.setGeometry(QtCore.QRect(270, 130, 211, 31))
        self.tbTerapeutaContrasena.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(79, 82, 85);")
        self.tbTerapeutaContrasena.setObjectName("tbTerapeutaContrasena")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(270, 100, 91, 21))
        self.label_6.setStyleSheet("color: rgb(5, 33, 68);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(60, 100, 91, 21))
        self.label_7.setStyleSheet("color: rgb(5, 33, 68);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.btnTerapeutaCancelar = QtWidgets.QPushButton(Dialog)
        self.btnTerapeutaCancelar.setGeometry(QtCore.QRect(360, 390, 121, 31))
        self.btnTerapeutaCancelar.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 1px;\n"
";\n"
"border-color: rgb(250, 124, 39);\n"
"background-color: rgb(250, 124, 39);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.btnTerapeutaCancelar.setObjectName("btnTerapeutaCancelar")
        self.btnCrearTerapeuta = QtWidgets.QPushButton(Dialog)
        self.btnCrearTerapeuta.setGeometry(QtCore.QRect(60, 390, 121, 31))
        self.btnCrearTerapeuta.setMouseTracking(False)
        self.btnCrearTerapeuta.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(7, 34, 64);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.btnCrearTerapeuta.setObjectName("btnCrearTerapeuta")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 131, 71))
        self.label.setStyleSheet("image: url(:/iconoTerapeuta/imgTerapeuta);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(180, 30, 201, 41))
        self.label_8.setStyleSheet("color: rgb(5, 33, 68);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Terapeuta"))
        self.label_2.setText(_translate("Dialog", "Nombre(s)"))
        self.label_3.setText(_translate("Dialog", "Apellidos"))
        self.label_4.setText(_translate("Dialog", "Teléfono"))
        self.label_5.setText(_translate("Dialog", "Correo"))
        self.label_6.setText(_translate("Dialog", "Contraseña"))
        self.label_7.setText(_translate("Dialog", "Usuario"))
        self.btnTerapeutaCancelar.setText(_translate("Dialog", "Calcelar"))
        self.btnCrearTerapeuta.setText(_translate("Dialog", "Crear terapeuta"))
        self.label_8.setText(_translate("Dialog", "Crear terapeuta"))
import imgNaoAplication_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())