import mysql
from conexiones.Conexion    import Conexion
from modelo.ModeloUsuario import ModeloUsuario


class ConsultaUsuario(Conexion):

    def __init__(self):
        super().__init__()

    def consultarUsuario(self, usuario: ModeloUsuario):
        try:
            self.cursor.execute("SELECT * FROM usuarios WHERE nombreUsuario = '{}' and password ='{}'".format(
                usuario.nombreUsuario, usuario.password))
            resultado = self.cursor.fetchall()
            if len(resultado) > 0:
                return True
            else:
                return False
        except Exception as err:
            print("Error al consultar usuario: {}".format(err))
            return None

