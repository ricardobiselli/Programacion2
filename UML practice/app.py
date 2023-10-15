import os
from estudiante import *
from datospersonales import *


def menu():
    print("|--------------------------------------|")
    print("|1 - Ingresar cómo alumno              |")
    print("|2 - Ingresar cómo profesor            |")
    print("|3 - Ver cursos                        |")
    print("|4 - Salir                             |")
    print("|--------------------------------------|\n")


print("Bienvenido!")
respuesta = ""

while respuesta != "salir":
    menu()
    opt = input("Ingrese la opción de menú: ")

    if opt.isnumeric():
        opt = int(opt)
        if opt == 1:
            #resultado = estudiante.validar_credenciales(alumnos)

            
            resultado = estudiante.validar_credenciales(alumnos, "1@gmail.com", "123123")

            
          

            if resultado:
                print("Access granted!")
            else:
                print("Access denied.")
        elif opt == 2:
            pass            
        elif opt == 3:
            pass           
        elif opt == 4:
            os.system("clear")  # cambiar a cls para windows
            print("Saliendo del programa.")
            respuesta = "salir"
        else:
            print("No ha ingresado una opción válida")
    else:
        print("Ingrese una opción numérica")
