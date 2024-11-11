from sqlalchemy import Column, String, Date, Integer, Numeric,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from common import Base


class Aula(Base):
    __tablename__ = 'aula'

    ##TODO: Insertar acá las columnas id, nombre y relacion con alumno
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String)
    alumno: Mapped[List["Alumno"]] = relationship(back_populates="aula")

    def __init__(self, nombre):
        self.nombre = nombre
        