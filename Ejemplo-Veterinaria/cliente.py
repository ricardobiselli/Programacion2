from persona import Persona
from datetime import date
from saldo import Saldo
from tipo_documento import TipoDocumento

class Cliente(Persona):

    def __init__(self, nombre: str, apellido: str, nro_documento: str, tipo_documento: TipoDocumento = TipoDocumento('DNI')) -> None:
        super().__init__(nombre,apellido,nro_documento, tipo_documento)
        self.__fecha_alta = date.today()
        self.__fecha_saldo_cta_corriente = None
        self.__saldo_cta_corriente = float(0)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

    @property
    def fecha_alta(self) -> date:
        return self.__fecha_alta

    @property
    def fecha_saldo_cta_corriente(self) -> date:
        return self.__fecha_saldo_cta_corriente

    @fecha_saldo_cta_corriente.setter
    def fecha_saldo_cta_corriente(self, nueva_fecha: str):
        self.__fecha_saldo_cta_corriente = nueva_fecha

    @property
    def saldo_cta_corriente(self) -> float:
        return self.__saldo_cta_corriente

    @saldo_cta_corriente.setter
    def saldo_cta_corriente(self, nuevo_saldo: str):
        self.__saldo_cta_corriente = nuevo_saldo

    def calcular_interes_saldo(self) -> float:
        """ Retorna el saldo con intereses, si el cliente no posee
            saldo retorna 0
        """
        if self.__saldo_cta_corriente > 0:
            return Saldo.calcular_interes_saldo(self.saldo_cta_corriente, self.fecha_saldo_cta_corriente)

        return float(0)