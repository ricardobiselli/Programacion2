from usuario import *
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
            def validar_ingreso():
                mail_ingresado = input("Ingrese el mail con el que se registró: ")
                for alumno in alumnos:
                    if mail_ingresado == alumno["email"]:
                        print("YES!")
                        break  
                    else:
                        print("El correo no coincide con ningún alumno registrado.")
            validar_ingreso()
        elif opt == 2:
            pass
        elif opt == 3:
            pass
        elif opt == 4:
            print("Saliendo del programa.")
            repuesta = "salir"
        else:
            print("No ha ingresado una opción válida")
    else:
        print("Ingrese una opción numérica")
