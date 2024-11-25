from datetime import date

from .persona import Persona
from common import session_factory


def create_people():
    session = session_factory()
    juan = Persona("Juan Perez", date(1984, 10, 20))
    pedro = Persona("Pedro Fernandez", date(1990, 5, 17))
    session.add(juan)
    session.add(pedro)
    session.commit()
    session.close()


def get_people():
    session = session_factory()
    people_query = session.query(Persona)
    session.close()
    return people_query.all()


if __name__ == "__main__":
    people = get_people()
    if len(people) == 0:
        create_people()
    people = get_people()

    for person in people:
        print(f'{person.nombre} nacio en {person.fecha_nacimiento}')