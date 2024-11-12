from dao.dao_profile import daoProfile
from modelo.informacionpersonal import InformacionPersonal

class ProfileDTO:
    def buscarPerfil(self, usuario):
        daoprofile = daoProfile()
        perfil = daoprofile.buscarPerfil(usuario)
        if perfil is None:
            return None
        return InformacionPersonal(perfil[0], perfil[1], perfil[2], perfil[3], perfil[4], perfil[5], usuario.getId(), usuario.getUsername(), usuario.getPassword(), usuario.getCorreo(), usuario.getRol())
    
    def crearPerfil(self, usuario, nombre, apellido, telefono, fechaNacimiento, genero, direccion):
        daoprofile = daoProfile()
        return daoprofile.crearPerfil(InformacionPersonal(nombre, apellido, genero, direccion, telefono, fechaNacimiento, 
                                                   usuario.getId(), usuario.getUsername(), usuario.getPassword(), usuario.getCorreo(),
                                                     usuario.getRol()))
    
    def actualizarPerfil(self, InformacionPersonal):
        daoprofile = daoProfile()
        return daoprofile.actualizarPerfil(InformacionPersonal)
        