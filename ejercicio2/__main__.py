from datetime import date

from .alumno import Alumno
from .aula import Aula
from common import session_factory


def create_data():
    
    session = session_factory()
    
    aula1 = Aula("aula 1")
    aula2 = Aula("aula 2")
    
    alumno1 = Alumno("Juan Perez",aula1)
    alumno2 = Alumno("Pedro Fernandez",aula1)
    alumno3 = Alumno("Fran Carroza",aula2)
    alumno4 = Alumno("Alexis Farias",aula2)
    alumno5 = Alumno("Rodrigo Blanco",aula2)
    
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
    alumno_query = session.query(Alumno)
    session.close()
    return alumno_query.all()


if __name__ == "__main__":
    alumnos = get_alumnos()
    if len(alumnos) == 0:
        create_data()
    alumnos = get_alumnos()

    for alumno in alumnos:
        print(f'"{alumno.nombre}" va al aula {alumno.aula.nombre}')
