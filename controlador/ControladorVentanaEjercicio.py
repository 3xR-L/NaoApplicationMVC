#
import os
import threading
import time

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic,QtWidgets

from vista.VentajaEjercicio import Ui_VentanaEjercicio
from controlador.ControladorVentanaTablero import ControladorVentanaTablero
from controlador.ControladorVentanaBuscar import ControladorVentanaBuscar
from controlador.ControladorVentanaFelicitar import ControladorVentanaFelicitar

from PyQt5 import QtWidgets as qtw
from modelo.ClaseCronometro import Cronometro
class ControladorVentanaEjercicio(qtw.QMainWindow):

    def __init__(self, id):
        ##Originaslemte no tenpia esto
        super().__init__()
        self.bandera = True
        self.idTerapeuta = id
        self.ventana= QtWidgets.QMainWindow()
        self.vista = Ui_VentanaEjercicio()
        self.vista.setupUi(self.ventana)
        self.ventana.show()
        self.t = threading.Thread(target=self.cronometro)
        self.clicks()


    def clicks(self):
        #Abre la ventana
        self.vista.btnIniciar.clicked.connect(self.abrirVentanaTablero)
        self.vista.btnBuscar.clicked.connect(self.abrirVentanaBuscar)
        #Detiene el ejercicio
        self.vista.btnDetener.clicked.connect(self.detener)

    def abrirVentanaTablero(self):
        self.bandera = True
        self.cvt = ControladorVentanaTablero()
        self.hiloTiempo()

    def detener(self):
        #Bansdera = falso
        self.cvt.bandera=False
        self.bandera = False
        #Matar el hilo
        #self.t1.raise_exception()
        self.cvt.cerrar()
    def abrirVentanaBuscar(self):

        self.cvb = ControladorVentanaBuscar(self.idTerapeuta)



    def cronometro(self):
            for hora in range(24):
                if self.bandera == True:
                    for minuto in range(60):
                        if self.bandera == True:
                            for segundo in range(60):
                                if self.bandera == True:
                                    os.system('cls')
                                    tiempo=(f'{minuto}:{segundo}')
                                    print(tiempo)
                                    if (self.bandera == True):
                                        self.vista.tbTiempo.setText(str(tiempo))
                                        time.sleep(1)
                                    else:
                                        time
                                    #time.sleep(0.5)
                                else:
                                    break
                        else:
                            break
                else:
                    break
    def hiloTiempo(self):

        self.t.start()

