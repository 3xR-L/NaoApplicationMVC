class ModeloTerapeuta:
    idTerapeuta = 1

    def __init__(self, idTerapeuta, nombre, ape_paterno, ape_materno, genero,
                 fecha_nacimiento, cod_postal, localidad, calle, num,
                 nacionalidad, numero_contacto, correo_electronico,
                Municipio_idMunicipio, usuarios_nombreUsuario):
        self.idTerapeuta = ModeloTerapeuta.idTerapeuta
        ModeloTerapeuta.idTerapeuta += 1
        self.nombre = nombre
        self.ape_paterno = ape_paterno
        self.ape_materno = ape_materno
        self.genero = genero
        self.fecha_nacimiento = fecha_nacimiento
        self.cod_postal = cod_postal
        self.localidad = localidad
        self.calle = calle
        self.num = num
        self.nacionalidad = nacionalidad
        self.numero_contacto = numero_contacto
        self.correo_electronico = correo_electronico
        self.borradoLogico = 0
        self.Municipio_idMunicipio = Municipio_idMunicipio
        self.usuarios_nombreUsuario = usuarios_nombreUsuario

    # Getters
    def getIdTerapeuta(self):
        return self.idTerapeuta

    def getNombre(self):
        return self.nombre

    def getApe_paterno(self):
        return self.ape_paterno

    def getApe_materno(self):
        return self.ape_materno

    def getGenero(self):
        return self.genero

    def getFecha_nacimiento(self):
        return self.fecha_nacimiento

    def getCod_postal(self):
        return self.cod_postal

    def getLocalidad(self):
        return self.localidad

    def getCalle(self):
        return self.calle

    def getNum(self):
        return self.num

    def getNacionalidad(self):
        return self.nacionalidad

    def getNumero_contacto(self):
        return self.numero_contacto

    def getCorreo_electronico(self):
        return self.correo_electronico

    def getBorradoLogico(self):
        return self.borradoLogico

    def getMunicipio_idMunicipio(self):
        return self.Municipio_idMunicipio

    def getUsuarios_nombreUsuario(self):
        return self.usuarios_nombreUsuario

    # Setters
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApe_paterno(self, ape_paterno):
        self.ape_paterno = ape_paterno

    def setApe_materno(self, ape_materno):
        self.ape_materno = ape_materno

    def setGenero(self, genero):
        self.genero = genero

    def setFecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def setCod_postal(self, cod_postal):
        self.cod_postal = cod_postal

    def setLocalidad(self, localidad):
        self.localidad = localidad

    def setCalle(self, calle):
        self.calle = calle

    def setNum(self, num):
        self.num = num

    def setNacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

    def setNumero_contacto(self, numero_contacto):
        self.numero_contacto = numero_contacto

    def setCorreo_electronico(self, correo_electronico):
        self.correo_electronico = correo_electronico

    def setBorradoLogico(self, borradoLogico):
        self.borradoLogico = borradoLogico

    def setMunicipio_idMunicipio(self, Municipio_idMunicipio):
        self.Municipio_idMunicipio = Municipio_idMunicipio

    def setUsuarios_nombreUsuario(self, usuarios_nombreUsuario):
        self.usuarios_nombreUsuario = usuarios_nombreUsuario

    def __str__(self):
        return "idTerapeuta: " + str(self.idTerapeuta) + "\n" + \
               "nombre: " + self.nombre + "\n" + \
               "ape_paterno: " + self.ape_paterno + "\n" + \
               "ape_materno: " + self.ape_materno + "\n" + \
               "genero: " + self.genero + "\n" + \
               "fecha_nacimiento: " + self.fecha_nacimiento + "\n" + \
               "cod_postal: " + self.cod_postal + "\n" + \
               "localidad: " + self.localidad + "\n" + \
               "calle: " + self.calle + "\n" + \
               "num: " + self.num + "\n" + \
               "nacionalidad: " + self.nacionalidad + "\n" + \
               "numero_contacto: " + self.numero_contacto + "\n" + \
               "correo_electronico: " + self.correo_electronico + "\n" + \
               "borradoLogico: " + str(self.borradoLogico) + "\n" + \
               "Municipio_idMunicipio: " + str(self.Municipio_idMunicipio) + "\n" + \
               "usuarios_nombreUsuario: " + self.usuarios_nombreUsuario + "\n"
