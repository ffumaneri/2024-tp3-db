from datetime import date

from .alumno import Alumno
from .aula import Aula
from common import session_factory


def create_data():
    session = session_factory()
    
    ##TODO: crear 2 aulas
    aula14 = Aula(nombre='Aula 14')
    aula23 = Aula(nombre='Aula 23')

    session.add(aula14)
    session.add(aula23)
    
    ##TODO: crear 5 alumnos
    marcos = Alumno('Marcos Hernandez', aula=aula14)
    osvaldo = Alumno('Osvaldo Ramirez', aula=aula14)
    fabricio = Alumno('Fabricio Constanza', aula=aula14)
    victor = Alumno('Victor Colombo', aula=aula23)
    facundo = Alumno('Facundo Perez', aula=aula23)

    session.add(marcos)
    session.add(osvaldo)
    session.add(fabricio)
    session.add(victor)
    session.add(facundo)

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
        print(f'{alumno.nombre} va al aula {alumno.aula.nombre}')