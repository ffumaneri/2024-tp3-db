from sqlalchemy import Column, ForeignKey, String, Date, Integer, Numeric
from common import Base
from sqlalchemy.orm import relationship

class Oficina(Base):
    __tablename__ = 'oficina'

    ##TODO: Insertar acá las columnas id, nombre y id del jefe.

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    jefe_id = Column(Integer, ForeignKey('jefe.id'), unique=True)

    jefe = relationship("Jefe", back_populates="oficina")

    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe        