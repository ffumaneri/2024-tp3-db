from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, mapped_column, Mapped
from common import Base


class Jefe(Base):
    __tablename__ = 'jefe'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)

    oficina = relationship("Oficina", back_populates='jefe', uselist=False)

    def __init__(self, nombre):
        self.nombre = nombre
