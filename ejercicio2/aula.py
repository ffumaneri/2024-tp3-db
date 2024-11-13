from sqlalchemy import Column, String, Date, Integer, Numeric
from sqlalchemy.orm import relationship, Mapped

from common import Base


class Aula(Base):
    __tablename__ = 'aula'

    ##TODO: Insertar acá las columnas id, nombre y relacion con alumno
    id: Mapped[int] = Column(Integer, primary_key=True)
    nombre: Mapped[str] = Column(String)
    alumnos = relationship("Alumno", back_populates="aula")

    def __init__(self, nombre):
        self.nombre = nombre
        