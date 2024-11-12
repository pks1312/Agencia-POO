class Paquete:
    def __init__(self,id= None,fecha= None,destinos= [], costo= None):
        self.__id = id  
        self.__fecha = fecha
        self.__destinos = destinos
        self.__costo = costo
    
    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id

    def getFecha(self):
        return self.__fecha
    
    def setFecha(self, fecha):
        self.__fecha = fecha

    def getDestinos(self):
        return self.__destinos
    
    def addDestino(self, destino):
        self.__destinos.append(destino)

    def getCosto(self):
        return self.__costo
    
    def setCosto(self, costo):
        self.__costo = costo

    
    def actualizarCosto(self, costo):
        self.__costo += costo

    def destinoExists(self, destino):
        for d in self.__destinos:
            if d.getId() == destino.getId():
                return True
        return False

    def __str__(self):
        return f"Fecha: {self.__fecha} - Destinos: {self.__destinos} - Costo: {self.__costo}"
    
 