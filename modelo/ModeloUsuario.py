class ModeloUsuario:
    def __init__(self, nombreUsuario: str, password: str, tipo: int = 1):
        self.nombreUsuario = nombreUsuario
        self.password = password
        self.tipo = tipo

    # Getters
    def getNombreUsuario(self):
        return self.nombreUsuario

    def getPassword(self):
        return self.password

    def getTipo(self):
        return self.tipo

    # Setters
    def setNombreUsuario(self, nombreUsuario: str):
        self.nombreUsuario = nombreUsuario

    def setPassword(self, password: str):
        self.password = password

    def setTipo(self, tipo: int):
        self.tipo = tipo
