from datetime import date
from .alumno import Alumno
from .aula import Aula
from common import session_factory

def create_data():
    session = session_factory()
    
    aula1 = Aula("Aula 101")
    aula2 = Aula("Aula 102")
    session.add(aula1)
    session.add(aula2)
    
    alumno1 = Alumno("Juan", aula1)
    alumno2 = Alumno("María", aula1)
    alumno3 = Alumno("Carlos", aula1)
    alumno4 = Alumno("Ana", aula2)
    alumno5 = Alumno("Luis", aula2)

    session.add_all([alumno1, alumno2, alumno3, alumno4, alumno5])
    
    session.commit()
    session.close()

def get_alumnos():
    session = session_factory()
    query = session.query(Alumno).all()
    session.close()
    return query

if __name__ == "__main__":
    alumnos = get_alumnos()
    if len(alumnos) == 0:
        create_data()
    alumnos = get_alumnos()

    for alumno in alumnos:
        print(f'"{alumno.nombre}" va al aula {alumno.aula.nombre}')
