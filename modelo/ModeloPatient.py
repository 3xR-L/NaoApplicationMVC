class ModeloPatient:
    def __init__(
        self,
        nombre,
        ape_paterno,
        genero,
        fecha_nacimiento,
        numero_contacto,
        direccion="",
        localidad="",
        ape_materno="",
    ):
        self.nombre = nombre
        self.ape_paterno = ape_paterno
        self.ape_materno = ape_materno
        self.genero = genero
        self.fecha_nacimiento = fecha_nacimiento
        self.localidad = localidad
        self.direccion = direccion
        self.diagnostico = ""
        self.numero_contacto = numero_contacto
        self.Tutor_idTutor = 0

    # Getters
    def getIdPaciente(self):
        return self.idPaciente

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

    def getDiagnostico(self):
        return self.diagnostico

    def getNumero_contacto(self):
        return self.numero_contacto

    def getCorreo_electronico(self):
        return self.correo_electronico

    def getBorradoLogico(self):
        return self.borradoLogico

    def getTutor_idTutor(self):
        return self.Tutor_idTutor

    def getMunicipio_idMunicipio(self):
        return self.Municipio_idMunicipio

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

    def setDiagnostico(self, diagnostico):
        self.diagnostico = diagnostico

    def setNumero_contacto(self, numero_contacto):
        self.numero_contacto = numero_contacto

    def setCorreo_electronico(self, correo_electronico):
        self.correo_electronico = correo_electronico

    def setBorradoLogico(self, borradoLogico):
        self.borradoLogico = borradoLogico

    def setTutor_idTutor(self, Tutor_idTutor):
        self.Tutor_idTutor = Tutor_idTutor

    def setMunicipio_idMunicipio(self, Municipio_idMunicipio):
        self.Municipio_idMunicipio = Municipio_idMunicipio

    def __str__(self):
        return (
            "idPaciente: "
            + str(self.idPaciente)
            + " nombre: "
            + self.nombre
            + " ape_paterno: "
            + self.ape_paterno
            + " ape_materno: "
            + self.ape_materno
            + " genero: "
            + self.genero
            + " fecha_nacimiento: "
            + self.fecha_nacimiento
            + " cod_postal: "
            + self.cod_postal
            + " localidad: "
            + self.localidad
            + " calle: "
            + self.calle
            + " num: "
            + self.num
            + " nacionalidad: "
            + self.nacionalidad
            + " diagnostico: "
            + self.diagnostico
            + " numero_contacto: "
            + self.numero_contacto
            + " correo_electronico: "
            + self.correo_electronico
            + " borradoLogico: "
            + str(self.borradoLogico)
            + " Tutor_idTutor: "
            + str(self.Tutor_idTutor)
            + " Municipio_idMunicipio: "
            + str(self.Municipio_idMunicipio)
        )
