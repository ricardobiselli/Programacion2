from consulta import Consulta
from datetime import date

class Factura():

    __nro_fact = int(0)

    def __init__(self, consulta: Consulta, condicion_pago: str = 'contado') -> None:
        self.__fecha = date.today()
        self.__nro = self.nro_factura
        self.__consulta = consulta
        self.__monto = consulta.monto_practica
        self.__condicion_pago = condicion_pago
        self.__estado = False
    
    @property
    def nro_factura(cls):
        cls.__nro_fact = cls.__nro_fact + 1
        return cls.__nro_fact

    @property
    def consulta(self) -> Consulta:
        return self.__consulta
    
    @property
    def fecha(self) -> date:
        return self.__fecha
    
    @property
    def nro(self) -> int:
        return self.__nro
    
    @property
    def monto(self) -> float:
        return self.__monto
    
    @property
    def condicion_pago(self) -> str:
        return self.__condicion_pago
    
    @property
    def estado(self) -> str:
        return 'Cobrado' if self.__estado else 'Pendiente'
    
    @estado.setter
    def estado(self, nuevo_estado: bool):
        self.__estado = nuevo_estado

    def __str__(self) -> str:
        return f''' Nro Factura: {self.nro} - Fecha: {self.fecha}
                    Monto: {self.monto} - Estado: {self.estado}
                '''
