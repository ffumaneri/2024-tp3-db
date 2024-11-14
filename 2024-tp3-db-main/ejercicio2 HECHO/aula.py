from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from common import Base

class Aula(Base):
    __tablename__ = 'aula'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Clave primaria
    nombre = Column(String, nullable=False)

    # Relación con Alumno, lado del aula (One-to-Many)
    alumnos = relationship("Alumno", back_populates="aula", cascade="all, delete-orphan")

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return f"<Aula(id={self.id}, nombre='{self.nombre}')>"
