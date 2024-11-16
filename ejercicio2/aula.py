from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from common import Base

class Aula(Base):
    __tablename__ = 'aula'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)

    alumnos = relationship("Alumno", back_populates="aula")

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return f"<Aula(id={self.id}, nombre='{self.nombre}')>"
