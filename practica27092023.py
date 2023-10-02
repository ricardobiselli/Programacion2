
lista = ["ho", 3.16, "la", 81, 6, 42]

def primeros_tres(lista):
    lista_primeros_tres = lista[:3]
    return lista_primeros_tres
print("EJ 1 ------------------------------------------")
print(primeros_tres(lista))



string1 = input("ingresar el primer string: ")
string2 = input("ingresar el segundo string: ")
nro = int(input("ingresar el nro: "))
    
def concatena(string1, string2, nro):
 
    concatenacion = string1 + " "+ string2 + " " + str(nro)
    return concatenacion

mensaje = concatena(string1, string2, nro)
print("EJ 2 ------------------------------------------")
print(mensaje)

    

"""3. calcularTarifaTotal(tarifaPorHora): Deberá retornar el valor de la tarifa total en pesos
teniendo encuenta la entrada y salida y la tarifa por hora. Si la patente es invalida o la entrada más
reciente que la salida deberá informar un error."""

print("EJ 3 ------------------------------------------")
  
class vehiculo:
    def __init__(self, patente, descripcion):
        self.patente=patente
        self.descripcion=descripcion
        
    def mostrar(self):
        print(f"Patente: {self.patente}")
        print(f"Descripción: {self.descripcion}")
        
    def validarPatente(self):
        if len(self.patente) == 6 or len(self.patente) == 8:
            return True
        else:
            return False

auto1 = vehiculo("FRG778", "esta es ladescripcion del auto")
auto1.mostrar()
validacionPatente = auto1.validarPatente()
print(validacionPatente)


class estadia:
    def __init__(self, vehiculo, hora_entrada, hora_salida):
        self.vehiculo = vehiculo
        self.hora_entrada =  hora_entrada
        self.hora_salida = hora_salida
        
    def mostrar(self):
        print(f"vehiculo: {self.vehiculo}")
        print(f"hora de entrada: {self.hora_entrada}")
        print(f"hora de salida: {self.hora_salida}")
    def calcularTarifaTotal(self, tarifaPorHora):
        if not self.vehiculo.validarPatente() or self.hora_entrada > self.hora_salida:
            return "Error: Patente inválida o hora de entrada mayor que hora de salida"
        else:
            tiempo_estadia = self.hora_salida - self.hora_entrada
            tarifa_total = tiempo_estadia * tarifaPorHora
            print(tarifa_total)
            return tarifa_total

auto1 = vehiculo("FTQ774", "Esta es la descripción del auto")

auto1.mostrar()
cliente = estadia(auto1, 19, 23)
cliente.mostrar()
tarifaPorHora = 10  
tarifa_total = cliente.calcularTarifaTotal(tarifaPorHora)

    