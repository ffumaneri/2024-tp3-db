from datetime import date

from .alumno import Alumno
from .aula import Aula
from common import session_factory


def create_data():
    ##TODO: crear 5 alumnos

    ##TODO: crear 2 aulas

    session = session_factory()

    aula1 = Aula("aula 1")
    aula2 = Aula("aula 2")

    juan = Alumno("Juan Perez",aula1)
    pedro = Alumno("Pedro Fernandez",aula1)
    laura = Alumno("Laura Fernandez",aula2)
    maria = Alumno("Maria Gutierrez",aula1)
    pamela = Alumno("Pamela Lopez",aula2)


    session.add(juan)
    session.add(pedro)
    session.add(laura)
    session.add(maria)
    session.add(pamela)

    session.commit()
    session.close()

    #pass #borrar esto cuando agreguen codigo


def get_alumnos():
    ##TODO: Hacer query para obtener todas las aulas
  #  pass #borrar esto cuando agreguen codigo
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
