import time

from vista.VentajaTablero import Ui_VentanaTablero


from PyQt5 import QtWidgets as qtw, QtWidgets


class ControladorVentanaTablero(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = QtWidgets.QMainWindow()
        self.vista = Ui_VentanaTablero()
        self.vista.setupUi(self.ventana)
        self.ventana.show()
        self.cliks()

    def cliks(self):

        print("55555555555555")
        self.vista.btnMover.clicked.connect(self.mover)


    def mover(self):

            posX=self.vista.labelRobot.x()
            posy=self.vista.labelRobot.y()
            print("entra a mover" + str(posX))

            if(posX== 520):
                if(posy==-20):
                    posX=20
                    posy=480
                else:
                 posy=posy-100
                 posX=20
            else:
                posX = posX + 100


            self.vista.labelRobot.move(posX, posy)
            print("posy" + str(posy))
            print("posx" + str(posX))
