import threading
import time
import random
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from vista.VentajaTablero import Ui_VentanaTablero

from PyQt5 import QtWidgets as qtw, QtWidgets
from PyQt5 import QtCore as qtc


class ControladorVentanaTablero(qtw.QMainWindow):
    con = qtc.pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.ventana = QtWidgets.QMainWindow()
        self.vista = Ui_VentanaTablero()
        self.vista.setupUi(self.ventana)
        self.ventana.show()
        self.bandera = True
        self.hilo = threading.Thread(target=self.numerosAleatorios)
        self.cliks()


    def cliks(self):
        self.hilo.start()

    def mover(self):

        posX = self.vista.labelRobot.x()
        posy = self.vista.labelRobot.y()

        if (posX == 520):
            if (posy == -20):
                posX = 20
                posy = 480

            else:
                posy = posy - 100
                posX = 20
        else:
            posX = posX + 100

        self.vista.labelRobot.move(posX, posy)

    def numerosAleatorios(self):
        self.sesion = []
        while (self.bandera == True):
            self.numero = random.randint(1, 10)
            self.sesion.append(self.numero)
            time.sleep(1)

            if self.numero >= 6:
                self.mover()

        self.con.emit(self.sesion)
        time.sleep(.5)
        self.ventana.close()

    def cerrar(self):
        self.bandera = False
