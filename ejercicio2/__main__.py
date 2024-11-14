#from datetime import date
#from .jefe import Jefe
#from .oficina import Oficina

from .aula import Aula
from .alumno import Alumno
from common import session_factory

def create_data():
    session = session_factory()

    aula1 = Aula('Aula 1')
    aula2 = Aula('Aula 2')

    session.add(aula1)
    session.add(aula2)

    mauricio = Alumno('Mauricio', aula1)
    benjamin = Alumno('Benjamín', aula1)
    roberto  = Alumno('Roberto',  aula2)
    pedro    = Alumno('Pedro',    aula2)
    jose     = Alumno('José',     aula2)

    session.add(mauricio)
    session.add(benjamin)
    session.add(roberto)
    session.add(pedro)
    session.add(jose)

    session.commit()
    session.close()

def get_alumnos():
    session = session_factory()
    
    query = session.query(Alumno)
    listaAlumnos = query.all()
    session.close()
    
    return listaAlumnos

if __name__ == "__main__":
    alumnos = get_alumnos()
    if len(alumnos) == 0:
        create_data()
    alumnos = get_alumnos()

    for alumno in alumnos:
        print(f'"{alumno.nombre}" va al aula {alumno.aula.nombre}')
