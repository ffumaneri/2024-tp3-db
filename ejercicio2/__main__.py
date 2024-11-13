from datetime import date

from .aula import Aula
from .alumno import Alumno
from common import session_factory


def create_data():
    session = session_factory()
    aula1 = Aula("Aula 1")
    aula2 = Aula("Aula 2")
    session.add(aula1)
    session.add(aula2)
    session.commit()
    
    alumno1 = Alumno("Juan Perez", aula1)
    alumno2 = Alumno("Maria Lopez", aula1)
    alumno3 = Alumno("Pedro Martinez", aula1)
    alumno4 = Alumno("Ana Fernandez", aula2)
    alumno5 = Alumno("Lucas Rodriguez", aula2)
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
    alumnos_query = session.query(Alumno)
    return alumnos_query.all()

if __name__ == "__main__":
    alumnos = get_alumnos()
    if len(alumnos) == 0:
        create_data()
    alumnos = get_alumnos()

    for alumno in alumnos:
        print(f'"{alumno.nombre}" va al aula {alumno.aula.nombre}')
    