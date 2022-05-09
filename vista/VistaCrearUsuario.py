from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import datetime


class VistaCrearUsuario(qtw.QMainWindow):

    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        # Main UI code goes here
        #Set window as modal
        self.setWindowModality(qtc.Qt.ApplicationModal)
        self.setWindowTitle('Registro de Usuario')
        cx_form = qtw.QWidget()
        self.setCentralWidget(cx_form)
        cx_form.setLayout(qtw.QFormLayout())
        heading = qtw.QLabel("Registro de Usuario")
        heading.setStyleSheet("color: rgb(5, 33, 68);\nfont: 24pt \"MS Shell Dlg 2\";")

        #Color the background of the window white
        cx_form.setStyleSheet("background-color: rgb(255, 255, 255);")
        #Set a fixed size for the window
        self.setFixedSize(380, 460)
        #Don't allow the user to resize the window
        self.setFixedSize(self.size())

        cx_form.layout().addRow(heading)
        self.inputs = {
            'Nombre(s)*': qtw.QLineEdit(),
            'Apellido paterno*': qtw.QLineEdit(),
            'Apellido materno': qtw.QLineEdit(),
            'Fecha de nacimiento*': qtw.QDateEdit(
                 self,
                 date=datetime.date.today(),
                 calendarPopup=True,
                 maximumDate=datetime.date.today(),
                 displayFormat='yyyy-MM-dd'
                 ),
            'Género*': qtw.QComboBox(),
            'Teléfono*': qtw.QLineEdit(),
            'Dirección': qtw.QLineEdit(),
            'Localidad': qtw.QLineEdit(),
            'Tipo de usuario*': qtw.QCheckBox('TERAPEUTA', checked=True),
            'Nombre de usuario*': qtw.QLineEdit(),
            'Contraseña*': qtw.QLineEdit(
                echoMode=qtw.QLineEdit.Password),
            'Confirmar contraseña*': qtw.QLineEdit(
                echoMode=qtw.QLineEdit.Password)
        }

        generos = ('Masculino', 'Femenino')

        self.inputs['Género*'].addItems(generos)

        for label, widget in self.inputs.items():
            cx_form.layout().addRow(label, widget)

        label_font = qtg.QFont()
        label_font.setFamily('MS Shell Dlg 2')
        label_font.setPointSize(12)
        label_font.setWeight(qtg.QFont.DemiBold)
        for inp in self.inputs.values():
            cx_form.layout().labelForField(inp).setStyleSheet("color: rgb(5, 33, 68);\nfont: 13pt \"MS Shell Dlg 2\";")


        # Set the maximum characters for the inputs
        self.inputs['Nombre(s)*'].setMaxLength(30)
        self.inputs['Apellido paterno*'].setMaxLength(25)
        self.inputs['Apellido materno'].setMaxLength(25)
        self.inputs['Nombre de usuario*'].setMaxLength(25)
        self.inputs['Contraseña*'].setMaxLength(15)
        self.inputs['Confirmar contraseña*'].setMaxLength(15)
        self.inputs['Dirección'].setMaxLength(50)
        self.inputs['Localidad'].setMaxLength(25)
        self.inputs['Teléfono*'].setMaxLength(10)

        self.submit = qtw.QPushButton('Guardar')
        self.cancel = qtw.QPushButton('Cancelar', clicked=self.close)
        cx_form.layout().addRow(self.submit, self.cancel)

        self.submit.setStyleSheet("\n"
            "border-style: solid;\n"
            "border-width: 1px;\n"
            "border-color: rgb(0, 51, 102);\n"
            "background-color: rgb(7, 34, 64);\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 8px;\n"
            "font: 12pt \"MS Shell Dlg 2\";")

        self.cancel.setStyleSheet("\n"
            "border-style: solid;\n"
            "border-width: 1px;\n"
            ";\n"
            "border-color: rgb(250, 124, 39);\n"
            "background-color: rgb(250, 124, 39);\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 8px;\n"
            "font: 12pt \"MS Shell Dlg 2\";")

        #Set size of submit button
        self.submit.setFixedSize(165, 25)
        #Set size of cancel button
        self.cancel.setFixedSize(190, 25)

        self.message = qtw.QLabel()
        self.message.setStyleSheet("color: rgb(5, 33, 68);\nfont: 10pt \"MS Shell Dlg 2\";")
        cx_form.layout().addRow(self.message)
        self.message.setAlignment(qtc.Qt.AlignCenter)
        # End main UI code
        self.show()