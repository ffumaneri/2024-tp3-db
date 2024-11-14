from datetime import date

from .alumno import Alumno
from .aula import Aula
from common import session_factory


def create_data():
    session = session_factory()

    laboratorio = Aula("Laboratorio de Computación")
    aula23 = Aula("Aula 23")

    santiago = Alumno("Santiago Castro", laboratorio)
    maximiliano = Alumno("Maximiliano Chiardola", aula23)
    exequiel = Alumno("Exequiel Vittor", laboratorio)
    florenciab = Alumno("Florencia Bruno", aula23)
    florenciam = Alumno("Florencia Milera", laboratorio)

    session.add(santiago)
    session.add(maximiliano)
    session.add(exequiel)
    session.add(florenciab)
    session.add(florenciam)

    session.add(laboratorio)
    session.add(aula23)

    session.commit()
    session.close()

def get_alumnos():
    session = session_factory()
    query = session.query(Alumno)
    session.close()
    return query.all()

if __name__ == "__main__":
    alumnos = get_alumnos()
    if len(alumnos) == 0:
        create_data()
    alumnos = get_alumnos()

    for alumno in alumnos:
        print(f'"{alumno.nombre}" va al aula {alumno.aula.nombre}')
