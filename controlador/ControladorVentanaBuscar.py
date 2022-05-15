# Create the controller for the search window
from vista.VentanaBuscar import VentanaBuscar
from controlador.ControladorCrearUsuario import ControladorCrearUsuario
from modelo.CrudUsuario import CrudUsuario
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class ControladorVentanaBuscar:
    def __init__(self, idTerapeuta):
        self.vista = VentanaBuscar()
        self.idTerapeuta = idTerapeuta
        self.getPatients()
        self.clicks()
        self.vista.le_search.returnPressed.connect(self.search)
        # define what to do when the user clicks on the table
        self.vista.table.cellClicked.connect(self.select)


    def clicks(self):
        self.vista.btn_add.clicked.connect(self.add)
        self.vista.btn_close.clicked.connect(self.vista.close)
        self.vista.btn_delete.clicked.connect(self.delete)
        self.vista.btn_edit.clicked.connect(self.edit)
        self.vista.btn_search.clicked.connect(self.search)


    def search(self):
        # search the patient in the table by the name
        text = self.vista.le_search.text()
        # show all rows
        self.vista.table.setRowCount(0)
        # Get the patients id from the database
        self.getPatients()
        for i in range(self.vista.table.rowCount()):
            if self.vista.table.item(i, 1).text().lower().find(text.lower()) != -1 or self.vista.table.item(i, 2).text().lower().find(text.lower()) \
                    != -1 or self.vista.table.item(i, 3).text().lower().find(text.lower()) != -1:
                pass
            else:
                self.vista.table.hideRow(i)


    def add(self):
        self.crear = ControladorCrearUsuario(1, self.idTerapeuta)
        self.crear.vista.submitted.connect(self.getPatients)

    def delete(self):
        if self.vista.table.currentRow() != -1:
            # Get the selected row
            row = self.vista.table.currentRow()
            # Get the patient id
            idPatient = self.vista.table.item(row, 0).text()
            # Delete the patient from the database
            self.Consulta.eliminarPacientes(idPatient)
            # Delete the patient from the table
            self.vista.table.removeRow(row)
            # Reload the table
            #self.getPatients()


    # Load patients from the database and show them in the table
    def getPatients(self):
        self.vista.table.clearContents()
        # Get the patients id from the database
        self.Consulta = CrudUsuario()
        listaPacientes = self.Consulta.consultarPacientesAsociados(self.idTerapeuta)
        j =0

        for i in listaPacientes:
            #insert a row in the table
            self.vista.table.insertRow(j)
            self.vista.table.setItem(j, 0, qtw.QTableWidgetItem(str(i[0])))
            self.vista.table.setItem(j, 1, qtw.QTableWidgetItem(i[1]))
            self.vista.table.setItem(j, 2, qtw.QTableWidgetItem(i[2]))
            self.vista.table.setItem(j, 3, qtw.QTableWidgetItem(i[3]))
            self.vista.table.setItem(j, 4, qtw.QTableWidgetItem(i[4]))
            self.vista.table.setItem(j, 5, qtw.QTableWidgetItem(i[5]))
            self.vista.table.setItem(j, 6, qtw.QTableWidgetItem(i[7]))
            self.vista.table.setItem(j, 7, qtw.QTableWidgetItem(i[8]))
            self.vista.table.setItem(j, 8, qtw.QTableWidgetItem(i[12]))

            j = j + 1

    # edit the patient data
    def edit(self):
        if self.vista.table.currentRow() != -1:
            # Get the selected row
            row = self.vista.table.currentRow()
            # Get the patient id
            idPatient = self.vista.table.item(row, 0).text()
            # Open the edit window
            self.vistaEditar = ControladorCrearUsuario(2, self.idTerapeuta, idPatient)
            self.vistaEditar.vista.submitted.connect(self.getPatients)

    def select(self):
        self.vista.selected.emit([self.vista.table.item(self.vista.table.currentRow(), 0).text(), self.vista.table.item(self.vista.table.currentRow(), 1).text(),
                                      " "+self.vista.table.item(self.vista.table.currentRow(), 2).text()])
        self.vista.close()