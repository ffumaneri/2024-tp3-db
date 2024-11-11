from datetime import date
from sqlalchemy.orm import joinedload
from .alumno import Alumno
from .aula import Aula
from common import session_factory


def create_data():
    session = session_factory()
    aula1 = Aula("aula 1")
    aula2 = Aula("aula 2")

    session.add(aula1)
    session.add(aula2)
    session.commit()

    ##TODO: crear 5 alumnos
    alumno1 = Alumno("Julieta", aula=aula1)
    alumno2 = Alumno("Matias", aula=aula1)
    alumno3 = Alumno("Patricio", aula=aula1)
    alumno4 = Alumno("Martina", aula=aula2)
    alumno5 = Alumno("Irene", aula=aula2)
    
    session.add_all([alumno1, alumno2, alumno3, alumno4, alumno5])

    session.commit()
    session.close()
    session.commit()
    session.close()
    # pass #borrar esto cuando agreguen codigo


def get_alumnos():
    ##TODO: Hacer query para obtener todas las aulas
    session = session_factory()
    alumnos = session.query(Alumno)
    

    return alumnos.all() , session
    # pass #borrar esto cuando agreguen codigo



if __name__ == "__main__":
    alumnos, session = get_alumnos()
    if len(alumnos) == 0:
        create_data()
    alumnos,session = get_alumnos()

    for alumno in alumnos:
        print(f'"{alumno.nombre}" va al aula {alumno.aula.nombre}') 
    session.close()