from controlador.dto_profile import ProfileDTO
from utils.utilsfunctions import isEmpty
import os
os.system("cls")

def inicialPerfil(usuario):
    while True:
        try:
            perfil = ProfileDTO().buscarPerfil(usuario)
            if perfil is None:
                print("No tienes un Perfil creado")
                print("Desea crear un Perfil?")
                print("1. Si")
                print("2. No")
                opcion = input("Ingrese opción:")
                if opcion == '1':
                    crearPerfil(usuario)
                else:
                    break
                return
            else:
                print("Mi Perfil")
                print(f"Nombre : {perfil.getNombre()}")
                print(f"Apellido : {perfil.getApellido()}")
                print(f"Teléfono : {perfil.getTelefono()}")
                print(f"Fecha de Nacimiento : {perfil.getFechaNacimiento()}")
                print(f"Género : {perfil.getGenero()}")
                print(f"Dirección : {perfil.getDireccion()}")
                print("Que Operación desea realizar?")
                print("1. Actualizar Perfil")
                print("2. Salir")
                opcion = input("Ingrese opción:")
                if opcion == '1':
                    actualizarPerfil(perfil)
                elif opcion == '2':
                    break
        except ValueError:
            print("Debe ingresar un valor numérico")
        except Exception as e:
            print("Error inesperado")
            print(e)
            break

def crearPerfil(usuario):
    print("Creación de Perfil")
    nombre = input("Nombre : ")
    if isEmpty(nombre):
        print("El nombre no puede estar vacío")
        return
    apellido = input("Apellido : ")
    if isEmpty(apellido):
        print("El apellido no puede estar vacío")
        return
    telefono = input("Teléfono : ")
    if isEmpty(telefono):
        print("El teléfono no puede estar vacío")
        return
    fechaNacimiento = input("Fecha de Nacimiento (YYYY-MM-DD) : ")
    if isEmpty(fechaNacimiento):
        print("La fecha de nacimiento no puede estar vacía")
        return
    genero = input("Género (M/F) : ")
    if isEmpty(genero):
        print("El género no puede estar vacío")
        return
    direccion = input("Dirección : ")
    if isEmpty(direccion):
        print("La dirección no puede estar vacía")
        return
    ProfileDTO().crearPerfil(usuario, nombre, apellido, telefono, fechaNacimiento, genero, direccion)
    print("Perfil creado")

def actualizarPerfil(perfil):
    print("Actualización de Perfil")
    print("Que datos desea actualizar?")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Teléfono")
    print("4. Fecha de Nacimiento")
    print("5. Género")
    print("6. Dirección")
    print("7. Salir")
    opcion = input("Ingrese opción:")
    if opcion == '1':
        nombre = input("Nombre : ")
        if isEmpty(nombre):
            print("El nombre no puede estar vacío")
        perfil.setNombre(nombre)
    elif opcion == '2':
        apellido = input("Apellido : ")
        if isEmpty(apellido):
            print("El apellido no puede estar vacío")
            return
        perfil.setApellido(apellido)
    elif opcion == '3':
        telefono = input("Teléfono : ")
        if isEmpty(telefono):
            print("El teléfono no puede estar vacío")
            return
        perfil.setTelefono(telefono)
    elif opcion == '4':
        fechaNacimiento = input("Fecha de Nacimiento (YYYY-MM-DD) : ")
        if isEmpty(fechaNacimiento):
            print("La fecha de nacimiento no puede estar vacía")
            return
        perfil.setFechaNacimiento(fechaNacimiento)
    elif opcion == '5':
        genero = input("Género (M/F) : ")
        if isEmpty(genero):
            print("El género no puede estar vacío")
            return
        perfil.setGenero(genero)
    elif opcion == '6':
        direccion = input("Dirección : ")
        if isEmpty(direccion):
            print("La dirección no puede estar vacía")
            return
        perfil.setDireccion(direccion)
    elif opcion == '7':
        return
    ProfileDTO().actualizarPerfil(perfil)
    print("Perfil actualizado")