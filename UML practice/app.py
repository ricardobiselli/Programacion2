from abc import ABC, abstractmethod


class ususario(ABC):
    def __init__(self, nombre:str, apellido:str, email:str, contrasenia: str):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasenia = contrasenia
        
    def __str__(self):
        return f"nombre: {self.nombre}"
    
    def validar_credenciales(email: str, contrasenia:str)-> bool:
        
        