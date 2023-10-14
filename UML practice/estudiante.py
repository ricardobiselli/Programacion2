from app import usuario

class estudiante(usuario):
    def __init__(self, legajo: int, anio_inscripcion_carrera: int):
        self._legajo = legajo
        self._anio_inscripcion_carrera = anio_inscripcion_carrera

    def matricular_en_curso(curso):  # curso:Curso
        pass