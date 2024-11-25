from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column
from common import Base
from alumno import Alumno

class Aula(Base):
    __tablename__ = 'aula'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)

    # Relación con Alumno
    alumnos: Mapped[list["Alumno"]] = relationship("Alumno", back_populates="aula")

    def __init__(self, nombre):
        self.nombre = nombre