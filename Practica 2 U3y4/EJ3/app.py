from datos import *


def menu():
    print("----------------------------------------")
    print("|1 - Reservar turno paciente           |")
    print("|2 - Cancelar turno paciente           |")
    print("|3 - Ingresar paciente                 |")
    print("----------------------------------------\n")


print("---------------")
print("| BIENVENIDO! |")
print("---------------\n")
respuesta = ""
while respuesta != "salir":
    menu()
    opt = input("Ingrese la opción de menú: ")

    if opt.isnumeric():
        opt = int(opt)
        if opt == 1:
           for n in especialidades:
               print(n)

        elif opt == 2:
            pass
        elif opt == 3:
            pass
      
        else:
            print("----------------------------------------")
            print("| No ha ingresado una opción válida... |")
            print("----------------------------------------\n")
    else:
        print("----------------------------------")
        print("| Ingrese una opción numérica... |")
        print("----------------------------------\n")