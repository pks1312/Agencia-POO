from modelo.user import User    
from dao.dao_user import daoUser
from utils.encoder import Encoder
class UserDTO:

    def listarUsuarios(self):
        daouser = daoUser()
        resultado = daouser.listarUsuarios() 
        lista = []
        if resultado is not None:
            for u in resultado:
                usuario = User(id=u[0], username=u[1], correo=u[2], password=u[3])
                lista.append(usuario)
        return lista
    
    def buscarUsuario(self, username):
        daouser = daoUser()
        resultado = daouser.buscarUsuario(User(username=username))
        return User(id=resultado[0], username=resultado[1], correo=resultado[2], password=resultado[3]) if resultado is not None else None
    
    def agregarUsuario(self, username, correo, password):
        daouser = daoUser()
        resultado = daouser.agregarUsuario(User(username=username, correo=correo, password=Encoder().encode(password)))
        return resultado
    
    def eliminarUsuario(self, usuario):
        daouser = daoUser()
        resultado = daouser.eliminarUsuario(usuario)
        return resultado
    
    def actualizarUsuario(self, usuario, opc):
        daouser = daoUser()
        if opc == 5:
            usuario.setPassword(Encoder().encode(usuario.getPassword()))
        resultado = daouser.actualizarUsuario(usuario, opc)
        return resultado

    def validarLogin(self, username, password):
        daouser = daoUser()
        resultado = daouser.validarLogin(User(username=username, password=password))
        return User(id=resultado[0], username=resultado[1], correo=resultado[2], password=resultado[3], rol= resultado[4]) if resultado is not None and Encoder().decode(password, resultado[3]) else None
