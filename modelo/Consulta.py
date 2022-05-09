from conexiones.Conexion import Conexion
from modelo import ModeloUsuario


class Consulta(Conexion):
    '''Clase que permite consultar información de la base de datos'''

    def __init__(self):
        super().__init__()

    """Consultar si el usuario y contraseña son correctos"""
    def consultarUsuario(self, usuario: ModeloUsuario):
        try:
            self.cursor.execute("SELECT * FROM usuarios WHERE nombreUsuario = '{}' and password ='{}'".format(
                usuario.nombreUsuario, usuario.password))
            resultado = self.cursor.fetchall()
            if len(resultado) > 0 and resultado[0][2] == '1':
                return True
            else:
                return False

        except Exception as err:
            print("Error al consultar usuario: {}".format(err))
            return None

    def consultarUsarioPorNombre(self, nombreUsuario):
        try:
            self.cursor.execute("SELECT * FROM usuarios WHERE nombreUsuario = '{}'".format(nombreUsuario))
            resultado = self.cursor.fetchall()
            if len(resultado) > 0:
                return False
            else:
                return True
        except Exception as err:
            print("Error al consultar usuario: {}".format(err))
            return False

    def guardarUsuario(self, user: ModeloUsuario):
        self.cursor.execute(
            "INSERT INTO usuarios Values('{}', '{}', {})".format(user.nombreUsuario, user.password, user.tipo))
        self.db.commit()