import threading
import time
import random
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from vista.VentajaTablero import Ui_VentanaTablero


from PyQt5 import QtWidgets as qtw, QtWidgets


class ControladorVentanaTablero(qtw.QMainWindow):
    numero = 0
    bandera = False
    def __init__(self):
        super().__init__()
        self.ventana = QtWidgets.QMainWindow()
        self.vista = Ui_VentanaTablero()
        self.vista.setupUi(self.ventana)
        self.ventana.show()

        self.bandera=True
        self.cliks()


    def cliks(self):

        hilo = threading.Thread(target=self.numerosAleatorios)
        hilo.start()
        #self.vista.btnMover.clicked.connect(self.numerosAleatorios)


    def mover(self):

            posX=self.vista.labelRobot.x()
            posy=self.vista.labelRobot.y()
            print("entra a mover" + str(posX))

            if(posX== 520):
                if(posy==-20):
                    posX=20
                    posy=480
                    #Se muestran los gifts

                else:
                 posy=posy-100
                 posX=20
            else:
                posX = posX + 100


            self.vista.labelRobot.move(posX, posy)
            print("posy" + str(posy))
            print("posx" + str(posX))

    def numerosAleatorios(self):
        print("Entra a los numeros aleatorios")

        while (self.bandera == True):
            self.numero = random.randint(1,10)
            print(self.numero)
            time.sleep(1)

            if self.numero >= 6:
                self.mover()
    def cerrar(self):
        print("Entra a cerrar Tablero")
        self.ventana.close()

