from sqlalchemy import Column, String,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from common import Base


class Alumno(Base):
    __tablename__ = 'alumno'

    ##TODO: Insertar acá las columnas id, nombre, id aula y relaciones con aula
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre = Column(String)
    aula: Mapped["Aula"] = relationship(back_populates="alumno")
    id_aula: Mapped[int] = mapped_column(ForeignKey("aula.id"))

    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula