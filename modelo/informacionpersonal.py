from modelo.user import User

class InformacionPersonal(User):
    def __init__(self, nombre= None, apellido= None, genero= None, direccion= None,
                  telefono= None, fechaNacimiento= None,id=None, username= None, password= None, correo=None, rol=None):
        super().__init__(id, username, password, correo, rol)
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fechaNacimiento = fechaNacimiento
        self.__genero = genero
        self.__direccion = direccion
        self.__telefono = telefono

    # Getters
    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getFechaNacimiento(self):
        return self.__fechaNacimiento

    def getGenero(self):
        return self.__genero

    def getDireccion(self):
        return self.__direccion

    def getTelefono(self):
        return self.__telefono

    # Setters
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellido(self, apellido):
        self.__apellido = apellido

    def setFechaNacimiento(self, fechaNacimiento):
        self.__fechaNacimiento = fechaNacimiento

    def setGenero(self, genero):
        self.__genero = genero

    def setDireccion(self, direccion):
        self.__direccion = direccion

    def setTelefono(self, telefono):
        self.__telefono = telefono