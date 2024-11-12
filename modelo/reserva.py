class Reserva:
    def __init__(self, id, paquete, usuario, acompanantes):
        self.__id = id
        self.__paquete = paquete
        self.__usuario = usuario
        self.__acompanantes = acompanantes
    
    
    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getPaquete(self):
        return self.__paquete

    def setPaquete(self, paquete):
        self.__paquete = paquete

    def getUsuario(self):
        return self.__usuario

    def setUsuario(self, usuario):
        self.__usuario = usuario

    def getAcompanantes(self):
        return self.__acompanantes
            