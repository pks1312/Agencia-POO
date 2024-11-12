from controlador.dto_reserva import ReservaDTO
from controlador.paquete_dto import PaqueteDTO
import os
os.system("cls")

def agendarReserva(usuario):
    try:
        paquetes = PaqueteDTO().verPaquetes()
        print("Paquetes Disponibles")
        for paquete in paquetes:
            print(f"Paquete: {paquete.getId()}")
            print(f"Fecha de inicio: {paquete.getFecha()}")
            print(f"Costo total: {paquete.getCosto()}")
            print("Destinos:")
            print("--------------------------------------------------")
            for destino in paquete.getDestinos():
                print(f"Nombre: {destino.getNombre()}")
                print(f"Descripción: {destino.getDescripcion()}")
                print("--------------------------------------------------")
        
        id = input("Ingrese id del paquete a reservar: ")
        if not id.isdigit():
            print("Debe ingresar un valor numérico")
            return agendarReserva(usuario)
        
        paquete = PaqueteDTO().buscarPaquete(id)
        if paquete is None:
            print("El paquete no existe")
            return agendarReserva(usuario)
        
        print("Paquete a reservar:")
        print(f"Fecha de inicio: {paquete.getFecha()}")
        print(f"Costo total: {paquete.getCosto()}")
        print("Destinos:")
        for destino in paquete.getDestinos():
            print(f"Nombre: {destino.getNombre()}")
            print(f"Descripción: {destino.getDescripcion()}")
            print("--------------------------------------------------")

        print("Ingrese la cantidad de personas")
        cantidad = input("Ingrese cantidad de personas: ")
        if not cantidad.isdigit():
            print("Debe ingresar un valor numérico")
            return agendarReserva(usuario)
        
        if ReservaDTO().agendarReserva(paquete, usuario, cantidad):
            print("Reserva realizada con éxito")
    except ValueError:
        print("Debe ingresar un valor numérico")
    except Exception as e:
        print("Error inesperado")
        print(e)
    finally:
        # Close any open resources here
        pass

def verReservas(usuario):
    try:
        reservas = ReservaDTO().verReservas(usuario)
        if len(reservas) == 0:
            print("No tiene reservas")
        else:
            for reserva in reservas:
                paquete = reserva.getPaquete()
                print(f"ID Reserva: {reserva.getId()}")
                print(f"Paquete: {paquete.getId()}")
                print(f"Fecha de inicio: {paquete.getFecha()}")
                print(f"Costo total: {paquete.getCosto()}")
                print("Destinos:")
                for destino in paquete.getDestinos():
                    print(f"Nombre: {destino.getNombre()}")
                    print(f"Descripción: {destino.getDescripcion()}")
                    print("--------------------------------------------------")
    except Exception as e:
        print("Error inesperado")
        print(e)
    finally:
        # Close any open resources here
        pass
    
def cancelarReserva(usuario):
    try:
        reservas = ReservaDTO().verReservas(usuario)
        if len(reservas) == 0:
            print("No tiene reservas")
        else:
            print("Reservas:")
            for reserva in reservas:
                paquete = reserva.getPaquete()
                print(f"ID Reserva: {reserva.getId()}")
                print(f"Paquete: {paquete.getId()}")
                print(f"Fecha de inicio: {paquete.getFecha()}")
                print(f"Costo total: {paquete.getCosto()}")
                print("Destinos:")
                for destino in paquete.getDestinos():
                    print(f"Nombre: {destino.getNombre()}")
                    print(f"Descripción: {destino.getDescripcion()}")
                    print("--------------------------------------------------")
            
            id = input("Ingrese id de la reserva a cancelar: ")
            if not id.isdigit():
                print("Debe ingresar un valor numérico")
                return cancelarReserva(usuario)
            
            reserva = ReservaDTO().buscarReserva(id, usuario)
            if reserva is None:
                print("La reserva no existe")
                return cancelarReserva(usuario)
            
            if ReservaDTO().cancelarReserva(id):
                print("Reserva cancelada con éxito")
    except ValueError:
        print("Debe ingresar un valor numérico")
    except Exception as e:
        print("Error inesperado")
        print(e)
    finally:
        # Close any open resources here
        pass


