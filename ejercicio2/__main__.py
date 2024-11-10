from datetime import date
from typing import List

from .alumno import Alumno
from .aula import Aula
from common import session_factory


def create_data():
    session = session_factory()
    
    aula1 = Aula("1")
    aula2 = Aula("2")

    juan = Alumno("Juan Perez", aula1)
    pedro = Alumno("Pedro Fernandez", aula1)
    geronimo = Alumno("Gerónimo Reffino", aula2)
    micaela = Alumno("Micaela Cáceres", aula2)


    session.add(juan)
    session.add(pedro)
    session.add(geronimo)
    session.add(micaela)

    session.commit()
    session.close()

def get_alumnos():
    session = session_factory()
    query = session.query(Alumno)
    session.close()
    return query.all()   

def get_aulas():
    session = session_factory()
    query = session.query(Aula)
    session.close()
    return query.all()

if __name__ == "__main__":
    aulas = get_aulas()
    if len(aulas) == 0:
        create_data()
    alumnos = get_alumnos()

    for alumno in alumnos:
        print(f'{alumno.nombre} va al aula {alumno.aula.nombre}')
