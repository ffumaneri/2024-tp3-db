from .aula import Aula
from .alumno import Alumno
from common import session_factory


def create_data():
    session = session_factory()
    
    # Crear 2 aulas
    aula_100 = Aula(nombre="Aula 100")
    aula_200 = Aula(nombre="Aula 200")

    # Crear 5 alumnos
    maria = Alumno(nombre="Maria Marquez", aula=aula_100)
    juan = Alumno(nombre="Juan Gomez", aula=aula_100)
    pedro = Alumno(nombre="Pedro Sanchez", aula=aula_100)
    alejandra = Alumno(nombre="Alejandra Alva", aula=aula_200)
    marcos = Alumno(nombre="Marcos Marquez", aula=aula_200)

    session.add(aula_100)
    session.add(aula_200)
    session.add(maria)
    session.add(juan)
    session.add(pedro)
    session.add(alejandra)
    session.add(marcos)

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
        print(f'"{alumno.nombre}" va al aula {alumno.aula.nombre}')