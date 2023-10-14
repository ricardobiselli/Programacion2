from abc import ABC, abstractmethod

class usuario(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia

    def __str__(self):
        return self._nombre.title()

    def validar_credenciales(email: str, contrasenia: str) -> bool:
        pass
