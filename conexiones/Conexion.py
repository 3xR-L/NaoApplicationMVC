# Make a class that represents a connection to a SQL database
import pymysql


class Conexion:

    def __init__(self):
        self.__host = "localhost"
        self.__user = "root"
        self.__password = "maestria"
        self.__database = "cognidroneeg"
        self.__port = 3306
        self.db = self.conectar()
        self.cursor = self.db.cursor()

    # Make a method that connects to the database
    def conectar(self):
        try:
            return pymysql.connect(host=self.__host, user=self.__user, password=self.__password, db=self.__database,
                               port=self.__port)
        except pymysql.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            return None

    # Make a method that closes the connection to the database
    def cerrar(self):
        self.db.close()

