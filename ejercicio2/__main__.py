from common import session_factory, Base, Session, engine
from .alumno import Alumno
from .aula import Aula

def create_data():
    session = session_factory()

    aula1 = Aula(nombre="aula 1")
    aula2 = Aula(nombre="aula 2")
    
    session.add(aula1)
    session.add(aula2)
    session.commit()  

    alumno1 = Alumno(nombre="Juan", aula=aula1)
    alumno2 = Alumno(nombre="Pedro", aula=aula1)
    alumno3 = Alumno(nombre="Maria", aula=aula2)
    alumno4 = Alumno(nombre="Luis", aula=aula2)
    alumno5 = Alumno(nombre="Carlos", aula=aula2)

    session.add(alumno1)
    session.add(alumno2)
    session.add(alumno3)
    session.add(alumno4)
    session.add(alumno5)

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
