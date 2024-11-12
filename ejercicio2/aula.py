from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from common import Base


class Aula(Base):
    __tablename__ = 'aula'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    alumnos = relationship("Alumno", back_populates="aula", uselist=True)

    def __init__(self, nombre):
        self.nombre = nombre
