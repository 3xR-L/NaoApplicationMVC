#Create a window to display the search results of the user in the database
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class VentanaBuscar(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowModality(qtc.Qt.ApplicationModal)
        self.setWindowTitle("Buscar")
        cx_form = qtw.QWidget()
        self.setCentralWidget(cx_form)
        cx_form.setLayout(qtw.QFormLayout())
        heading = qtw.QLabel("Administración de Usuarios")
        heading.setStyleSheet("color: rgb(5, 33, 68);\nfont: 24pt \"MS Shell Dlg 2\";")
        heading.setAlignment(qtc.Qt.AlignCenter)
        cx_form.setStyleSheet("background-color: rgb(255, 255, 255);")
        #set a maximum size for the window
        self.setMaximumSize(qtc.QSize(1000, 800))
        #set a minimum size for the window
        self.setMinimumSize(qtc.QSize(500, 500))
        cx_form.layout().addRow(heading)

        self.table = qtw.QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Nombre", "Apellido", "Usuario", "Contraseña"])
        self.table.setEditTriggers(qtw.QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(qtw.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(qtw.QAbstractItemView.SingleSelection)
        self.table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table.setShowGrid(False)
        self.table.setStyleSheet("selection-background-color: rgb(5, 33, 68);")
        self.table.setStyleSheet("selection-color: rgb(255, 255, 255);")
        self.table.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")

        #add the table to the window
        cx_form.layout().addRow(self.table)

        #add the buttons to the window
        self.btn_add = qtw.QPushButton("Agregar")
        self.btn_add.setStyleSheet("background-color: rgb(5, 33, 68);\ncolor: rgb(255, 255, 255);")
        self.btn_add.setFont(qtg.QFont("MS Shell Dlg 2", 12))

        self.btn_edit = qtw.QPushButton("Editar")
        self.btn_edit.setStyleSheet("background-color: rgb(5, 33, 68);\ncolor: rgb(255, 255, 255);")
        self.btn_edit.setFont(qtg.QFont("MS Shell Dlg 2", 12))

        self.btn_delete = qtw.QPushButton("Eliminar")
        self.btn_delete.setStyleSheet("background-color: rgb(5, 33, 68);\ncolor: rgb(255, 255, 255);")
        self.btn_delete.setFont(qtg.QFont("MS Shell Dlg 2", 12))

        self.btn_close = qtw.QPushButton("Cerrar")
        self.btn_close.setStyleSheet("background-color: rgb(5, 33, 68);\ncolor: rgb(255, 255, 255);")
        self.btn_close.setFont(qtg.QFont("MS Shell Dlg 2", 12))

        #add the buttons in the same row to the window
        gropu_buttons = qtw.QWidget()
        gropu_buttons.setLayout(qtw.QHBoxLayout())
        gropu_buttons.layout().addWidget(self.btn_add)
        gropu_buttons.layout().addWidget(self.btn_edit)
        gropu_buttons.layout().addWidget(self.btn_delete)
        gropu_buttons.layout().addWidget(self.btn_close)
        cx_form.layout().addRow(gropu_buttons)

        self.show()
