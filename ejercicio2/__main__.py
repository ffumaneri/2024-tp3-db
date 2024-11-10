from datetime import date

from .aula import Aula
from .alumno import Alumno
from common import session_factory



def create_data():
    session =session_factory()

    aula1 = Aula("Aula Roja")
    aula2 = Aula("Aula Azul")
    session.add(aula1)
    session.add(aula2)
    

    alumno1 = Alumno("Julian Millen",aula1)
    alumno2 = Alumno("Ricardo Kaká",aula1)
    alumno3 = Alumno("Fabian Cubero",aula2)
    alumno4 = Alumno("Lionel Messi",aula2)
    alumno5 = Alumno("Mariano Martinez",aula1)


    session.add(alumno1)
    session.add(alumno2)
    session.add(alumno3)
    session.add(alumno4)
    session.add(alumno5)


    session.commit()
    session.close()


def get_alumnos():
    ##TODO: Hacer query para obtener todas las aulas
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
