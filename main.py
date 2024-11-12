from controlador.initialValidations import validarLogin, crearCuenta, inicialAdmin, incialUsuario
import os
os.system("cls")

def menuAccesoUsuarios():
    print("""
||------------------------||
||  Bienvenido al Sistema ||
||------------------------||
||1. Login de acceso      ||
||2. Crear cuenta usuario ||
||3. Salir                ||
||------------------------||
""")
   
print("\n=== Aplicación Usuarios ===\n")
while True:
    menuAccesoUsuarios()
    opc = input("Ingrese opción:")
    if opc == '1':
        ##### login
        intentos = 1
        while intentos <= 3:
            try:
                resu = validarLogin()
                if resu is not None:
                    print(f"Bienvenido(a) Sr(a). : {resu.getUsername()}")
                    if resu.getRol() >= 2:
                        inicialAdmin(resu)
                    else:
                        incialUsuario(resu)
                    break
                else:
                    print("Usuario o contraseña incorrecta")
                    intentos += 1
            except(Exception) as e:
                print(e)
                print("intentar nuevamente")
        if intentos == 4:
            print("Ha superado el número de intentos permitidos")
    elif opc == '2':
        resu = crearCuenta()
        if resu is not None:
            print("Usuario creado con éxito")
            print("Espere a que el administrador habilite su cuenta")
            print("Gracias por utilizar el sistema")

    elif opc == '3':
        print("Gracias por utilizar el sistema")
        break
    else:
        print("Opción no válida")