from conex import conn
import traceback

class daoProfile:
    def __init__(self):
        try:
            self.__conn = conn.Conex("localhost", "root", "", "AgenciaTurismo")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.__conn
    
    def crearPerfil(self, perfil):
        sql = "insert into informacionpersonal (nombre, apellido, genero, direccion, telefono, fechaNacimiento, id_usuario) values (%s, %s, %s, %s, %s, %s, %s)"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (perfil.getNombre(), perfil.getApellido(), perfil.getGenero(), perfil.getDireccion(), perfil.getTelefono(), perfil.getFechaNacimiento(), perfil.getId()))
            c.getConex().commit()
        except Exception as ex:
            print(traceback.print_exc())
            c.getConex().rollback()
        finally:
            c.closeConex()

    def buscarPerfil(self, usuario):
        sql = "select nombre, apellido, genero, direccion, telefono, fechaNacimiento from informacionpersonal where id_usuario = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (usuario.getId()))
            perfil = cursor.fetchone()
            return perfil
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            c.closeConex()

    def actualizarPerfil(self, perfil):
        sql = "update informacionpersonal set nombre = %s, apellido = %s, genero = %s, direccion = %s, telefono = %s, fechaNacimiento = %s where id_usuario = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (perfil.getNombre(), perfil.getApellido(), perfil.getGenero(), perfil.getDireccion(), perfil.getTelefono(), perfil.getFechaNacimiento(), perfil.getId()))
            c.getConex().commit()
        except Exception as ex:
            print(traceback.print_exc())
            c.getConex().rollback()
        finally:
            c.closeConex()