from datetime import date

class Paciente():
    def __init__(self, nombre_apellido: str, direccion: str, fecha_nacimiento: date, edad: int):
        self._nombre_apellido = nombre_apellido
        self._direccion = direccion
        self._fecha_nacimiento = fecha_nacimiento
        self._edad = edad
        
    @property
    def nombre_apellido(self):
        return self._nombre_apellido
    
    @nombre_apellido.setter
    def nombre_apellido(self, value):
        self._nombre_apellido = value
        
    @property
    def direccion(self):
        return self._direccion
    
    @direccion.setter
    def direccion(self, value):
        self._direccion = value
        
    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        self._fecha_nacimiento = value
        
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, value):
        self._edad = value
        
        

    def __str__(self) -> str:
        return f"Nombre: {self._nombre_apellido}"

