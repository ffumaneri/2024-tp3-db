from .jefe import Jefe
from .oficina import Oficina
from common import session_factory, Base,Session,engine

# Función para crear datos
def create_data():
    session = session_factory()

    # Crear instancias de Jefe
    juan = Jefe(nombre="Juan", apellido="Perez")
    pedro = Jefe(nombre="Pedro", apellido="Fernandez")

    # Crear las oficinas, pasando los objetos Jefe
    oficina1 = Oficina(nombre="oficina 1", jefe=juan)  # Pasa el objeto Jefe
    oficina2 = Oficina(nombre="oficina 2", jefe=pedro)

    # Agregar las oficinas y commit
    session.add(oficina1)
    session.add(oficina2)
    session.commit()  # Aquí SQLAlchemy gestionará la relación y la clave foránea

    session.close()
# Función para obtener las oficinas
def get_oficinas():
    session = session_factory()
    query = session.query(Oficina)
    session.close()
    return query.all()

# Código principal
if __name__ == "__main__":
    people = get_oficinas()
    if len(people) == 0:
        create_data()
    
    oficinas = get_oficinas()
    for oficina in oficinas:
        print(f'{oficina.nombre} tiene como jefe {oficina.jefe.nombre}')
