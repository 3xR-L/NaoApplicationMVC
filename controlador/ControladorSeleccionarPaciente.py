from PyQt5 import QtWidgets
from  vista.vistaCrearPaciente import Ui_DialogTipoUsuario
from vista.vistaCrearTerapeuta import Ui_Dialog

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class ControladorSeleccionarPaciente(QtWidgets.QMainWindow): #Hereda para poder usar va window
    def __init__(self):
        super().__init__()
        #Le asignamos la vista a un objeto para manipularlo
        self.ui = Ui_DialogTipoUsuario()
        self.ui.setupUi(self)
        self.clicks()

    def clicks(self):
       # self.ui.btn.clicked.connect(self.ocultarContrasena)
        self.ui.btnCrearTerapeuta.clicked.connect(self.abrirVentanaCrearTerapeuta)
       #self.ui.btnCrear.clicked.connect(self.abrirVistaSeleccionarUsuario)

    def abrirVentanaCrearPaciente(self):
        pass

    def abrirVentanaCrearTerapeuta(self):
        # Abrir vista crear terapeuta
        self.ventana = QtWidgets.QMainWindow()
        self.uiTerapeuta = Ui_Dialog
        self.uiTerapeuta.setupUi(self.ventana)
        self.ventana.show()
        self.close()
        print("click en terapeuta")
