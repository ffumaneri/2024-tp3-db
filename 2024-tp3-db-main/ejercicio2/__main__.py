from .alumno import Alumno
from .aula import Aula
from common import session_factory


def create_data():
   
    session = session_factory()

    try:
        
        aula1 = Aula(nombre="Matemáticas")
        aula2 = Aula(nombre="Ciencias")


        alumno1 = Alumno(nombre="Juan Pérez", aula=aula1)
        alumno2 = Alumno(nombre="María Gómez", aula=aula1)
        alumno3 = Alumno(nombre="Carlos Sánchez", aula=aula2)
        alumno4 = Alumno(nombre="Laura Fernández", aula=aula2)
        alumno5 = Alumno(nombre="Pedro García", aula=aula2)

        
        session.add_all([aula1, aula2, alumno1, alumno2, alumno3, alumno4, alumno5])
        session.commit()
    except Exception as e:
        session.rollback()
        print("Error al crear los datos:", e)
    finally:
        session.close()


def get_alumnos():
    
    session = session_factory()

    try:
        
        alumnos = session.query(Alumno).all()
        return alumnos
    except Exception as e:
        print("Error al obtener los alumnos:", e)
        return []
    finally:
        session.close()


if __name__ == "__main__":
    alumnos = get_alumnos()
    if len(alumnos) == 0:
        create_data()
        alumnos = get_alumnos()

    for alumno in alumnos:
        print(f'"{alumno.nombre}" va al aula {alumno.aula.nombre}')