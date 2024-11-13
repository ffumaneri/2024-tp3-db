from datetime import date
from sqlalchemy.orm import joinedload

from .alumno import Alumno
from .aula import Aula
from common import session_factory


def create_data():
    session=session_factory()
    
    ##TODO: crear 5 alumnos    
    ##TODO: crear 2 aulas

    aula1 = Aula("Aula 1")
    aula2 = Aula("Aula 2")
    session.add(aula1)
    session.add(aula2)
    
    alumno1 = Alumno("Gaston Brondani", aula1)
    alumno2 = Alumno("Juan Perez", aula1)
    alumno3 = Alumno("Pedro Rodriguez", aula1)
    alumno4 = Alumno("Maria Gomez", aula2)
    alumno5 = Alumno("Ana Martinez", aula2)
    session.add(alumno1)
    session.add(alumno2)
    session.add(alumno3)
    session.add(alumno4)
    session.add(alumno5)

    session.commit()
    session.close()


    
    


def get_alumnos():
    ##TODO: Hacer query para obtener todas las aulas
    session=session_factory()
    query=session.query(Alumno).options(joinedload(Alumno.aula))
    alumnos=query.all()
    session.close()
    return alumnos




if __name__ == "__main__":
    alumnos = get_alumnos()
    if len(alumnos) == 0:
        create_data()
    alumnos = get_alumnos()

    for alumno in alumnos:
        print(f'"{alumno.nombre}" va al aula {alumno.aula.nombre}') 
