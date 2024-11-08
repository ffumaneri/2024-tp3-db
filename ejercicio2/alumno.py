from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from common import Base


class Alumno(Base):
    __tablename__ = 'alumno'

    ##TODO: Insertar acá las columnas id, nombre, id aula y relaciones con aula
    id = Column(Integer,primary_key=True)
    nombre = Column(String)
    id_aula = Column(Integer,ForeignKey('aula.id'))
    aula = relationship('Aula',back_populates='alumnos')
    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula