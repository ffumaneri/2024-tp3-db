from datetime import date

from .aula import Aula
from .alumno import Alumno
from common import session_factory


def create_data():
    session = session_factory()
    ##TODO: crear 5 alumnos
    juan = Alumno("Juan Terzano", aula1)
    rodrigo = Alumno("Rodrigo Prettis", aula2)
    ivan = Alumno("Ivan Zualet", aula1)
    manuel = Alumno("Manuel Hernandez", aula2)
    enzo = Alumno("Enzo Fernandez", aula1)

    session.add(aula1)
    session.add(aula2)
    session.add(juan)
    session.add(rodrigo)
    session.add(ivan)
    session.add(manuel)
    session.add(enzo)

    ##TODO: crear 2 aulas
    aula1 = Aula("Aula 1")
    aula2 = Aula("Aula 2")
    
    session.commit()
    session.close()


def get_alumnos():
    ##TODO: Hacer query para obtener todas las aulas
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
