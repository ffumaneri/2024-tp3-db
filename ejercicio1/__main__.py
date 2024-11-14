from common import session_factory
from .jefe import Jefe
from .oficina import Oficina


def create_data():
    session = session_factory()
    juan = Jefe("Juan Perez")
    pedro = Jefe("Pedro Fernandez")

    oficina1 = Oficina("oficina 1", juan)
    oficina2 = Oficina("oficina 2", pedro)

    session.add(juan)
    session.add(pedro)

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