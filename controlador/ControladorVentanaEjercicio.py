#
import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic,QtWidgets

from vista.VentajaEjercicio import Ui_VentanaEjercicio
from controlador.ControladorVentanaTablero import ControladorVentanaTablero


from PyQt5 import QtWidgets as qtw
from modelo.ClaseCronometro import Cronometro
class ControladorVentanaEjercicio(qtw.QMainWindow):
    def __init__(self):
        ##Originaslemte no tenpia esto
        super().__init__()
        self.ventana= QtWidgets.QMainWindow()
        self.vista = Ui_VentanaEjercicio()
        self.vista.setupUi(self.ventana)
        self.ventana.show()

        self.clicks()


    def clicks(self):
        #Abre la ventana
        self.vista.btnIniciar.clicked.connect(self.abrirVentanaTablero)
        #Detiene el ejercicio
        self.vista.btnDetener.clicked.connect(self.detener)

        print("Entra a los clicks")
    def abrirVentanaTablero(self):

        print("Entra a Abrin Vt")
        self.cvt = ControladorVentanaTablero()


    def detener(self):
        #Bansdera = falso
        self.cvt.bandera=False
        self.cvt.cerrar()
