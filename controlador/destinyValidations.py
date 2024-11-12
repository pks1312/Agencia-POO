from controlador.destinoDTO import DestinoDTO
from utils.utilsfunctions import isEmpty

def crearDestino():
    nombre = input("Ingrese nombre del destino : ")
    if isEmpty(nombre): return crearDestino()
    # resu = DestinoDTO().BuscarDestino(nombre)
    # if resu is not None:
    #     print("El destino ya existe")
    #     return crearDestino()
    
    descripcion = input("Ingrese descripción del destino : ")
    if isEmpty(descripcion): return crearDestino()
    precio = input("Ingrese precio del destino : ")
    if isEmpty(precio): return crearDestino()
    resultado = DestinoDTO().agregarDestino(nombre, descripcion, precio)
    return resultado

def verDestinos():
    resu = DestinoDTO().listarDestinos()
    if resu is not None:
        for destino in resu:
            print(f"Nombre : {destino.getNombre()}")
            print(f"Descripción : {destino.getDescripcion()}")
            print(f"Precio : {destino.getCosto()}")
            print("=====================================")
    else:
        print("No hay destinos registrados")
    return resu

def buscarDestino():
    print("Ingresa el destino que deseas buscar:")
    nombre = input("Ingrese nombre del destino : ")
    if isEmpty(nombre): return buscarDestino()
    resu = DestinoDTO().BuscarDestino(nombre)
    if resu is not None:
        print(f"Nombre : {resu.getNombre()}")
        print(f"Descripción : {resu.getDescripcion()}")
        print(f"Precio : {resu.getCosto()}")
        print("=====================================")
    else:
        print("No se encontró el destino")

def eliminarDestino():
    print("Ingresa el destino que deseas eliminar:")
    nombre = input("Ingrese nombre del destino : ")
    if isEmpty(nombre): return eliminarDestino()
    resu = DestinoDTO().BuscarDestino(nombre)
    if resu is not None:
        print(f"Nombre : {resu.getNombre()}")
        print(f"Descripción : {resu.getDescripcion()}")
        print(f"Precio : {resu.getCosto()}")
        print("=====================================")
        opcion = input("¿Estás seguro que deseas eliminar este destino? (s/n) : ")
        if opcion == 's':
            DestinoDTO().eliminarDestino(resu.getNombre())
            print("Destino eliminado")
        else:
            print("Operación cancelada")
    else:
        print("No se encontró el destino")

def modificarDestino():
    print("Ingresa el destino que deseas modificar:")
    nombre = input("Ingrese nombre del destino : ")
    if isEmpty(nombre): return modificarDestino()
    resu = DestinoDTO().BuscarDestino(nombre)
    if resu is not None:
        print(f"Nombre : {resu.getNombre()}")
        print(f"Descripción : {resu.getDescripcion()}")
        print(f"Precio : {resu.getCosto()}")
        print("=====================================")
        print("¿Qué deseas modificar?")
        print("1. Nombre")
        print("2. Descripción")
        print("3. Precio")
        opcion = input("Ingrese opción : ")
        if opcion == '1':
            nombre = input("Ingrese nuevo nombre del destino : ")
            if isEmpty(nombre): return modificarDestino()
            resu.setNombre(nombre)
        elif opcion == '2':
            descripcion = input("Ingrese nueva descripción del destino : ")
            if isEmpty(descripcion): return modificarDestino()
            resu.setDescripcion(descripcion)
        elif opcion == '3':
            precio = input("Ingrese nuevo precio del destino : ")
            if isEmpty(precio): return modificarDestino()
            resu.setCosto(precio)
        DestinoDTO().modificarDestino(resu)
        print("Destino modificado")
    else:
        print("No se encontró el destino")