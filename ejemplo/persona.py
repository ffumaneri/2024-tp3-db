from sqlalchemy import Column, String, Date, Integer, Numeric  

from common import Base


class Persona(Base):
    __tablename__ = 'persona'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    fecha_nacimiento = Column(Date)

    def __init__(self, nombre, fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
