# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaEjercicio.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vista import imgVentanaTerapeuta
class Ui_VentanaEjercicio(object):
    def setupUi(self, VentanaEjercicio):
        VentanaEjercicio.setObjectName("VentanaEjercicio")
        VentanaEjercicio.resize(427, 540)
        VentanaEjercicio.setMinimumSize(QtCore.QSize(427, 540))
        VentanaEjercicio.setMaximumSize(QtCore.QSize(427, 540))
        VentanaEjercicio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7 = QtWidgets.QLabel(VentanaEjercicio)
        self.label_7.setGeometry(QtCore.QRect(20, 90, 91, 21))
        self.label_7.setStyleSheet("color: rgb(5, 33, 68);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.tbTerapeuta = QtWidgets.QLabel(VentanaEjercicio)
        self.tbTerapeuta.setGeometry(QtCore.QRect(20, 120, 381, 31))
        self.tbTerapeuta.setStyleSheet("\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(79, 82, 85);")
        self.tbTerapeuta.setObjectName("tbTerapeuta")
        self.label = QtWidgets.QLabel(VentanaEjercicio)
        self.label.setGeometry(QtCore.QRect(60, 0, 291, 81))
        self.label.setStyleSheet("image: url(:/imgVentana/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.tbPaciente = QtWidgets.QLineEdit(VentanaEjercicio)
        self.tbPaciente.setGeometry(QtCore.QRect(20, 180, 311, 31))
        self.tbPaciente.setStyleSheet("\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(79, 82, 85);")
        self.tbPaciente.setText("")
        self.tbPaciente.setObjectName("tbPaciente")
        self.tbPaciente.setEnabled(False)
        self.label_8 = QtWidgets.QLabel(VentanaEjercicio)
        self.label_8.setGeometry(QtCore.QRect(20, 160, 91, 21))
        self.label_8.setStyleSheet("color: rgb(5, 33, 68);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.btnBuscar = QtWidgets.QPushButton(VentanaEjercicio)
        self.btnBuscar.setGeometry(QtCore.QRect(340, 180, 61, 31))
        self.btnBuscar.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 1px;\n"
";\n"
"border-color: rgb(250, 124, 39);\n"
"background-color: rgb(250, 124, 39);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.btnBuscar.setObjectName("btnBuscar")
        self.label_9 = QtWidgets.QLabel(VentanaEjercicio)
        self.label_9.setGeometry(QtCore.QRect(20, 220, 91, 21))
        self.label_9.setStyleSheet("color: rgb(5, 33, 68);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.tbEjercicio = QtWidgets.QLabel(VentanaEjercicio)
        self.tbEjercicio.setGeometry(QtCore.QRect(20, 250, 381, 31))
        self.tbEjercicio.setStyleSheet("\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(79, 82, 85);")
        self.tbEjercicio.setText("Serpientes y escaleras")
        self.tbEjercicio.setObjectName("tbEjercicio")
        self.btnIniciar = QtWidgets.QPushButton(VentanaEjercicio)
        self.btnIniciar.setGeometry(QtCore.QRect(120, 480, 81, 31))
        self.btnIniciar.setMouseTracking(False)
        self.btnIniciar.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(7, 34, 64);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.btnIniciar.setObjectName("btnIniciar")
        self.btnDetener = QtWidgets.QPushButton(VentanaEjercicio)
        self.btnDetener.setGeometry(QtCore.QRect(220, 480, 71, 31))
        self.btnDetener.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 1px;\n"
";\n"
"border-color: rgb(250, 124, 39);\n"
"background-color: rgb(250, 124, 39);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.btnDetener.setObjectName("btnDetener")
        self.label_10 = QtWidgets.QLabel(VentanaEjercicio)
        self.label_10.setGeometry(QtCore.QRect(130, 430, 91, 21))
        self.label_10.setStyleSheet("color: rgb(5, 33, 68);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.tbTiempo = QtWidgets.QLineEdit(VentanaEjercicio)
        self.tbTiempo.setGeometry(QtCore.QRect(210, 430, 81, 31))
        self.tbTiempo.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(79, 82, 85);")
        self.tbTiempo.setText("")
        self.tbTiempo.setObjectName("tbTiempo")
        self.label_11 = QtWidgets.QLabel(VentanaEjercicio)
        self.label_11.setGeometry(QtCore.QRect(20, 290, 191, 21))
        self.label_11.setStyleSheet("color: rgb(5, 33, 68);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.textEditDescripcion = QtWidgets.QTextEdit(VentanaEjercicio)
        # specify the instruction displayed in the text edit box
        self.textEditDescripcion.setPlaceholderText("Escriba aquí la descripción del ejercicio despues de haberlo detenido"+
                                                    " y presione el botón de Detener/Guardar nuevamente para guardar la sesión.")

        self.textEditDescripcion.setGeometry(QtCore.QRect(20, 310, 381, 71))
        self.textEditDescripcion.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(79, 82, 85);")
        self.textEditDescripcion.setObjectName("textEditDescripcion")

        self.retranslateUi(VentanaEjercicio)
        QtCore.QMetaObject.connectSlotsByName(VentanaEjercicio)

    def retranslateUi(self, VentanaEjercicio):
        _translate = QtCore.QCoreApplication.translate
        VentanaEjercicio.setWindowTitle(_translate("VentanaEjercicio", "Dialog"))
        self.label_7.setText(_translate("VentanaEjercicio", "Terapeuta"))
        self.label_8.setText(_translate("VentanaEjercicio", "Paciente"))
        self.btnBuscar.setText(_translate("VentanaEjercicio", "Buscar"))
        self.label_9.setText(_translate("VentanaEjercicio", "Ejercicio"))
        self.btnIniciar.setText(_translate("VentanaEjercicio", "Iniciar"))
        self.btnDetener.setText(_translate("VentanaEjercicio", "Detener/\nGuardar"))
        self.label_10.setText(_translate("VentanaEjercicio", "Tiempo"))
        self.label_11.setText(_translate("VentanaEjercicio", "Descripción del ejercicio"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaEjercicio = QtWidgets.QDialog()
    ui = Ui_VentanaEjercicio()
    ui.setupUi(VentanaEjercicio)
    VentanaEjercicio.show()
    sys.exit(app.exec_())

