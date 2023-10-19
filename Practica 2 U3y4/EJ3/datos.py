from especialidad import Especialidad
from medico import *

#especialidades
    
general = Especialidad("clinica", 101),
orl = Especialidad("Otorrino", 102),
img = Especialidad("Diagnostico por imagenes", 103),
derma = Especialidad("dermatología", 101),

especialidades = [general, orl, img, derma]

#medicos

med1= Medico("Rene Favaloro", "00010", date(1960,9,10))