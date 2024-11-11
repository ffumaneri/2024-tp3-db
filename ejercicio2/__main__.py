from datetime import date

from .aula import Aula
from .alumno import Alumno
from common import session_factory


def create_data():
    session = session_factory()
    aula1 = Aula(nombre="Aula 23")
    aula2 = Aula(nombre="Aula Magna")

    alumno1 = Alumno(nombre="Juan Perez", aula=aula1)
    alumno2 = Alumno(nombre="Ana Frank", aula=aula1)
    alumno3 = Alumno(nombre="Luis Borges", aula=aula2)
    alumno4 = Alumno(nombre="Sofía Coppola", aula=aula2)
    alumno5 = Alumno(nombre="Carlos Tevez", aula=aula1)
    session.add_all([aula1, aula2, alumno1, alumno2, alumno3, alumno4, alumno5])
    session.commit()
    session.close()
    
def get_alumnos():
    session = session_factory()
    alumnos_query = session.query(Alumno)
    session.close()
    return alumnos_query.all()


if __name__ == "__main__":
    alumnos = get_alumnos()
    if len(alumnos) == 0:
        create_data()
    alumnos = get_alumnos()

    for alumno in alumnos:
        print(f'"{alumno.nombre}" va al aula {alumno.aula.nombre}')
