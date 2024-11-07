from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from common import Base


class Jefe(Base):
    __tablename__ = 'jefe'

    ##TODO: Insertar acá las columnas id, nombre y la relación con oficina
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre = Column(String)
    oficina: Mapped["Oficina"] = relationship(back_populates="jefe")

    def __init__(self, nombre):
        self.nombre = nombre