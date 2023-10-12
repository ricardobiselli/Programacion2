import os
from abc import ABC, abstractmethod


"""

    Al ingresar al sistema se debe mostrar un menú en bucle con las siguiente opciones:
1. Ingresar cómo alumno
2. Ingresar cómo profesor
3. Ver cursos
4. Salir
    """
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
    opt = input("\n Ingrese la opción de menú: ")
    os.system("cls")
    if opt.isnumeric():
        if int(opt) == 1:
            pass
        elif int(opt) == 2:
            pass
        elif int(opt) == 3:
            pass
        elif int(opt) == 4:
            pass
        else:
            print("no ha ingresando una opción válida")
    else:
        print("Ingrese una opción numérica")
           
class usuario(ABC):
    def __init__(self, nombre:str, apellido:str, email:str, contrasenia: str):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia
        
    def __str__(self):
        return self._nombre.title()
    
    def validar_credenciales(email: str, contrasenia:str)-> bool:
        pass
    
    
    
    
class estudiante(usuario):
    def __init__(self, legajo: int, anio_inscripcion_carrera: int):
        self._legajo = legajo
        self._anio_inscripcion_carrera = anio_inscripcion_carrera
    
    def matricular_en_curso(curso): #curso:Curso
        pass
        
        
        
        
        
class profesor(usuario):
    def __init__(self, titulo: str, anio_egreso: int):
        pass    
    
    def __str__(self):
        return self._legajo.title()
    
    def dictar_curso(curso):#curso:Curso
        pass
    
    
martin = (estudiante, "martin", "biselli", "martin@martin.com", "111111")
print(martin)