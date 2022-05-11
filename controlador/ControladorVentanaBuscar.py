# Create the controller for the search window
from vista.VentanaBuscar import VentanaBuscar
from controlador.ControladorCrearUsuario import ControladorCrearUsuario
from modelo.CrudUsuario import CrudUsuario

class ControladorVentanaBuscar:
    def __init__(self, idTerapeuta):
        self.vista = VentanaBuscar()
        self.idTerapeuta = idTerapeuta
        self.getPatients()
        self.clicks()

    def clicks(self):
        self.vista.btn_add.clicked.connect(self.add)
        self.vista.btn_close.clicked.connect(self.vista.close)
        #self.vista.btn_delete.clicked.connect(self.delete)

    def add(self):
        self.crear = ControladorCrearUsuario(1)

    #def delete(self):

    # Load patients from the database and show them in the table
    def getPatients(self):
        # Get the patients id from the database
        self.Consulta = CrudUsuario()
        self.Consulta.consultarPacientesAsociados(self.idTerapeuta)


