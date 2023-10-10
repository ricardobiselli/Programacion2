from abc import ABC, abstractmethod
from datetime import date

class persona(ABC):
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: date, edad: int) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_nacimiento = fecha_nacimiento
        self._edad= edad