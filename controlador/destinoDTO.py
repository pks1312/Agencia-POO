from dao.dao_destino import daoDestino
from modelo.destino import Destino

class DestinoDTO:
    def agregarDestino(self, nombre, descripcion, precio):
        daodestino = daoDestino()
        daodestino.insertarDestino(Destino(nombre, descripcion, precio))
        return True
    
    def listarDestinos(self):
        daodestino = daoDestino()
        resultado = daodestino.listarDestinos()
        lista = []
        if resultado is not None:
            for d in resultado:
                destino = Destino(id=d[0], nombre=d[1], descripcion=d[2], costo=d[3])
                lista.append(destino)
        return lista
    
    def BuscarDestino(self, nombre):
        daodestino = daoDestino()
        resultado = daodestino.BuscarDestino(nombre)
        return Destino(id=resultado[0], nombre=resultado[1], descripcion=resultado[2], costo=resultado[3]) if resultado is not None else None
    
    def eliminarDestino(self, nombre):
        daodestino = daoDestino()
        daodestino.eliminarDestino(nombre)
        return True
    
    def modificarDestino(self, destino):
        daodestino = daoDestino()
        daodestino.modificarDestino(destino)
        return True