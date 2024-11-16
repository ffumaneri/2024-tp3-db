from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship
from common import Base


class Alumno(Base):
    __tablename__ = 'alumnos'

    ##TODO: Insertar acá las columnas id, nombre, id aula y relaciones con aula

    id = Column(Integer, primary_key=True)
    nombre = Column(String(70))
    id_aula = Column(Integer, ForeignKey('aulas.id'))
    aula = relationship('Aula')

    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula