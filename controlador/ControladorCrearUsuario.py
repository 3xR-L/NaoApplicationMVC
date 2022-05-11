# Create a new user
from modelo.ModeloUsuario import ModeloUsuario
from vista.VistaCrearUsuario import VistaCrearUsuario
from modelo.ModeloPatient import ModeloPatient
from modelo.ModeloTerapeuta import ModeloTerapeuta
import re
from PyQt5 import QtWidgets as qtw
from modelo.CrudUsuario import CrudUsuario


class ControladorCrearUsuario():
    letters_spaces = re.compile(r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]*$')
    numbers = re.compile(r'^[0-9]*$')
    # letters and numbers and no spaces
    letters_numbers = re.compile(r'^[a-zA-Z0-9]*$')
    # letters, numbers and special characters
    letters_numbers_special = re.compile(r'^[a-zA-Z0-9@#$%&_-]*$')
    # letters, numbers and spaces
    letters_numbers_spaces = re.compile(r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9\s]*$')

    def __init__(self, mode=0):
        super().__init__()
        self.vista = VistaCrearUsuario()
        self.vista.inputs['Tipo de usuario*'].setEnabled(False)
        if mode == 0:
            pass
        else:
            self.vista.inputs['Tipo de usuario*'].setChecked(False)
            self.vista.inputs['Tipo de usuario*'].setText('PACIENTE')
            self.vista.inputs['Nombre de usuario*'].setEnabled(False)
            self.vista.inputs['Contraseña*'].setEnabled(False)
            self.vista.inputs['Confirmar contraseña*'].setEnabled(False)

        # access checkbox from vista
        self.clicks()

    def clicks(self):
        # Set the click event for the checkbox
        # self.vista.inputs['Tipo de usuario*'].clicked.connect(self.checkbox_clicked)
        # Set the click event for the button to create the user
        self.vista.submit.clicked.connect(self.create_user)

    def create_user(self):
        # Validate the inputs
        valid_data = self.validate_inputs()
        # Check if the username doesn't exist
        if valid_data:
            # Create the user
            self.Consulta = CrudUsuario()
            resultado = self.Consulta.consultarUsarioPorNombre(self.vista.inputs['Nombre de usuario*'].text())
            print(resultado)
            if resultado:
                # Save the user in the database
                self.save_user()
                self.vista.message.setText('Usuario guardado correctamente.')
                self.vista.message.setStyleSheet('color: green')
            else:
                self.vista.message.setText('El usuario ya existe.')
                self.vista.message.setStyleSheet('color: red')
        else:
            # Show error message
            self.vista.message.setText('Llenar los valores con *. Revisar que las contraseñas coincidan.\n\
                No usar espacios en nombre de usuario o contraseña.\nLa contraseña debe tener al menos 6 caracteres.')
            self.vista.message.setStyleSheet('color: red')

    def validate_inputs(self):
        for values in self.vista.inputs.values():
            if values == self.vista.inputs['Apellido materno'] or values == self.vista.inputs['Dirección'] \
                    or values == self.vista.inputs['Localidad'] or values == self.vista.inputs['Tipo de usuario*'] \
                    or values == self.vista.inputs['Género*'] or values == self.vista.inputs['Fecha de nacimiento*']:
                continue
            else:
                if values != self.vista.inputs['Nombre de usuario*'] and values != self.vista.inputs['Contraseña*'] \
                        and values != self.vista.inputs['Confirmar contraseña*']:
                    if values.text() == '':
                        return False
                else:
                    if self.vista.inputs['Tipo de usuario*'].isChecked() == False:
                        continue
                    else:
                        if values.text() == '':
                            return False

        if self.vista.inputs['Tipo de usuario*'].isChecked() and (
                self.letters_numbers_special.match(self.vista.inputs['Nombre de usuario*'].text()) is None or \
                self.letters_numbers_special.match(self.vista.inputs['Contraseña*'].text()) is None or \
                self.letters_numbers_special.match(self.vista.inputs['Confirmar contraseña*'].text()) is None or \
                len(self.vista.inputs['Contraseña*'].text()) < 6):
            return False

        if self.vista.inputs['Contraseña*'].text() != self.vista.inputs['Confirmar contraseña*'].text() and \
            self.vista.inputs['Tipo de usuario*'].isChecked():
            return False

        if self.numbers.match(self.vista.inputs['Teléfono*'].text()) is None or len(
                self.vista.inputs['Teléfono*'].text()) != 10:
            return False

        if self.letters_spaces.match(self.vista.inputs['Nombre(s)*'].text()) is None or \
                self.letters_spaces.match(self.vista.inputs['Apellido paterno*'].text()) is None or \
                self.letters_spaces.match(
                    self.vista.inputs['Apellido materno'].text()) is None or self.letters_numbers_spaces.match(
            self.vista.inputs['Dirección'].text()) is None or \
                self.letters_numbers_spaces.match(self.vista.inputs['Localidad'].text()) is None:
            return False

        self.vista.message.setText('Datos ingresados correctamente.')
        self.vista.message.setStyleSheet('color: green')
        return True

    def save_user(self):
        try:
            if self.vista.inputs['Tipo de usuario*'].isChecked():
                user = ModeloUsuario(self.vista.inputs['Nombre de usuario*'].text(),
                                     self.vista.inputs['Contraseña*'].text())
                data = ModeloTerapeuta(self.vista.inputs['Nombre(s)*'].text(),
                                       self.vista.inputs['Apellido paterno*'].text(),
                                       self.vista.inputs['Género*'].currentText(),
                                       self.vista.inputs['Fecha de nacimiento*'].text(),
                                       self.vista.inputs['Teléfono*'].text(), self.vista.inputs['Dirección'].text(),
                                       self.vista.inputs['Localidad'].text(),
                                       self.vista.inputs['Apellido materno'].text())
                self.Consulta.guardarUsuario( data, 1, user)

            else:
                data = ModeloPatient(self.vista.inputs['Nombre(s)*'].text(), self.vista.inputs['Apellido paterno*'].text(),
                                     self.vista.inputs['Género*'].currentText(), self.vista.inputs['Fecha de nacimiento*'].text(),
                                     self.vista.inputs['Teléfono*'].text(), self.vista.inputs['Dirección'].text(),
                                     self.vista.inputs['Localidad'].text(), self.vista.inputs['Apellido materno'].text())
                self.Consulta.guardarUsuario(data, 0)

            self.show_message()

        except Exception as e:
            print(e)
            self.vista.message.setText('Error al guardar el usuario.')

    def show_message(self):
        # open a message box to show the user that the user was saved
        msg = qtw.QMessageBox()
        msg.setIcon(qtw.QMessageBox.Information)
        msg.setText("El usuario fue registrado correctamente.")
        msg.setWindowTitle("Usuario registrado")
        msg.setStandardButtons(qtw.QMessageBox.Ok)
        msg.exec_()
        self.vista.close()