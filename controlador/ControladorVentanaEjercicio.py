#
import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic,QtWidgets

from vista.VentajaEjercicio import Ui_VentanaEjercicio
from controlador.ControladorVentanaTablero import ControladorVentanaTablero
from controlador.ControladorVentanaBuscar import ControladorVentanaBuscar

from PyQt5 import QtWidgets as qtw

class ControladorVentanaEjercicio(qtw.QMainWindow):
    def __init__(self, id):
        ##Originaslemte no tenpia esto
        super().__init__()
        self.idTerapeuta = id
        self.ventana= QtWidgets.QMainWindow()
        self.vista = Ui_VentanaEjercicio()
        self.vista.setupUi(self.ventana)
        self.ventana.show()

        self.clicks()


    def clicks(self):
        self.vista.btnIniciar.clicked.connect(self.abrirVentanaTablero)
        self.vista.btnBuscar.clicked.connect(self.abrirVentanaBuscar)

    def abrirVentanaTablero(self):
        self.cvt = ControladorVentanaTablero()

    def abrirVentanaBuscar(self):
        self.cvb = ControladorVentanaBuscar(self.idTerapeuta)