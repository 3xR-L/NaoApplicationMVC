#Abrimos la vemtana del Login 

from PyQt5 import QtWidgets
import sys
from vista.VentanaLogin import Ui_VentanaLogin #importamos la clase
from vista.VistaLoggin import ClaseVistaLogin

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

#Para Mostrar el Login 
class ControladorVentanaLogin(QtWidgets.QMainWindow): #Hereda para poder usar va window
    def __init__(self):
        super().__init__()
        #Le asignamos la vista a un objeto para manipularlo 
        self.ui = Ui_VentanaLogin()
        self.ui.setupUi(self)
        #self.inicializarGUI()

        #-----EVENTOS CLICK
        self.clicks()



        ##ocultamos El ojito
        self.ui.btnOjoAbierto.setVisible(False)

        #Ocultamos la contraseña
        self.ui.tbPassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def clicks(self):
        self.ui.btnOjoCerrado.clicked.connect(self.mostrarContrasena)
        self.ui.btnOjoAbierto.clicked.connect(self.ocultarContrasena)

    def inicializarGUI(self):
        self.ui.btnOjoCerrado.clicked.connect(self.mostrarContraseña)

        #Para hacer visible e invisible la contraseña
    def ocultarContrasena(self):
        self.ui.btnOjoAbierto.setVisible(False)
        self.ui.btnOjoCerrado.setVisible(True)

    def mostrarContrasena(self):
        self.ui.btnOjoAbierto.setVisible(True)
        self.ui.btnOjoCerrado.setVisible(False)


