from datetime import date

class usuario:
    def __init__(self,usr_name: str, email: str):
        self._usr_name = usr_name
        self.estado = True
        self.email = email
        self.password = ""
        self.nombre = ""
        self.apellido = ""
        self.fecha_alta = date.today()
        self.fecha_baja = None
        
    @property
    def usr_name(self):
        return self._usr_name
        
    def ingresar_pass(self, password):
        self.password = password
        
    def ingresar_datos(self,nombre: str, apellido:str):
        self.nombre = nombre
        self.apellido = apellido
        
    def tramitar_baja(self, estado):
        if self.estado==True:
            self.estado = False
            self.fecha_baja = date.today()
            
    def validar_credenciales(self, usr_name, password):
        if usr_name == self._usr_name and password == self.password:
            return True
        
    def mostrar(self):
        print(f"{self._usr_name}")
        print(f"{self.email}")
        print(f"{self.nombre}")
        print(f"{self.apellido}")
        print(f"{self.fecha_alta}")
        print(f"{self.fecha_baja}")
        print(f"{self.password}")


