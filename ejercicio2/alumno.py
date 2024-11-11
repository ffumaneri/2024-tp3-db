from sqlalchemy import Column, String, Date, Integer, Numeric,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from common import Base


class Alumno(Base):
    __tablename__ = 'alumno'

    ##TODO: Insertar acá las columnas id, nombre, id aula y relaciones con aula
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String)
    aula_id: Mapped[int] = mapped_column(ForeignKey("aula.id"))
    aula: Mapped["Aula"] = relationship(back_populates="alumno")

    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula