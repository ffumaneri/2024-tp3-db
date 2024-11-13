from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from common import Base


class Alumno(Base):
    __tablename__ = 'alumno'

    ##TODO: Insertar acá las columnas id, nombre, id aula y relaciones con aula
    id: Mapped[int] = Column(Integer, primary_key=True)
    nombre: Mapped[str] = Column(String)
    aula_id: Mapped[int] = Column(Integer, ForeignKey('aula.id'))
    aula = relationship("Aula", back_populates="alumnos", uselist=False)

    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula