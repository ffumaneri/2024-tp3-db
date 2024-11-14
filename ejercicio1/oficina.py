from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from common import Base

class Oficina(Base):
    __tablename__ = 'oficina'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    jefeId = Column(Integer, ForeignKey("jefe.id"))
    jefe = relationship("Jefe", back_populates="oficina")

    ##TODO: Insertar acá las columnas id, nombre y id del jefe.

    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe
        