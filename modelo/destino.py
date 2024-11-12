class Destino():
    def __init__(self, nombre= None,descripcion= None, costo= None,id= None):  
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__costo = costo

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getDescripcion(self):
        return self.__descripcion

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def getCosto(self):
        return self.__costo

    def setCosto(self, costo):
        self.__costo = costo