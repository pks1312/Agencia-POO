from dao.dao_reserva import daoReserva
from controlador.paquete_dto import PaqueteDTO
from modelo.reserva import Reserva

class ReservaDTO:
    def agendarReserva(self, paquete, usuario, cantidad):
        daoreserva = daoReserva()
        return daoreserva.agendarReserva(paquete, usuario, cantidad)
    
    def verReservas(self, usuario):
        daoreserva = daoReserva()
        reservas = []
        resu = daoreserva.verReservas(usuario)
        for res in resu:
            resul = PaqueteDTO().buscarPaquete(res[1])
            reserva = Reserva(id=res[0], paquete=resul, usuario=usuario, acompanantes=res[2])
            reservas.append(reserva)
        return reservas
    
    def buscarReserva(self, id, usuario):
        daoreserva = daoReserva()
        resu = daoreserva.buscarReserva(id)
        paquete = PaqueteDTO().buscarPaquete(resu[1])
        return Reserva(id=id, paquete=paquete, usuario=usuario, acompanantes=resu[2])
    
    
    def eliminarReserva(self, id):
        daoreserva = daoReserva()
        return daoreserva.eliminarReserva(id)

    
