from conex import conn
import traceback

class daoDestino:
    def __init__(self):
        try:
            self.__conn = conn.Conex("localhost", "root", "", "AgenciaTurismo")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.__conn
    
    def insertarDestino(self, destino):
        sql = "insert into destinos (nombre, descripcion, costo) values (%s, %s, %s)"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (destino.getNombre(), destino.getDescripcion(), destino.getCosto()))
            c.getConex().commit()
        except Exception as ex:
            print(traceback.print_exc())
            c.getConex().rollback()
        finally:
            c.closeConex()

    def listarDestinos(self):
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute("select id, nombre, descripcion, costo from destinos")
            result = cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            c.closeConex()

        return result
    
    def BuscarDestino(self, nombre):
        sql = "select id, nombre, descripcion, costo from destinos where lower(nombre) = %s"
        resultado = None
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (nombre.lower()))
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
            c.getConex.rollback()
        finally:
            c.closeConex()
        return resultado

    def eliminarDestino(self, nombre):
        
        sql = "delete from destinos where lower(nombre) = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (nombre.lower()))
            c.getConex().commit()
        except Exception as ex:
            print(traceback.print_exc())
            c.getConex().rollback()
        finally:
            c.closeConex()

    def modificarDestino(self, destino):
        sql = "update destinos set nombre = %s, descripcion = %s, costo = %s where lower(nombre) = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (destino.getNombre(), destino.getDescripcion(), destino.getCosto(), destino.getNombre().lower()))
            c.getConex().commit()
        except Exception as ex:
            print(traceback.print_exc())
            c.getConex().rollback()
        finally:
            c.closeConex()
        