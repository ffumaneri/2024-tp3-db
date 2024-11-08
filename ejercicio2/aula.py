from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from common import Base


class Aula(Base):
    __tablename__ = 'aula'
    idaula = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
  
    # Relación inversa, desde 'Aula' hacia 'Alumno'
    alumnos = relationship("Alumno", back_populates="aula")

    def __init__(self, nombre):
        self.nombre = nombre  # Corrige 'self.name' a 'self.nombre'
