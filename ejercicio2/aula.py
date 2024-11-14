from sqlalchemy import Column, String, Date, Integer, Numeric
from sqlalchemy.orm import relationship
from common import Base
from ejercicio2.alumno import Alumno


class Aula(Base):
    __tablename__ = 'aula'

    ##TODO: Insertar acá las columnas id, nombre y relacion con alumno
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    alumnos = relationship(Alumno)


    def __init__(self, nombre):
        self.name = nombre
        