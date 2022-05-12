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
                self.cursor.execute(
                    "SELECT idTerapeuta FROM terapeuta WHERE usuarios_nombreUsuario = '{}'".format(resultado[0][0]))
                id = self.cursor.fetchall()
                return id[0][0]
            else:
                return 0

        except Exception as err:
            print("Error al consultar usuario: {}".format(err))
            return 0

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

    def guardarUsuario(self, data: [ModeloTerapeuta, ModeloPatient], type: int, idTerapist=None, user: [ModeloUsuario] = None):
        print('aqui')
        if(type == -1):
            table ='terapeuta'
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
            if(type == 0):
                table2 = 'terapeuta_has_paciente'
                print('aqui2')
                self.cursor.execute(
                    "INSERT INTO {} (nombre, ape_paterno, ape_materno, genero, fecha_nacimiento, localidad, calle,\
                    numero_contacto, Tutor_idTutor) Values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(table, data.nombre,
                    data.ape_paterno, data.ape_materno, data.genero, data.fecha_nacimiento, data.localidad, data.direccion, data.numero_contacto,
                    idTerapist)
                )
                # get the last id inserted
                print(self.cursor.execute("SELECT idPaciente FROM paciente ORDER BY idPaciente DESC limit 1"))
                #self.cursor.execute(
                #    "INSERT INTO {} (terapeuta_idTerapeuta, paciente_idPaciente) Values('{}', '{}')".format(
                        #table2, id_paciente, idTerapist)
                #)
            else:
                self.cursor.execute(
                    "UPDATE {} SET nombre ='{}', ape_paterno='{}', ape_materno='{}', genero='{}', fecha_nacimiento='{}', localidad='{}', calle='{}',\
                    numero_contacto='{}' WHERE idPaciente = {}".format(table, data.nombre,
                                                                                                    data.ape_paterno,
                                                                                                    data.ape_materno,
                                                                                                    data.genero,
                                                                                                    data.fecha_nacimiento,
                                                                                                    data.localidad,
                                                                                                    data.direccion,
                                                                                                    data.numero_contacto,
                                                                     type)
                )

        self.db.commit()

    def consultarPacientesAsociados(self, id: int):
        try:
            self.cursor.execute("SELECT idPaciente FROM paciente WHERE Tutor_idTutor = '{}'".format(id))
            id_pacientes = self.cursor.fetchall()
            self.lista_pacientes = ()
            for idOnly in id_pacientes:
                self.cursor.execute(
                    "SELECT * FROM paciente WHERE idPaciente = '{}'".format(
                        idOnly[0]))
                self.lista_pacientes = self.lista_pacientes + self.cursor.fetchall()

            return self.lista_pacientes
        except Exception as err:
            print("Error al consultar pacientes: {}".format(err))
            return self.lista_pacientes

    def eliminarPacientes(self, id: int):
        try:
            self.cursor.execute("DELETE FROM terapeuta_has_paciente WHERE paciente_idPaciente = '{}'".format(id))
            self.cursor.execute("DELETE FROM sesionterapeutica WHERE Paciente_idPaciente = '{}'".format(id))
            self.cursor.execute("DELETE FROM paciente WHERE idPaciente = '{}'".format(id))
            self.db.commit()
        except Exception as err:
            print("Error al eliminar pacientes: {}".format(err))

    def consultarPacientePorId(self, id: int):
        try:
            self.cursor.execute("SELECT * FROM paciente WHERE idPaciente = '{}'".format(id))
            return self.cursor.fetchall()
        except Exception as err:
            print("Error al consultar paciente: {}".format(err))