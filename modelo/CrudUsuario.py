from conexiones.Conexion import Conexion
from modelo import ModeloUsuario
from modelo.ModeloTerapeuta import ModeloTerapeuta
from modelo.ModeloPatient import ModeloPatient

class CrudUsuario(Conexion):
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

    def guardarUsuario(self, data: [ModeloTerapeuta, ModeloPatient], type: int, user: [ModeloUsuario] = None):
        if(type == 1):
            table = 'terapeuta'
            self.cursor.execute(
                "INSERT INTO usuarios Values('{}', '{}', {})".format(user.nombreUsuario, user.password, user.tipo))
            self.cursor.execute(
                "INSERT INTO {} (nombre, ape_paterno, ape_materno, genero, fecha_nacimiento, localidad, calle,"
                "numero_contacto, borradoLogico, usuarios_nombreUsuario) Values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                    table, data.nombre,
                    data.ape_paterno, data.ape_materno, data.genero, data.fecha_nacimiento, data.localidad,
                    data.direccion, data.numero_contacto,
                    user.tipo, user.nombreUsuario)
            )
        else:
            table = 'paciente'
            self.cursor.execute(
                "INSERT INTO {} (nombre, ape_paterno, ape_materno, genero, fecha_nacimiento, localidad, calle,\
                numero_contacto) Values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(table, data.nombre,
                data.ape_paterno, data.ape_materno, data.genero, data.fecha_nacimiento, data.localidad, data.direccion, data.numero_contacto)
            )
        self.db.commit()