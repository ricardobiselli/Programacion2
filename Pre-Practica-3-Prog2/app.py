"""
Se desea crear un programa que simule el funcionamiento basico de un vehiculo.


-Crear una clase "Vehiculo" con los atributos : marca(Str),ruedas ( Int ),color(Str),enMarcha(Booleano, por defecto False)
-Crear su constructor
-Crear el metodo de instancia arrancar() que permita poner en marcha el vehiculo
-crear el metodo de instancia tipoVehiculo() que devuelva "Automovil" si el vehiculo tiene 4 ruedas y "Motocicleta" si posee 2 ruedas.
-Crear el metodo de instancia mostrar() que muestre por pantalla todos los 4 atributos del vehiculo.


Colocar abajo la comisión y nro de grupo, ademas de los integrantes del grupo ( Nombre y apellido , legajo ).A la hora de hacer el PR colocar nro de grupo y comisión en el titulo del mismo.
Comisión : X
Grupo : X
Integrantes:
-Legajo XXXX,....
-Legajo YYYY,....
"""

class Auto():
    def __init__(self, brand, wheels, color):
        self.brand= brand
        self.wheels= wheels
        self.color= color
        self.inmotion= True
    
    def arrancar(self):
        if not self.inmotion:
            self.inmotion = True
        
        
        
    def tipoVehiculo(self):
        if self.wheels == 4:
            return "Car"
        elif self.wheels == 2:
            return "Motorbike"
        else:
            return "different kind of vehicle...¿?"
            
    def mostrar(self):
        print("atributos del vehículo")
        print(f"brand: {self.brand}")
        print(f"wheels: {self.wheels}")
        print(f"color: {self.color}")
        type = self.tipoVehiculo()
        print(f"Type of vehicle: {type}")
        print(f"Ignition: {'On' if self.inmotion else 'Off'}")
        
myCar = Auto("Fiat", 4, "grey")
myCar.mostrar()
myCar.arrancar()

        

            
        
        
    