from common import session_factory
from .aula import Aula
from .alumno import Alumno


def create_data():  

    session = session_factory()

    aula1 = Aula("aula 1")
    aula2 = Aula("aula 2")

    session.add(aula1)
    session.add(aula2)

    session.commit()

    alumno1 = Alumno(nombre="Juan Perez", aula=aula1)
    alumno2 = Alumno(nombre="Pedro Fernandez", aula=aula1)
    alumno3 = Alumno(nombre="Maria Fernandez", aula=aula2)
    alumno4 = Alumno(nombre="Juan Fernandez", aula=aula2)
    alumno5 = Alumno(nombre="Maria Perez", aula=aula2)   

    session.add_all([alumno1, alumno2, alumno3, alumno4, alumno5])

    session.commit()
    session.close()


def get_alumnos():
    session = session_factory()
    query = session.query(Alumno)
    return query.all(), session

if __name__ == "__main__":
    alumnos, session = get_alumnos()
    if len(alumnos) == 0:
        create_data()
    alumnos, session = get_alumnos()

    for alumno in alumnos:
        print(f'"{alumno.nombre}" va al aula {alumno.aula.nombre}')
    session.close()
        
