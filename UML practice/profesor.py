from app import usuario

class profesor(usuario):
    
    def __init__(self, titulo: str, anio_egreso: int):
        pass

    def __str__(self):
        return self._legajo.title()

    def dictar_curso(curso):  # curso:Curso
        pass