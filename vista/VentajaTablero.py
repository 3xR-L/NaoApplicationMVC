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
        # disable close button on top right corner
        VentanaTablero.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        self.labelTablero = QtWidgets.QLabel(VentanaTablero)
        self.labelTablero.setGeometry(QtCore.QRect(-70, -90, 801, 791))
        self.labelTablero.setStyleSheet("image: url(:/imgVentana/tablero);")
        self.labelTablero.setText("")
        self.labelTablero.setObjectName("labelTablero")
        self.labelRobot = QtWidgets.QLabel(VentanaTablero)
        self.labelRobot.setGeometry(QtCore.QRect(20, 480, 111, 131))
        self.labelRobot.setStyleSheet(
            "background-color:rgba(255, 0, 0, 0);\n"
            "image: url(:/imgVentana/img2);\n"
            ""
        )
        self.labelRobot.setText("")
        self.labelRobot.setObjectName("labelRobot")

        self.retranslateUi(VentanaTablero)
        QtCore.QMetaObject.connectSlotsByName(VentanaTablero)

    def retranslateUi(self, VentanaTablero):
        _translate = QtCore.QCoreApplication.translate
        VentanaTablero.setWindowTitle(_translate("VentanaTablero", "Dialog"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    VentanaTablero = QtWidgets.QDialog()
    ui = Ui_VentanaTablero()
    ui.setupUi(VentanaTablero)
    VentanaTablero.show()
    sys.exit(app.exec_())
