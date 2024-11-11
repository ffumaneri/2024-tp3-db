from datetime import date

from common import session_factory
from ejercicio2.alumno import Alumno
from ejercicio2.aula import Aula


def create_data():
    session = session_factory()

    aula1 = Aula(nombre="matematicas")
    aula2 = Aula(nombre="ingles")
    
    session.add(aula1)
    session.add(aula2)
    session.commit()  

    session.add(Alumno(nombre="Lautaro", aula=aula1))
    session.add(Alumno(nombre="ezequiel", aula=aula1))
    session.add(Alumno(nombre="hernesto", aula=aula2))
    session.add(Alumno(nombre="jose", aula=aula2))
    session.add(Alumno(nombre="Carlitos", aula=aula2))

    session.commit()
    session.close()



def get_alumnos():
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
