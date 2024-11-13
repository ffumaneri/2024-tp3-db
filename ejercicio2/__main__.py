from .aula import Aula
from .alumno import Alumno
from common import session_factory


def create_data():
    session = session_factory()
    aula1 = Aula(nombre='Aula 1')
    aula2 = Aula(nombre='Aula 2')

    session.add_all([aula1, aula2])
    session.commit()

    alumno1 = Alumno(nombre='Juan', aula=aula1)
    alumno2 = Alumno(nombre='Pedro', aula=aula1)
    alumno3 = Alumno(nombre='Maria', aula=aula2)
    alumno4 = Alumno(nombre='Ana', aula=aula2)
    alumno5 = Alumno(nombre='Luis', aula=aula2)

    session.add_all([alumno1, alumno2, alumno3, alumno4, alumno5])
    session.commit()
    session.close()

def get_alumnos():
    session = session_factory()
    query = session.query(Alumno)
    return query.all(), session

if __name__ == "__main__":
    alumnos, session = get_alumnos()
    if len(alumnos) == 0:
        create_data()
    alumnos, session = get_alumnos()

    for alumno in alumnos:
        print(f'"{alumno.nombre}" va al aula {alumno.aula.nombre}')
    session.close()