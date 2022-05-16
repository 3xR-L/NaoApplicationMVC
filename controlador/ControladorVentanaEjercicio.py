import os
import threading
import time
from PyQt5 import QtWidgets as qtw
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from controlador.ControladorVentanaBuscar import ControladorVentanaBuscar
from controlador.ControladorVentanaTablero import ControladorVentanaTablero
from modelo.ClaseCronometro import Cronometro
from modelo.CrudUsuario import CrudUsuario
from vista.VentajaEjercicio import Ui_VentanaEjercicio


class ControladorVentanaEjercicio(qtw.QMainWindow):

    def __init__(self, id):
        ##Originaslemte no tenpia esto
        super().__init__()
        self.bandera = False
        self.idTerapeuta = id
        self.idPaciente = 0
        self.ventana = QtWidgets.QMainWindow()
        self.vista = Ui_VentanaEjercicio()
        self.vista.setupUi(self.ventana)
        self.ventana.show()
        self.clicks()
        self.fillBlanks()
        self.guardar = False
        self.valores = []

    def clicks(self):
        # Abre la ventana
        self.vista.btnIniciar.clicked.connect(self.abrirVentanaTablero)
        self.vista.btnBuscar.clicked.connect(self.abrirVentanaBuscar)
        # Detiene el ejercicio
        self.vista.btnDetener.clicked.connect(self.detener)

    # Fill in the blank labels
    def fillBlanks(self):
        self.Consulta = CrudUsuario()
        tName = self.Consulta.consultarTerapeutaPorId(self.idTerapeuta)
        self.vista.tbTerapeuta.setText(tName[0][1] + " " + tName[0][2])

    def abrirVentanaTablero(self):
        if self.idPaciente != 0:
            self.guardar = False
            self.bandera = True
            self.cvt = ControladorVentanaTablero()
            self.t = threading.Thread(target=self.cronometro)
            self.hiloTiempo()
            self.cvt.con.connect(self.guardarDatos)

    def detener(self):
        # Bansdera = falso
        if self.bandera:
            self.cvt.bandera = False
            self.bandera = False
            self.guardar = True
            self.cvt.cerrar()
        else:
            if self.guardar:
                self.guardarEjercicio()
                self.guardar = False

    def guardarEjercicio(self):
        self.Consulta = CrudUsuario()
        self.Consulta.guardarEjercicio(self.idTerapeuta, self.idPaciente, self.valores, self.vista.tbTiempo.text(),
                                       self.vista.textEditDescripcion.toPlainText())
        # display a message box
        msg = qtw.QMessageBox()
        msg.setIcon(qtw.QMessageBox.Information)
        msg.setText("Ejercicio guardado")
        msg.setWindowTitle("Guardado")
        msg.exec_()

    def abrirVentanaBuscar(self):
        self.cvb = ControladorVentanaBuscar(self.idTerapeuta)
        # self.cvb.vista.selected.connect(self.vista.tbPaciente.setText)
        # get the text
        self.cvb.vista.selected.connect(self.getText)

    def getText(self, text):
        self.vista.tbPaciente.setText(text[1] + " " + text[2])
        self.idPaciente = int(text[0])

    def cronometro(self):
        for hora in range(24):
            if self.bandera == True:
                for minuto in range(60):
                    if self.bandera == True:
                        for segundo in range(60):
                            if self.bandera == True:
                                tiempo = (f'{minuto}:{segundo}')
                                if self.bandera == True:
                                    self.vista.tbTiempo.setText(str(tiempo))
                                    time.sleep(1)
                                else:
                                    break
                            else:
                                break
                    else:
                        break
            else:
                break

    def hiloTiempo(self):
        self.t.start()

    def guardarDatos(self, values):
        self.valores = values
