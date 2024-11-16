from datetime import date
from .alumno import Alumno
from .aula import Aula
from common import session_factory


def create_data():
    ##TODO: crear 5 alumnos

    ##TODO: crear 2 aulas

    session = session_factory()

    aula1 = Aula("aula 1")
    aula2 = Aula("aula 2")

    martin = Alumno("Juan Perez",aula1)
    sergio = Alumno("Pedro Fernandez",aula1)
    exequiel = Alumno("Laura Fernandez",aula2)
    rocio = Alumno("Maria Gutierrez",aula1)
    facundo = Alumno("Pamela Lopez",aula2)


    session.add(martin)
    session.add(sergio)
    session.add(exequiel)
    session.add(rocio)
    session.add(facundo)
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
