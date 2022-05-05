# Create a new user
import sys
from vista.VistaCrearUsuario import VistaCrearUsuario
from modelo.ModeloPatient import ModeloPatient
from modelo.ModeloTerapeuta import ModeloTerapeuta
from PyQt5 import QtWidgets as qtw

class ControladorCrearUsuario():
    def __init__(self):
        self.vista = VistaCrearUsuario()

