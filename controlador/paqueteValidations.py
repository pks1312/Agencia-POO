from controlador.destinoDTO import DestinoDTO   
from controlador.paquete_dto import PaqueteDTO
from utils.utilsfunctions import isEmpty
import os
os.system("cls")

def crearPaquete():
    while True:
        try:
            print("Creación de Paquete")
            nombre = input("Ingrese destino del paquete : ")
            if isEmpty(nombre): return crearPaquete()
            destino = DestinoDTO().BuscarDestino(nombre)
            if destino is None:
                print("El destino no existe")
                return crearPaquete()
            costoTotal = destino.getCosto()
            destinos = []
            destinos.append(destino)
            while len(destinos) < 5:
                opcion = input("Desea agregar otro destino al paquete? (s/n) : ")
                if opcion == 's':
                    nombre = input("Ingrese destino del paquete : ")
                    if isEmpty(nombre): return crearPaquete()
                    destino = DestinoDTO().BuscarDestino(nombre)
                    if destino is None:
                        print("El destino no existe")
                        return crearPaquete()
                    costoTotal += destino.getCosto()
                    destinos.append(destino)
                else:
                    break
            if len(destinos) < 2:
                print("Debe agregar al menos 2 destinos al paquete")
                return crearPaquete()
            
            print("Ingrese Fecha de inicio del paquete")
            dia = input("Ingrese día (0-31): ")
            mes = input("Ingrese mes (1-12): ")
            anio = input("Ingrese año (2024 en adelante): ")

            if not dia.isdigit() or not mes.isdigit() or not anio.isdigit():
                print("Debe ingresar valores numéricos")
                return crearPaquete()

            dia = int(dia)
            mes = int(mes)
            anio = int(anio)

            if dia < 0 or dia > 31 or mes < 1 or mes > 12 or anio < 2024:
                print("Fecha inválida")
                return crearPaquete()

            fechaInicio = f"{anio}-{mes}-{dia}"
            
            resultado = PaqueteDTO().agregarPaquete(destinos, fechaInicio, costoTotal)
            return resultado
        except ValueError:
            print("Debe ingresar un valor numérico")
        except Exception as e:
            print("Error inesperado")
            print(e)

def verPaquetes():
    try:
        paquetes = PaqueteDTO().verPaquetes()
        if paquetes is None:
            print("No hay paquetes registrados")
        else:
            for paquete in paquetes:
                print("Hola")
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


def modificarPaquete():
    try:
        print("Modificación de Paquete")
        id = input("Ingrese id del paquete a modificar: ")
        if not id.isdigit():
            print("Debe ingresar un valor numérico")
            return modificarPaquete()
        paquete = PaqueteDTO().buscarPaquete(id)
        if paquete is None:
            print("El paquete no existe")
            return modificarPaquete()
        
        print("Paquete a modificar:")
        print(f"Fecha de inicio: {paquete.getFecha()}")
        print(f"Costo total: {paquete.getCosto()}")
        print("Destinos:")
        for destino in paquete.getDestinos():
            print(f"Nombre: {destino.getNombre()}")
            print(f"Descripción: {destino.getDescripcion()}")
            print("--------------------------------------------------")
        
        while True:
            opcion = input("¿Qué desea hacer?\n1. Agregar destino\n2. Quitar destino\n3. Cambiar fecha\n4. Salir\nIngrese el número de la opción: ")

            if opcion == '1':
                nombre = input("Ingrese destino del paquete : ")
                if isEmpty(nombre):
                    print("El nombre del destino no puede estar vacío")
                    continue
                destino = DestinoDTO().BuscarDestino(nombre)
                if destino is None:
                    print("El destino no existe")
                    continue
                costoDestino = destino.getCosto()
                paquete.addDestino(destino)
                paquete.actualizarCosto(costoDestino)
                print("Destino agregado al paquete")
                PaqueteDTO().addDestino(paquete, destino)

            elif opcion == '2':
                nombre = input("Ingrese destino a quitar del paquete : ")
                if isEmpty(nombre):
                    print("El nombre del destino no puede estar vacío")
                    continue
                destino = DestinoDTO().BuscarDestino(nombre)
                if destino is None:
                    print("El destino no existe")
                    continue
                costoDestino = destino.getCosto()
                paquete.actualizarCosto(-costoDestino)
                if PaqueteDTO().quitarDestino(paquete, destino) is True:
                    print("Destino quitado del paquete")
                else:
                    print("El destino no está en el paquete")   

            elif opcion == '3':
                dia = input("Ingrese día (0-31): ")
                mes = input("Ingrese mes (1-12): ")
                anio = input("Ingrese año (2024 en adelante): ")

                if not dia.isdigit() or not mes.isdigit() or not anio.isdigit():
                    print("Debe ingresar valores numéricos")
                    continue

                dia = int(dia)
                mes = int(mes)
                anio = int(anio)

                if dia < 0 or dia > 31 or mes < 1 or mes > 12 or anio < 2024:
                    print("Fecha inválida")
                    continue

                fechaInicio = f"{anio}-{mes}-{dia}"
                paquete.setFecha(fechaInicio)
                PaqueteDTO().modificarPaquete(paquete)
                print("Fecha de inicio del paquete modificada")
            elif opcion == '4':
                break
            else:
                print("Opción inválida")

    except ValueError:
        print("Debe ingresar un valor numérico")
    except Exception as e:
        print("Error inesperado")
        print(e)

def eliminarPaquete():
    try:
        print("Eliminación de Paquete")
        id = input("Ingrese id del paquete a eliminar: ")
        if not id.isdigit():
            print("Debe ingresar un valor numérico")
            return eliminarPaquete()
        paquete = PaqueteDTO().buscarPaquete(id)
        if paquete is None:
            print("El paquete no existe")
            return eliminarPaquete()
        
        print("Paquete a eliminar:")
        print(f"Fecha de inicio: {paquete.getFecha()}")
        print(f"Costo total: {paquete.getCosto()}")
        print("Destinos:")
        for destino in paquete.getDestinos():
            print(f"Nombre: {destino.getNombre()}")
            print(f"Descripción: {destino.getDescripcion()}")
            print("--------------------------------------------------")
        
        opcion = input("¿Está seguro que desea eliminar el paquete? (s/n): ")
        if opcion.lower() == 's':
            if PaqueteDTO().eliminarPaquete(paquete) is True:
                print("Paquete eliminado")
            else:
                print("No se pudo eliminar el paquete")
        else:
            print("Operación cancelada")
    except ValueError:
        print("Debe ingresar un valor numérico")
    except Exception as e:
        print("Error inesperado")
        print(e)