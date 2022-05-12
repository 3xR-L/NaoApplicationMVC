# Create the controller for the search window
from vista.VentanaBuscar import VentanaBuscar
from controlador.ControladorCrearUsuario import ControladorCrearUsuario
from modelo.CrudUsuario import CrudUsuario
from PyQt5 import QtWidgets as qtw

class ControladorVentanaBuscar:
    def __init__(self, idTerapeuta):
        self.vista = VentanaBuscar()
        self.idTerapeuta = idTerapeuta
        self.getPatients()
        self.clicks()

    def clicks(self):
        self.vista.btn_add.clicked.connect(self.add)
        self.vista.btn_close.clicked.connect(self.vista.close)
        self.vista.btn_delete.clicked.connect(self.delete)
        self.vista.btn_edit.clicked.connect(self.edit)

    def add(self):
        self.crear = ControladorCrearUsuario(1, self.idTerapeuta)

    def delete(self):
        # Get the selected row
        row = self.vista.table.currentRow()
        # Get the patient id
        idPatient = self.vista.table.item(row, 0).text()
        print(idPatient)
        # Delete the patient from the database
        self.Consulta.eliminarPacientes(idPatient)
        # Delete the patient from the table
        self.vista.table.removeRow(row)
        # Close the window
        self.vista.close()


    # Load patients from the database and show them in the table
    def getPatients(self):
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
        # Get the selected row
        row = self.vista.table.currentRow()
        print(row)
        # Get the patient id
        idPatient = self.vista.table.item(row, 0).text()
        # Open the edit window
        self.vistaEditar = ControladorCrearUsuario(2, self.idTerapeuta, idPatient)
