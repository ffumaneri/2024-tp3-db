from datetime import date
from .alumno import Alumno
from .aula import Aula
from common import session_factory

def create_data():
    session = session_factory()
    aula1 = Aula('Aula 1')
    aula2 = Aula('Aula 2')
    alumno1 = Alumno('Juan', aula1)
    alumno2 = Alumno('Pepe', aula1)
    alumno3 = Alumno('Luis', aula2)
    alumno4 = Alumno('Maria', aula2)
    alumno5 = Alumno('Carlos', aula2)
    session.add(aula1)
    session.add(aula2)
    session.add(alumno1)
    session.add(alumno2)
    session.add(alumno3)
    session.add(alumno4)
    session.add(alumno5)
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
