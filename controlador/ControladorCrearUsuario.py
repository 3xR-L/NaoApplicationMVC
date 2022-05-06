# Create a new user
from vista.VistaCrearUsuario import VistaCrearUsuario
from modelo.ModeloPatient import ModeloPatient
from modelo.ModeloTerapeuta import ModeloTerapeuta

from PyQt5 import QtWidgets as qtw

class ControladorCrearUsuario(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.vista = VistaCrearUsuario()
        print(self.vista.inputs['Tipo de usuario*'])
        #access checkbox from vista
        self.clicks()


    def clicks(self):
        # Set the click event for the checkbox
        self.vista.inputs['Tipo de usuario*'].clicked.connect(self.checkbox_clicked)
        #Abrir la ventana para registrar usuarios
        #self.vista.btnCrear.clicked.connect(self.registrar)


    def checkbox_clicked(self):
        if self.vista.inputs['Tipo de usuario*'].isChecked():
            self.vista.inputs['Tipo de usuario*'].setText('Terapeuta')
            self.vista.inputs['Nombre de usuario*'].setEnabled(True)
            self.vista.inputs['Contraseña*'].setEnabled(True)
            self.vista.inputs['Confirmar contraseña*'].setEnabled(True)
        else:
            self.vista.inputs['Tipo de usuario*'].setText('Paciente')
            self.vista.inputs['Nombre de usuario*'].setEnabled(False)
            self.vista.inputs['Contraseña*'].setEnabled(False)
            self.vista.inputs['Confirmar contraseña*'].setEnabled(False)
            #clear the inputs
            self.vista.inputs['Nombre de usuario*'].setText('')
            self.vista.inputs['Contraseña*'].setText('')
            self.vista.inputs['Confirmar contraseña*'].setText('')