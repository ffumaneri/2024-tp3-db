from datetime import date

from .jefe import Jefe
from .oficina import Oficina
from common import session_factory


def create_data():
    ##TODO: crear 5 alumnos
    ##TODO: crear 2 aulas
    pass #borrar esto cuando agreguen codigo


def get_alumnos():
    ##TODO: Hacer query para obtener todas las aulas
    pass #borrar esto cuando agreguen codigo



if __name__ == "__main__":
    alumnos = get_alumnos()
    if len(alumnos) == 0:
        create_data()
    alumnos = get_alumnos()

    for alumno in alumnos:
        print(f'"{alumno.nombre}" va al aula {alumno.aula.nombre}')
