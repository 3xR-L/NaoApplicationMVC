#Abrimos la vemtana del Login
from PyQt5 import QtWidgets

from modelo.Consulta import Consulta
from modelo.ModeloUsuario import ModeloUsuario
from vista.VentanaLogin import Ui_VentanaLogin #importamos la clase
from PyQt5 import QtWidgets as qtw
from controlador.ControladorCrearUsuario import ControladorCrearUsuario

#Para Mostrar el Login 
class ControladorLogin(qtw.QMainWindow): #Hereda para poder usar window QtWidgets.QMainWindow

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
        # Checamos que el usuario este registrado si se pulsa el boton
        self.ui.btnAceptar.clicked.connect(self.ingresar)
        #Abrir la ventana para registrar usuarios
        self.ui.btnCrear.clicked.connect(self.registrar)

    def inicializarGUI(self):
        self.ui.btnOjoCerrado.clicked.connect(self.mostrarContraseña)

        #Para hacer visible e invisible la contraseña
    def ocultarContrasena(self):
        self.ui.btnOjoAbierto.setVisible(False)
        self.ui.btnOjoCerrado.setVisible(True)
        self.ui.tbPassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def mostrarContrasena(self):
        self.ui.btnOjoAbierto.setVisible(True)
        self.ui.btnOjoCerrado.setVisible(False)
        self.ui.tbPassword.setEchoMode(QtWidgets.QLineEdit.Normal)    #Mostramos la password

    def ingresar(self):
        self.Consulta = Consulta()
        #Obtenemos los datos de la interfaz
        usuario = self.ui.tbNombre.text()
        password = self.ui.tbPassword.text()
        self.ModeloUsuario = ModeloUsuario(usuario, password)

        if (self.Consulta.consultarUsuario(self.ModeloUsuario)):
            print("Usuario Correcto")
            '''
            Inicializar la ventana de la selección de ejercicios
            '''
        else:
            print("Usuario Incorrecto")

    def registrar(self):
        self.vcu = ControladorCrearUsuario(1)