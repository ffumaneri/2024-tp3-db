from typing import List
from sqlalchemy import String,  Integer
from sqlalchemy.orm import relationship, mapped_column, Mapped
from common import Base


class Aula(Base):
    __tablename__ = 'aula'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)

    alumnos = relationship('Alumno', back_populates='aula')

    def __init__(self, nombre):
        self.nombre = nombre
        