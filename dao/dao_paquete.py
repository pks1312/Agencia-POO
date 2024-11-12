from conex import conn
import traceback


class daoPaquete:
    def __init__(self):
        try:
            self.__conn = conn.Conex("localhost", "root", "", "AgenciaTurismo")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.__conn\
    

    def agregarPaquete(self, paquete):
        sql = "insert into paquete (fecha, costo) values (%s, %s)"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (paquete.getFecha(), paquete.getCosto()))
            c.getConex().commit()
            
            # Get the ID of the newly inserted package
            paquete_id = cursor.lastrowid
            
            # Associate the package with destinations
            for destino in paquete.getDestinos():
                sql = "insert into paquete_destino (id_paquete, id_destino) values (%s, %s)"
                cursor.execute(sql, (paquete_id, destino.getId()))
                c.getConex().commit()
                
        except Exception as ex:
            print(traceback.print_exc())
            c.getConex().rollback()
        finally:
            c.closeConex()

    def verPaquetesP1(self):
        sql = "select id, fecha, costo from paquete"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            c.closeConex()
    
    def verPaquetesP2(self):
        sql = "call verPaquetesP2()"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            c.closeConex()

    def buscarPaquete(self, paquete):
        sql = "SELECT p.id, p.fecha, p.costo, d.id, d.nombre, d.descripcion, d.costo FROM paquete p JOIN paquete_destino pd ON p.id = pd.id_paquete JOIN destinos d ON pd.id_destino = d.id WHERE p.id = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (paquete.getId()))
            return cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            c.closeConex()

    def addDestino(self, paquete, destino):
        sql = "insert into paquete_destino (id_paquete, id_destino) values (%s, %s)"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (paquete.getId(), destino.getId()))
            c.getConex().commit()
            
            # Update the cost of the package
            sql = "update paquete set costo = %s where id = %s"
            cursor.execute(sql, (paquete.getCosto(), paquete.getId()))
            c.getConex().commit()
            
        except Exception as ex:
            print(traceback.print_exc())
            c.getConex().rollback()
        finally:
            c.closeConex()    

    def quitarDestino(self, paquete, destino):
        sql = "delete from paquete_destino where id_paquete = %s and id_destino = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (paquete.getId(), destino.getId()))
            c.getConex().commit()
            
            # Update the cost of the package
            sql = "update paquete set costo = %s where id = %s"
            cursor.execute(sql, (paquete.getCosto(), paquete.getId()))
            c.getConex().commit()
            
        except Exception as ex:
            print(traceback.print_exc())
            c.getConex().rollback()
        finally:
            c.closeConex() 
    
    def modificarPaquete(self, paquete):
        sql = "update paquete set fecha = %s, costo = %s where id = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (paquete.getFecha(), paquete.getCosto(), paquete.getId()))
            c.getConex().commit()
        except Exception as ex:
            print(traceback.print_exc())
            c.getConex().rollback()
        finally:
            c.closeConex()

    def eliminarPaquete(self, paquete):  
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            
            # Delete the associations in paquete_destino
            sql = "delete from paquete_destino where id_paquete = %s"
            cursor.execute(sql, (paquete.getId()))
            c.getConex().commit()
            
            # Delete the data in paquete
            sql = "delete from paquete where id = %s"
            cursor.execute(sql, (paquete.getId()))
            c.getConex().commit()
            
        except Exception as ex:
            print(traceback.print_exc())
            c.getConex().rollback()
        finally:
            c.closeConex()