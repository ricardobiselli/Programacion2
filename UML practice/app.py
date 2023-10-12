from abc import ABC, abstractmethod


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
    
    def dictar_curso(curso)#curso:Curso
        pass
    
    
martin = (estudiante, "martin", "biselli", "martin@martin.com", "111111")
print(martin)