from sqlalchemy import Column, String, Date, Integer, Numeric
from sqlalchemy.orm import relationship
from common import Base


class Aula(Base):
    __tablename__ = 'aula'

    ##TODO: Insertar acá las columnas id, nombre y relacion con alumno

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    alumnos = relationship("Alumno", back_populates="aula", uselist=True)

    def __init__(self, nombre):
        self.nombre = nombre
        