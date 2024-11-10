from sqlalchemy import Column, String, Date, Integer, Numeric
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from common import Base


class Alumno(Base):
    __tablename__ = 'alumno'

    id= Column(Integer, primary_key=True)
    nombre=Column(String)
    id_aula=Column(Integer,ForeignKey('aula.id'))

    aula = relationship('Aula', backref='alumnos', lazy='joined')

    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula