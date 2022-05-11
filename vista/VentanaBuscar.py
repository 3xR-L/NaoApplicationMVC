#Create a window to display the search results of the user in the database
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class VentanaBuscar(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowModality(qtc.Qt.ApplicationModal)
        self.setWindowTitle("Administrar Pacientes")
        cx_form = qtw.QWidget()
        self.setCentralWidget(cx_form)
        cx_form.setLayout(qtw.QFormLayout())
        heading = qtw.QLabel("Administración de Pacientes")
        heading.setStyleSheet("color: rgb(5, 33, 68);\nfont: 24pt \"MS Shell Dlg 2\";")
        heading.setAlignment(qtc.Qt.AlignCenter)
        cx_form.setStyleSheet("background-color: rgb(255, 255, 255);")
        #set a minimum size for the window
        self.setMinimumSize(qtc.QSize(1300, 500))
        cx_form.layout().addRow(heading)

        self.table = qtw.QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["Nombre", "Apellido Paterno", "Apellido Materno", "Género", "Fecha de Nacimiento", "Localidad", "Dirección",\
                "No. de Contacto"])
        # enable table modification
        self.table.setEditTriggers(qtw.QAbstractItemView.NoEditTriggers)
        #self.table.setEditTriggers(qtw.QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(qtw.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(qtw.QAbstractItemView.SingleSelection)
        self.table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table.setShowGrid(False)
        self.table.setStyleSheet("selection-background-color: rgb(5, 33, 68);")
        self.table.setStyleSheet("selection-color: rgb(255, 255, 255);")
        self.table.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        #set the width of the columns to fit the content
        self.table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        self.table.setSortingEnabled(True)
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

        # add a search label, line edit and a button in the same row centered
        search_group = qtw.QGroupBox()
        self.le_search = qtw.QLineEdit()
        self.le_search.setFont(qtg.QFont("MS Shell Dlg 2", 12))
        self.le_search.setStyleSheet("color: rgb(5, 33, 68);")
        self.le_search.setPlaceholderText("Buscar")
        # set a maximum length for the line edit
        self.le_search.setMaxLength(30)
        self.le_search.setFixedWidth(300)
        self.le_search.setFixedHeight(30)
        self.btn_search = qtw.QPushButton("Buscar")
        self.btn_search.setStyleSheet("background-color: rgb(5, 33, 68);\ncolor: rgb(255, 255, 255);")
        self.btn_search.setFont(qtg.QFont("MS Shell Dlg 2", 12))
        self.btn_search.setFixedWidth(100)
        self.btn_search.setFixedHeight(30)
        search_group.setLayout(qtw.QHBoxLayout())
        # set size of the group box to fit the content
        search_group.setFixedSize(400, 50)
        #search_group.layout().addWidget(self.le_search, qtc.Qt.AlignCenter)
        #search_group.layout().addWidget(self.btn_search, qtc.Qt.AlignCenter)
        # add the line edit and the button to the layout in the same row centered
        search_group.layout().addWidget(self.le_search, qtc.Qt.AlignCenter)
        search_group.layout().addWidget(self.btn_search)

        #add the search group to the window centered

        #add the buttons in the same row to the window
        group_buttons = qtw.QWidget()
        group_buttons.setLayout(qtw.QHBoxLayout())
        group_buttons.layout().addWidget(search_group)
        group_buttons.layout().addWidget(self.btn_add)
        group_buttons.layout().addWidget(self.btn_edit)
        group_buttons.layout().addWidget(self.btn_delete)
        group_buttons.layout().addWidget(self.btn_close)
        cx_form.layout().addRow(group_buttons)

        #open window in minum size
        self.setMinimumSize(1300, 500)

        self.show()
