from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from common import Base


class Jefe(Base):
    __tablename__ = 'jefe'

    ##TODO: Insertar acá las columnas id, nombre y la relación con oficina.
    id: Mapped[int] = Column(Integer, primary_key=True)
    nombre: Mapped[str] = Column(String)
    oficina = relationship("Oficina", back_populates="jefe", uselist=False)

    def __init__(self, nombre):
        self.nombre = nombre