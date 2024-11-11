from sqlalchemy import Column, String, Date, Integer, Numeric,ForeignKey
from sqlalchemy.orm import relationship

from common import Base


class Oficina(Base):
    __tablename__ = 'oficina'

    ##TODO: Insertar acá las columnas id, nombre y id del jefe.

    id=Column(Integer, primary_key=True)
    nombre = Column(String)
    
    jefe_id = Column(Integer, ForeignKey('jefe.id'), unique=True)
    jefe = relationship("Jefe", back_populates="oficina")

    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe
        