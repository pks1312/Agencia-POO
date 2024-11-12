

class User:
    def __init__(self,id= None,username = None, password= None, correo= None, rol= None):
        self.__id = id
        self.__username = username
        self.__password = password
        self.__correo = correo 
        self.__rol = rol
        
    def getAttribute(self, atributo):
        if atributo == "id":
            return self.__id
        elif atributo == "username":
            return self.__username
        elif atributo == "password":
            return self.__password
        elif atributo == "correo":
            return self.__correo
        else:
            return None

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id  
    
    def getUsername(self):
        return self.__username
    
    def setUsername(self, username):
        self.__username = username

    def getPassword(self):
        return self.__password
    
    def setPassword(self, password):
        self.__password = password

    def getCorreo(self):
        return self.__correo
    
    def setCorreo(self, correo):
        self.__correo = correo
    
    def getRol(self):
        return self.__rol

    def setRol(self, rol):
        self.__rol = rol
    
    def __str__(self):
        return f"Usuario: {self.__username} - Correo: {self.__correo} - Password: {self.__password} - ID: {self.__id}"
