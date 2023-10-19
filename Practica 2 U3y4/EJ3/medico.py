from datetime import date, time
from especialidad import Especialidad

class Medico():
    def __init__(self, nombre_apellido: str, matricula: str, fecha_matricula: date):
        self._nombre_apellido = nombre_apellido
        self._matricula = matricula
        self._fecha_matricula= fecha_matricula
    
    @property
    def nombre_apellido(self):
        return self._nombre_apellido
    
    @nombre_apellido.setter
    def nombre_apellido(self, value):
        self._nombre_apellido = value
        
    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, value):
        matricula = value
    
    @property
    def fecha_matricula(self):
        return self._fecha_matricula
    
    @fecha_matricula.setter
    def fecha_matricula(self, value):
        fecha_matricula = value
    
    
        
def __str__(self) -> str:
    return f""

        
def add_especialidad(especialidad: Especialidad):
    pass

def remove_especialidad(especialidad: Especialidad):
    pass