# See: https://www.geeksforgeeks.org/python-datetime-module/
from datetime import date

class Saldo:

    __interes_mensual = float(0.1)

    @classmethod
    def calcular_interes_saldo(cls, saldo: float, fecha_interes_desde: date) -> float:
        saldo = 0
        fecha_hoy = date.today()
        meses = int(((fecha_hoy - fecha_interes_desde).days)/30.44)
        interes_saldo = meses * cls.__interes_mensual * 100 * saldo
        return interes_saldo