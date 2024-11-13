from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from common import Base

class Oficina(Base):
    __tablename__ = 'oficina'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    jefe_id: Mapped[int] = mapped_column(Integer, ForeignKey('jefe.id'))

    jefe = relationship("Jefe", back_populates='oficina')

    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe
