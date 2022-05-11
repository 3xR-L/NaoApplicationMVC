#
import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic,QtWidgets

from vista.VentajaEjercicio import Ui_VentanaEjercicio
from controlador.ControladorVentanaTablero import ControladorVentanaTablero
from controlador.ControladorVentanaBuscar import ControladorVentanaBuscar

from PyQt5 import QtWidgets as qtw
from modelo.ClaseCronometro import Cronometro
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
        #Abre la ventana
        self.vista.btnIniciar.clicked.connect(self.abrirVentanaTablero)
        self.vista.btnBuscar.clicked.connect(self.abrirVentanaBuscar)
        #Detiene el ejercicio
        self.vista.btnDetener.clicked.connect(self.detener)

        print("Entra a los clicks")

    def abrirVentanaTablero(self):
        self.cvt = ControladorVentanaTablero()

    def detener(self):
        #Bansdera = falso
        self.cvt.bandera=False
        self.cvt.cerrar()
        
    def abrirVentanaBuscar(self):
        self.cvb = ControladorVentanaBuscar(self.idTerapeuta)
