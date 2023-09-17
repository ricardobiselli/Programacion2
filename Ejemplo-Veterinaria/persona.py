from abc import ABC, abstractmethod
from tipo_documento import TipoDocumento

class Persona(ABC):

    def __init__(self, nombre: str, apellido: str, nro_documento: str, tipo_documento: TipoDocumento) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._nro_documento = nro_documento
        self._tipo_documento = tipo_documento

    @property
    def nombre(self) -> str:
        return self._nombre.title()

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self._nombre = nuevo_nombre

    @property
    def apellido(self) -> str:
        return self._apellido.title()

    @apellido.setter
    def apellido(self, nuevo_apellido: str):
        self._apellido = nuevo_apellido

    @property
    def nro_documento(self) -> str:
        return self._nro_documento

    @nro_documento.setter
    def nro_documento(self, nuevo_nro_documento: str):
        self._nro_documento = nuevo_nro_documento

    @property
    def tipo_documento(self) -> str:
        return self._tipo_documento

    @tipo_documento.setter
    def tipo_documento(self, nuevo_tipo_documento: TipoDocumento):
        self._tipo_documento = nuevo_tipo_documento

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError
