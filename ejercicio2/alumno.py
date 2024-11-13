from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from common import Base


class Alumno(Base):
    __tablename__ = 'alumno'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    aula_id: Mapped[int] = mapped_column(Integer, ForeignKey('aula.id'))

    aula = relationship('Aula', back_populates='alumnos')

    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula

