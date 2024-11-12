from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from common import Base


class Alumno(Base):
    __tablename__ = 'alumno'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    id_aula = Column(Integer, ForeignKey('aula.id'), nullable=False)

    aula = relationship("Aula", back_populates="alumnos", uselist=False)

    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula
