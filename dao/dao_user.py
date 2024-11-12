from conex import conn
import traceback

class daoUser:

    def __init__(self):
        try:
            self.__conn = conn.Conex("localhost", "root", "", "AgenciaTurismo")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.__conn
    
    def validarLogin(self, user):
        sql = "select id, username, correo, password, rol from usuario where lower(username) = %s"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (user.getUsername()))
            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            c.closeConex()
        
        return resultado    

    def listarUsuarios(self):
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute("select id, username, correo from usuario")
            result = cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            c.closeConex()

        return result
    

    def buscarUsuario(self, user):
        sql = "select id, username, correo from usuario where lower(username) = %s"
        resultado = None
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (user.getUsername().lower()))
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
            c.getConex.rollback()
        finally:
            c.closeConex()
        return resultado

    def agregarUsuario(self, user):
        sql = "insert into usuario (username, correo, password, rol) values (%s, %s, %s, %s)"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (user.getUsername(), user.getCorreo(), user.getPassword(), 1))
            c.getConex().commit()
            return "Usuario agregado"
        except Exception as ex:
            print(ex)
            c.getConex().rollback()
            return "Error al agregar usuario"
        finally:
            c.closeConex()

    def eliminarUsuario(self, user):
        sql = "delete from usuario where id = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, user.getId())
            c.getConex().commit()
            return "Usuario eliminado"
        except Exception as ex:
            print(ex)
            c.getConex().rollback()
            return "Error al eliminar usuario"
        finally:
            c.closeConex()

    def actualizarUsuario(self, user, opc):
        columnas = {1: "username", 2: "correo", 3: "password", 4: "rol"}
        columna = columnas[opc]
        sql = "update usuario set {} = %s where id = %s".format(columna)
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (user.getAttribute(columna), user.getId()))
            c.getConex().commit()
            return "Usuario actualizado"
        except Exception as ex:
            print(ex)
            c.getConex().rollback()
            return "Error al actualizar usuario"
        finally:
            c.closeConex()
