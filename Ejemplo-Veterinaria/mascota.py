from datetime import date
from cliente import Cliente

class Mascota():

    def __init__(self, nombre:str, fecha_nacimiento: date) -> None:
        self.__fecha_alta = date.today()
        self.__fecha_ult_atencion = None
        self.__fecha_nacimiento = fecha_nacimiento
        self.__nombre = nombre
        self.__cliente = None

    @property
    def fecha_alta(self) -> date:
        return self.__fecha_alta
    
    @property
    def fecha_ult_atencion(self) -> date:
        return self.__fecha_ult_atencion

    @fecha_ult_atencion.setter
    def fecha_ult_atencion(self, nueva_fecha: str):
        self.__fecha_ult_atencion = nueva_fecha

    @property
    def fecha_nacimiento(self) -> date:
        return self.__fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, nueva_fecha: str):
        self.__fecha_nacimiento = nueva_fecha

    @property
    def nombre(self) -> str:
        return self.__nombre.title()

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre
    
    @property
    def edad(self) -> int:
        return (date.today().year - self.fecha_nacimiento.year)
    
    @property
    def lista_consultas(self) -> list:
        return self.__lista_consultas
    
    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        self.__cliente = cliente

    def __str__(self) -> str:
        return f"Mascota: {self.nombre} Edad: {self.edad} "

