from datetime import date
from veterinario import Veterinario
from mascota import Mascota

class Consulta():

    def __init__(self, mascota: Mascota) -> None:
        self.__fecha = date.today()
        self.__diagnostico = None
        self.__veterinario = None
        self.__mascota = mascota
        self.__monto_practica = None

    @property
    def fecha(self) -> date:
        return self.__fecha
    
    @property
    def diagnostico(self) -> str:
        return self.__diagnostico
    
    @diagnostico.setter
    def diagnostico(self, nuevo_diagnostico: str):
        self.__diagnostico = nuevo_diagnostico

    @property
    def veterinario(self) -> Veterinario:
        return self.__veterinario
    
    @veterinario.setter
    def veterinario(self, veterinario: Veterinario):
        self.__veterinario = veterinario

    @property
    def mascota(self) -> Mascota:
        return self.__mascota
    
    @mascota.setter
    def mascota(self, mascota: Mascota):
        self.__mascota = mascota

    @property
    def monto_practica(self) -> float:
        return self.__monto_practica
    
    @monto_practica.setter
    def monto_practica(self, nuevo_monto_practica: float):
        self.__monto_practica = nuevo_monto_practica

    def __str__(self) -> str:
        return f'''Fecha: {self.fecha} - Mascota: {self.mascota.nombre} - Cliente: {self.mascota.cliente}
                Diagnostico: {self.diagnostico}'''
    

    