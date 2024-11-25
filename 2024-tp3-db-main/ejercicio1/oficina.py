from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from common import Base
from jefe import Jefe


class Oficina(Base):
    __tablename__ = 'oficina'

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    jefe_id: Mapped[int] = mapped_column(ForeignKey("jefe.id"))
    jefe: Mapped["Jefe"] = relationship(back_populates="oficina")

    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe
        