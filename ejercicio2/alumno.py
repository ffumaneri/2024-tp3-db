from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from common import Base


class Alumno(Base):
    __tablename__ = 'alumno'
    idalumno = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    idaula = Column(Integer, ForeignKey('aula.idaula'))
    
    aula = relationship("Aula", back_populates="alumnos")

    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula  # Asigna el objeto aula, no el id.
