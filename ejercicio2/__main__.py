from common import session_factory
from sqlalchemy.orm import joinedload
from .alumno import Alumno
from .aula import Aula


def create_data():
    session = session_factory()
    ##TODO: crear 2 aulas
    aula_1 = Aula("Aula 1")
    aula_2 = Aula("Aula 2")

    session.add(aula_1)
    session.add(aula_2)
    session.commit()

    ##TODO: crear 5 alumnos
    juan = Alumno("Juan", aula_1)
    pablo = Alumno("Pablo", aula_1)
    matias = Alumno("Matias", aula_2)
    joaquin = Alumno("Joaquin", aula_2)
    florencia = Alumno("Florencia", aula_1)

    session.add(juan)
    session.add(pablo)
    session.add(matias)
    session.add(joaquin)
    session.add(florencia)

    session.commit()
    session.close()

def get_alumnos():
    ##TODO: Hacer query para obtener todas las aulas
    session = session_factory()
    query = session.query(Aula).options(joinedload(Aula.alumno))  # Eager load Alumno instances
    session.close()
    return query.all()


if __name__ == "__main__":
    aulas = get_alumnos()
    if len(aulas) == 0:
        create_data()
        aulas = get_alumnos()  

    for aula in aulas:
        for alumno in aula.alumno:  
            print(f'"{alumno.nombre}" va al aula {aula.nombre}')