from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from common import Base


class Aula(Base):
    __tablename__ = "aula"

    ##TODO: Insertar acá las columnas id, nombre y relacion con alumno
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    alumnos = relationship("Alumno",back_populates='aula')

    def __init__(self, nombre):
        self.nombre = nombre
