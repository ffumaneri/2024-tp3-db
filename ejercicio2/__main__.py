from datetime import date

from .aula import Aula
from .alumno import Alumno
from common import session_factory


def create_data():
    session = session_factory()

    ##TODO: crear 5 alumnos    
    ##TODO: crear 2 aulas

    aula1 = Aula(nombre="Aula 1")
    aula2 = Aula(nombre="Aula 2")
    session.add(aula1)
    session.add(aula2)

    alumno1 = Alumno(nombre="Juan Pérez", aula=aula1)
    alumno2 = Alumno(nombre="Ana Gómez", aula=aula1)
    alumno3 = Alumno(nombre="Carlos Díaz", aula=aula1)
    alumno4 = Alumno(nombre="Lucía Martínez", aula=aula1)
    alumno5 = Alumno(nombre="Pedro Sánchez", aula=aula1)
    session.add_all([alumno1, alumno2, alumno3, alumno4, alumno5])

    session.commit()
    session.close()


def get_alumnos():
    ##TODO: Hacer query para obtener todas las aulas
    session = session_factory()
    query = session.query(Alumno.aula_id)
    session.close()
    return query.all()


if __name__ == "__main__":
    alumnos = get_alumnos()
    if len(alumnos) == 0:
        create_data()
    alumnos = get_alumnos()

    for alumno in alumnos:
        print(f'"{alumno.nombre}" va al aula {alumno.aula.nombre}')
