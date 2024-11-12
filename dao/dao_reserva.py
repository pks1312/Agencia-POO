from conex import conn
import traceback

class daoReserva:
    
    def __init__(self):
        try:
            self.__conn = conn.Conex("localhost", "root", "", "AgenciaTurismo")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.__conn
    
    def agendarReserva(self, paquete, usuario, cantidad):
        sql = "INSERT INTO reserva (id_paquete, id_usuario, acompanantes) VALUES (%s, %s, %s)"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            try:
                cursor.execute(sql, (paquete.getId(), usuario.getId(), cantidad))
                c.getConex().commit()
                return True
            except Exception as ex:
                print(ex)
                c.getConex().rollback()
            finally:
                c.closeConex()
            c.getConex().commit()
        except Exception as ex:
            print(ex)
            c.getConex().rollback()
        finally:
            c.closeConex()
        return True
    
    def verReservas(self, usuario):
        sql = "select id, id_paquete, acompanantes from reserva where id_usuario = %s"
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (usuario.getId()))
            result = cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            c.closeConex()
        return result
    
    def eliminarReserva(self, id):
        sql = "delete from reserva where id = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (id))
            c.getConex().commit()
            return True
        except Exception as ex:
            print(ex)
            c.getConex().rollback()
        finally:
            c.closeConex()
        return True
    
    def buscarReserva(self, id):
        sql = "select id_paquete, acompanantes from reserva where id = %s"
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (id))
            result = cursor.fetchone()
        except Exception as ex:
            print(ex)
        finally:
            c.closeConex()
        return result