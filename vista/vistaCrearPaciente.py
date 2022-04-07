# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vistaSeleccionarPaciente.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from vista import imgNaoAplication

class Ui_DialogTipoUsuario(object):
    def setupUi(self, DialogTipoUsuario):
        DialogTipoUsuario.setObjectName("DialogTipoUsuario")
        DialogTipoUsuario.resize(386, 169)
        DialogTipoUsuario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8 = QtWidgets.QLabel(DialogTipoUsuario)
        self.label_8.setGeometry(QtCore.QRect(50, 0, 321, 41))
        self.label_8.setStyleSheet("color: rgb(5, 33, 68);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(DialogTipoUsuario)
        self.label.setGeometry(QtCore.QRect(50, 40, 131, 71))
        self.label.setStyleSheet("image: url(:/iconoTerapeuta/imgTerapeuta);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DialogTipoUsuario)
        self.label_2.setGeometry(QtCore.QRect(210, 40, 131, 71))
        self.label_2.setStyleSheet("\n"
"image: url(:/imgPaciente/imgPaciente);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.btnCrearTerapeuta = QtWidgets.QPushButton(DialogTipoUsuario)
        self.btnCrearTerapeuta.setGeometry(QtCore.QRect(50, 130, 121, 31))
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
        self.btnCrearPaciente = QtWidgets.QPushButton(DialogTipoUsuario)
        self.btnCrearPaciente.setGeometry(QtCore.QRect(210, 130, 121, 31))
        self.btnCrearPaciente.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 1px;\n"
";\n"
"border-color: rgb(250, 124, 39);\n"
"background-color: rgb(250, 124, 39);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.btnCrearPaciente.setObjectName("btnCrearPaciente")

        self.retranslateUi(DialogTipoUsuario)
        QtCore.QMetaObject.connectSlotsByName(DialogTipoUsuario)

    def retranslateUi(self, DialogTipoUsuario):
        _translate = QtCore.QCoreApplication.translate
        DialogTipoUsuario.setWindowTitle(_translate("DialogTipoUsuario", "Seleccionar usuario"))
        self.label_8.setText(_translate("DialogTipoUsuario", "Seleccione el tipo de usuario que desea crear"))
        self.btnCrearTerapeuta.setText(_translate("DialogTipoUsuario", "Crear terapeuta"))
        self.btnCrearPaciente.setText(_translate("DialogTipoUsuario", "Crear paciente"))
#import imgNaoAplication_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogTipoUsuario = QtWidgets.QDialog()
    ui = Ui_DialogTipoUsuario()
    ui.setupUi(DialogTipoUsuario)
    DialogTipoUsuario.show()
    sys.exit(app.exec_())
