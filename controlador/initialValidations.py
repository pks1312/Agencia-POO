from utils.utilsfunctions import isEmpty
from controlador.destinyValidations import crearDestino, verDestinos, buscarDestino, modificarDestino, eliminarDestino
from controlador.paqueteValidations import crearPaquete, verPaquetes, modificarPaquete, eliminarPaquete
from controlador.profileValidations import inicialPerfil
from controlador.reservasValidations import agendarReserva, verReservas, cancelarReserva
import os
os.system("cls")


from controlador.dto_user import UserDTO
import getpass

def validarLogin():
    username = input("Ingrese nombre de usuario : ")
    password = getpass.getpass("Ingrese contraseña : ")
    resultado = UserDTO().validarLogin(username, password)
    return resultado

def crearCuenta():
    username = input("Ingrese nombre de usuario : ")
    if isEmpty(username): return crearCuenta()
    correo = input("Ingrese correo : ")
    if isEmpty(correo): return crearCuenta()
    password = getpass.getpass("Ingrese contraseña : ")
    if isEmpty(password): return crearCuenta()
    resultado = UserDTO().agregarUsuario(username , correo, password)
    return resultado

def incialUsuario(usuario):
    os.system("cls")
    while True:
        try:
            print (f"Bienvenido {usuario.getUsername()}")
            print("Que Operación desea realizar?")
            print("0. Mi Perfil")
            print("1. Comprar Paquete")
            print("2. Ver mis reservas")
            print("3. Cancelar Reserva")
            print("4. Salir")
            opcion = input("Ingrese opción:")
            if opcion == '0':
                os.system("cls")
                inicialPerfil(usuario)
            elif opcion == '1':
                os.system("cls")
                agendarReserva(usuario)
            elif opcion == '2':
                os.system("cls")
                verReservas(usuario)
            elif opcion == '3':
                os.system("cls")
                cancelarReserva(usuario)
            elif opcion == '4':
                break
        except ValueError:
            print("Debe ingresar un valor numérico")
        except Exception as e:
            print("Error inesperado")
            print(e)



def inicialAdmin(usuario):
    os.system("cls")
    while True:
        try:
            print(f"Bienvenido {usuario.getUsername()}")
            print("Que Operación desea realizar?")
            print("1.-Menu de Destinos")
            print("2.-Menu de Paquetes")
            print("3.-Salir")
            opcion = input("Ingrese opción:")
            if opcion == '1':
                os.system("cls")
                inicialDestino()
            elif opcion == '2':
                os.system("cls")
                inicialPaquete()
            elif opcion == '3':
                break
        except ValueError:
            print("Debe ingresar un valor numérico")
        except Exception as e:
            print("Error inesperado")
            print(e)


def inicialDestino():
    os.system("cls")
    while True:
        try:
            print("Que Operación desea realizar?")
            print("1. Crear Destino")
            print("2. Ver Destinos")
            print("3. Buscar Destino")
            print("4. Modificar Destino")
            print("5. Eliminar Destino")
            print("6. Volver al menu principal")
            print("7. Salir")
            opcion = input("Ingrese opción:")
            os.system("cls")
            if opcion == '1':
                crearDestino()
            elif opcion == '2':
                verDestinos()
            elif opcion == '3':
                buscarDestino()
            elif opcion == '4':
                modificarDestino()
            elif opcion == '5':
                eliminarDestino()
            elif opcion == '6':
                inicialAdmin()
            elif opcion == '7':
                break
        except ValueError:
            print("Debe ingresar un valor numérico")
        except Exception as e:
            print("Error inesperado")
            print(e)
def inicialPaquete():
    while True:
        try:
            print("Que Operación desea realizar?")
            print("1. Crear Paquete")
            print("2. Ver Paquetes")
            print("3. Modificar Paquete")
            print("4. Eliminar Paquete")
            print("5. Volver al menu principal")
            print("6. Salir")
            opcion = input("Ingrese opción:")
            os.system("cls")    
            if opcion == '1':
                crearPaquete()
            elif opcion == '2':
                verPaquetes()
            elif opcion == '3':
                modificarPaquete()
            elif opcion == '4':
                eliminarPaquete()
            elif opcion == '5':
                inicialAdmin()
            elif opcion == '6':
                break
        except ValueError:
            print("Debe ingresar un valor numérico")
        except Exception as e:
            print("Error inesperado")
        print(e)