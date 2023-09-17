from persona import Persona
from tipo_documento import TipoDocumento

class Veterinario(Persona):

    def __init__(self, nombre: str, apellido: str, nro_documento: str, matricula: str, tipo_documento: TipoDocumento = TipoDocumento('DNI')) -> None:
        super().__init__(nombre, apellido, nro_documento, tipo_documento)
        self.__matricula = matricula

    @property
    def matricula(self) -> str:
        return self.__matricula.upper()

    @matricula.setter
    def matricula(self, nueva_matricula: str):
        self.__matricula = nueva_matricula

    def __str__(self) -> str:
        return f"Vet: {self.nombre} {self.apellido} Mat: {self.matricula}"