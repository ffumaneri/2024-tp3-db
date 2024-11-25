from datetime import date

from .alumno import Alumno
from .aula import Aula
from common import session_factory


def create_data():
    session = session_factory()
    ##TODO: crear 2 aulas
    aula1 = Aula("3ro A")
    aula2 = Aula("4to B")


    ##TODO: crear 5 alumnos
    al1 = Alumno("Jose Lopez", aula1)
    al2 = Alumno("Jacinta Colmenares", aula1)
    al3 = Alumno("Diego Hernandez", aula2)
    al4 = Alumno("Ludmila Martinez", aula2)
    al5 = Alumno("Pedro Cachamay", aula2)          

    session.add(aula1)
    session.add(aula2)

    session.add(al1)
    session.add(al2)
    session.add(al3)
    session.add(al4)
    session.add(al5)
    
    session.commit()
    session.close()


def get_alumnos():
    ##TODO: Hacer query para obtener todas las aulas
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
    alumnos = get_alumnos()
    if len(alumnos) == 0:
        create_data()
    alumnos = get_alumnos()

    for alumno in alumnos:
        print(f'"{alumno.nombre}" va al aula {alumno.aula.nombre}')
