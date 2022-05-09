# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaTablero.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vista import imgVentanaTerapeuta
class Ui_VentanaTablero(object):
    def setupUi(self, VentanaTablero):
        VentanaTablero.setObjectName("VentanaTablero")
        VentanaTablero.resize(660, 617)
        VentanaTablero.setMinimumSize(QtCore.QSize(660, 617))
        VentanaTablero.setMaximumSize(QtCore.QSize(660, 617))
        VentanaTablero.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelTablero = QtWidgets.QLabel(VentanaTablero)
        self.labelTablero.setGeometry(QtCore.QRect(-70, -90, 801, 791))
        self.labelTablero.setStyleSheet("image: url(:/imgVentana/tablero);")
        self.labelTablero.setText("")
        self.labelTablero.setObjectName("labelTablero")
        self.labelRobot = QtWidgets.QLabel(VentanaTablero)
        self.labelRobot.setGeometry(QtCore.QRect(20, 480, 111, 131))
        self.labelRobot.setStyleSheet("background-color:rgba(255, 0, 0, 0);\n"
"image: url(:/imgVentana/img2);\n"
"")
        self.labelRobot.setText("")
        self.labelRobot.setObjectName("labelRobot")
        self.btnMover = QtWidgets.QPushButton(VentanaTablero)
        self.btnMover.setGeometry(QtCore.QRect(590, 40, 61, 31))
        self.btnMover.setMouseTracking(False)
        self.btnMover.setStyleSheet("\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(7, 34, 64);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.btnMover.setObjectName("btnMover")

        self.retranslateUi(VentanaTablero)
        QtCore.QMetaObject.connectSlotsByName(VentanaTablero)

    def retranslateUi(self, VentanaTablero):
        _translate = QtCore.QCoreApplication.translate
        VentanaTablero.setWindowTitle(_translate("VentanaTablero", "Dialog"))
        self.btnMover.setText(_translate("VentanaTablero", "Mover"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaTablero = QtWidgets.QDialog()
    ui = Ui_VentanaTablero()
    ui.setupUi(VentanaTablero)
    VentanaTablero.show()
    sys.exit(app.exec_())

