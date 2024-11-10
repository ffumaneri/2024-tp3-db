from sqlalchemy import Column, String, Date, Integer, Numeric
from sqlalchemy.orm import relationship
from common import Base


class Aula(Base):
    __tablename__ = 'aula'
    id= Column(Integer, primary_key=True, autoincrement=True)
    nombre= Column(String)
    alumnos = relationship("Alumno", back_populates="aula")

    def __init__(self, nombre):
        self.nombre = nombre
        