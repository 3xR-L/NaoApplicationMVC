from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


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

        heading_font = qtg.QFont('MS Shell Dlg 2', 26, qtg.QFont.Bold)
        heading.setFont(heading_font)

        cx_form.layout().addRow(heading)
        inputs = {
            'Nombre(s)': qtw.QLineEdit(),
            'Apellido Paterno': qtw.QLineEdit(),
            'Apellido Materno': qtw.QLineEdit(),
            'Contraseña': qtw.QLineEdit(
                echoMode=qtw.QLineEdit.Password),
            'Genero': qtw.QComboBox(),
            'Terapeuta': qtw.QCheckBox('Checar si es terapeuta'),
        }
        generos = ('Masculino', 'Femenino')

        inputs['Genero'].addItems(generos)
        for label, widget in inputs.items():
            cx_form.layout().addRow(label, widget)

        label_font = qtg.QFont()
        label_font.setFamily('MS Shell Dlg 2')
        label_font.setPointSize(12)
        label_font.setWeight(qtg.QFont.DemiBold)
        for inp in inputs.values():
            cx_form.layout().labelForField(inp).setFont(label_font)

        self.submit = qtw.QPushButton(
            'Guardar')
        self.cancel = qtw.QPushButton('Cancelar', clicked=self.close)
        cx_form.layout().addRow(self.submit, self.cancel)

        self.submit.setStyleSheet("\n"
            "border-style: solid;\n"
            "border-width: 1px;\n"
            "border-color: rgb(0, 51, 102);\n"
            "background-color: rgb(7, 34, 64);\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 8px;\n"
            "font: 11pt \"MS Shell Dlg 2\";")

        self.cancel.setStyleSheet("\n"
            "border-style: solid;\n"
            "border-width: 1px;\n"
            ";\n"
            "border-color: rgb(250, 124, 39);\n"
            "background-color: rgb(250, 124, 39);\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 8px;\n"
            "font: 11pt \"MS Shell Dlg 2\";")

        # End main UI code
        self.show()

