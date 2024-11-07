from sqlalchemy import Column, ForeignKey, String, Date, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from common import Base


class Oficina(Base):
    __tablename__ = 'oficina'

    ##TODO: Insertar acá las columnas id, nombre y id del jefe.
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre = Column(String)
    jefe_id : Mapped[int] = mapped_column(ForeignKey("jefe.id"))
    jefe: Mapped["Jefe"] = relationship(back_populates="oficina")
    

    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe
        