from typing import List
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from common import Base


class Aula(Base):
    __tablename__ = 'aula'

    ##TODO: Insertar acá las columnas id, nombre y relacion con alumno
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre = Column(String)
    alumno: Mapped[List["Alumno"]] = relationship(back_populates="aula")

    def __init__(self, nombre):
        self.nombre = nombre
        