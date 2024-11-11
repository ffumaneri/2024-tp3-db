from datetime import date
from sqlalchemy.orm import joinedload
from common import session_factory
from .alumno import Alumno
from .aula import Aula


def create_data():
    session = session_factory()
    
    ##TODO: crear 2 aulas
    aula1 = Aula(nombre="Aula 1")
    aula2 = Aula(nombre="Aula 2")
    session.add([aula1,aula2])

    ##TODO: crear 5 alumnos
    alumno1 = Alumno(nombre="Alphonse Elric", aula=aula1)
    alumno2 = Alumno(nombre="King Bradley", aula=aula1)
    alumno3 = Alumno(nombre="Roy Mustang", aula=aula2)
    alumno4 = Alumno(nombre="Hohenheim", aula=aula2)
    alumno5 = Alumno(nombre="Edward Elric", aula=aula1)
    session.add_all([alumno1, alumno2, alumno3, alumno4, alumno5])

    session.commit()
    session.close()
    

def get_alumnos():
    session = session_factory()
    
    ##TODO: Hacer query para obtener todas las aulas
    alumnos = session.query(Alumno)
    session.close()
    return alumnos.all()



if __name__ == "__main__":
    alumnos = get_alumnos()
    if len(alumnos) == 0:
        create_data()
    alumnos = get_alumnos()

    for alumno in alumnos:
        print(f'"{alumno.nombre}" va al aula {alumno.aula.nombre}')
