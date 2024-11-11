from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from common import Base


class Alumno(Base):
    __tablename__ = 'alumno'
    id= Column(Integer, primary_key=True)
    nombre= Column(String)
    aula_id = Column(Integer, ForeignKey('aula.id'))
    aula = relationship('Aula', back_populates='alumnos')
    ##TODO: Insertar acá las columnas id, nombre, id aula y relaciones con aula

    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula