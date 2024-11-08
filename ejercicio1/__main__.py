from .jefe import Jefe
from .oficina import Oficina
from common import session_factory, Base,Session,engine

def create_data():
    session = session_factory()

    juan = Jefe(nombre="Juan", apellido="Perez")
    pedro = Jefe(nombre="Pedro", apellido="Fernandez")

    oficina1 = Oficina(nombre="oficina 1", jefe=juan)  
    oficina2 = Oficina(nombre="oficina 2", jefe=pedro)


    session.add(oficina1)
    session.add(oficina2)
    session.commit()  

    session.close()

def get_oficinas():
    session = session_factory()
    query = session.query(Oficina)
    session.close()
    return query.all()


if __name__ == "__main__":
    people = get_oficinas()
    if len(people) == 0:
        create_data()
    
    oficinas = get_oficinas()
    for oficina in oficinas:
        print(f'{oficina.nombre} tiene como jefe {oficina.jefe.nombre}')
