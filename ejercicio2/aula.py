from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from common import Base


class Aula(Base):
    __tablename__ = 'aula'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)

    alumnos = relationship('Alumno', back_populates='aula')

    ##TODO: Insertar acá las columnas id, nombre y relacion con alumno

    def __init__(self, nombre):
        self.nombre = nombre
        