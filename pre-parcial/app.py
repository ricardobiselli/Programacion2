import os
from liquidaciones import *

def menu():
    print("|--------------------------------------|")
    print("|1 - nuevo empleado                    |")
    print("|2 - sumar falta empleado              |")
    print("|3 - liquidar salarios                 |")
    print("|4 - salir                             |")
    print("|--------------------------------------|\n")


print("|-------------Bienvenido!--------------|\n")

opt = ""

while opt != "4":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system("cls")
    if opt.isnumeric():
        if int(opt) == 1:
            def registrar_nuevo_empleado():
                nombre = input("ingrese el nombre: ")
                pagaxhora = int(input("ingrese la paga $/hora: "))
                     
                nuevo_empleado = {
                "nombre": nombre,
                "paga_por_hora": pagaxhora,
                "faltas": 0,
                }
                
                empleados.append(nuevo_empleado)
                return None
    
            registrar_nuevo_empleado()
            
            """borrar
            print("--------------------------------------------")
            print("bucle temporal para chequear modificaciones")
            for empleado in empleados:
                print(empleado)
            print("--------------------------------------------") """
            
        elif int(opt) == 2:
            def sumar_falta_empleado():
                nombre = input("Ingrese el nombre del empleado para sumar falta: ")
                encontrado = False

                for elementos in empleados:
                    if nombre == elementos["nombre"]:
                        cargar_falta = int(input("Ingrese la cantidad de faltas a sumar: "))
                        elementos["faltas"] =  elementos["faltas"] + cargar_falta
                        encontrado = True
                        print(f"Se cargaron {cargar_falta} faltas para el empleado {nombre}.")
                        """borrar
                        print("--------------------------------------------")
                        print("bucle temporal para chequear modificaciones")
                        for empleado in empleados:
                            print(empleado)
                        print("--------------------------------------------")"""

                if not encontrado:
                    os.system("cls")
                    print(f"No se encontró al empleado con el nombre '{nombre}' en la lista de empleados.")

            sumar_falta_empleado()  
              
        elif int(opt) == 3:
            liquidacion_sueldo()
print("Hasta luego...")
            
                
                    