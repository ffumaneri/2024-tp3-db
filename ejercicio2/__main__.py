from common import session_factory, Base, Session, engine
from .alumno import Alumno
from .aula import Aula

def create_data():
    session = session_factory()

    # Crear 2 aulas primero
    aula1 = Aula(nombre="aula 1")
    aula2 = Aula(nombre="aula 2")
    
    # Añadir las aulas a la sesión primero para que se guarden en la base de datos
    session.add(aula1)
    session.add(aula2)
    session.commit()  # Hacer commit para que se generen los ID de las aulas

    # Ahora puedes crear los alumnos y asignarles las aulas
    alumno1 = Alumno(nombre="Juan", aula=aula1)
    alumno2 = Alumno(nombre="Pedro", aula=aula1)
    alumno3 = Alumno(nombre="Maria", aula=aula2)
    alumno4 = Alumno(nombre="Luis", aula=aula2)
    alumno5 = Alumno(nombre="Carlos", aula=aula2)

    # Añadir los alumnos a la sesión
    session.add(alumno1)
    session.add(alumno2)
    session.add(alumno3)
    session.add(alumno4)
    session.add(alumno5)

    # Confirmar los cambios en la base de datos
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
