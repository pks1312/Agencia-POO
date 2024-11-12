from dao.dao_paquete import daoPaquete
from modelo.paquete import Paquete
from modelo.destino import Destino


class PaqueteDTO:
    def agregarPaquete(self, destinos, fechaInicio, costoTotal):
        daopaquete = daoPaquete()
        daopaquete.agregarPaquete(Paquete(destinos=destinos, fecha=fechaInicio, costo=costoTotal))
        return True
    
    def verPaquetes(self):

        resuP = daoPaquete().verPaquetesP1()
        resuD = daoPaquete().verPaquetesP2()

        paquetes = []

        for r in resuP:
            paquete = Paquete(id=r[0], fecha=r[1], costo=r[2])
            paquetes.append(paquete)
        for r in resuD:
            for p in paquetes:
                if p.getId() == r[0]:
                    destino = Destino(id=r[1], nombre=r[2], descripcion=r[3], costo=r[4])
                    if not p.destinoExists(destino):  # Check if the destination already exists in the package
                        p.addDestino(destino)

        return paquetes
    
    def buscarPaquete(self, id):
        daopaquete = daoPaquete()
        resu = daopaquete.buscarPaquete(Paquete(id=id))
        paquete = None
        for r in resu:
            if paquete is None:
                paquete = Paquete(id=r[0], fecha=r[1], costo=r[2])
            if paquete.getId() == r[0]:
                destino = Destino(id=r[3], nombre=r[4], descripcion=r[5], costo=r[6])
                if not paquete.destinoExists(destino):  # Check if the destination already exists in the package
                    paquete.addDestino(destino)
        return paquete
    
    def addDestino(self, paquete, destino):
        daopaquete = daoPaquete()
        daopaquete.addDestino(paquete, destino)
        return True
    
    def quitarDestino(self, paquete, destino):
        daopaquete = daoPaquete()
        daopaquete.quitarDestino(paquete, destino)
        return True
    
    def modificarPaquete(self, paquete):
        daopaquete = daoPaquete()
        daopaquete.modificarPaquete(paquete)
        return True

    def eliminarPaquete(self, paquete):
        daopaquete = daoPaquete()
        daopaquete.eliminarPaquete(paquete)
        return True

