from datetime import date
from .aula import Aula
from .alumno import Alumno
from common import session_factory
from sqlalchemy.orm import joinedload  # Importamos joinedload


def create_data():
    session = session_factory()

    aula1 = Aula(nombre="101")  
    aula2 = Aula(nombre="102")

    session.add(aula1)
    session.add(aula2)
    
    alumno1 = Alumno(nombre="Bautista", aula=aula1)
    alumno2 = Alumno(nombre="Nicolas", aula=aula1)
    alumno3 = Alumno(nombre="Alejandro", aula=aula2)
    alumno4 = Alumno(nombre="Augusto", aula=aula2)
    alumno5 = Alumno(nombre="Florencia", aula=aula2)

    session.add(alumno1)
    session.add(alumno2)
    session.add(alumno3)
    session.add(alumno4)
    session.add(alumno5)

    session.commit()
    session.close()


def get_alumnos():
    session = session_factory()
    alumnos = session.query(Alumno).options(joinedload(Alumno.aula)).all()
    session.close()
    return alumnos


if __name__ == "__main__":
    alumnos = get_alumnos()
    if len(alumnos) == 0:
        create_data()
    alumnos = get_alumnos()

    for alumno in alumnos:
        print(f'"{alumno.nombre}" está en la "{alumno.aula.nombre}"')
