# Create the controller for the search window
from vista.VentanaBuscar import VentanaBuscar
from controlador.ControladorCrearUsuario import ControladorCrearUsuario

class ControladorVentanaBuscar:
    def __init__(self):
        self.vista = VentanaBuscar()
        self.clicks()

    def clicks(self):
        self.vista.btn_add.clicked.connect(self.add)
        self.vista.btn_close.clicked.connect(self.vista.close)
        #self.vista.btn_delete.clicked.connect(self.delete)

    def add(self):
        self.crear = ControladorCrearUsuario(1)

    #def delete(self):
