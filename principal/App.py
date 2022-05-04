#Esta es la aplicación principal 
#Importamos la ventana principal(loggin)

import sys
from PyQt5 import QtWidgets
from controlador.ControladorLogin import ControladorLogin

#Crear main 
#mandar llamar la ventana del login 

if __name__ == '__main__':
    app= QtWidgets.QApplication(sys.argv)
    ui= ControladorLogin()
    ui.show()
    sys.exit(app.exec_())