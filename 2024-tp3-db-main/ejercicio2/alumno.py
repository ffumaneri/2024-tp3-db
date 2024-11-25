from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from common import Base
from aula import Aula

class Alumno(Base):
    __tablename__ = 'alumno'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    id_aula: Mapped[int] = mapped_column(ForeignKey("aula.id"), nullable=False)

    # Relación hacia Aula (bidireccional)
    aula: Mapped["Aula"] = relationship("Aula", back_populates="alumnos")

    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula