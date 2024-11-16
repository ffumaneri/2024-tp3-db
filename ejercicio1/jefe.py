from sqlalchemy import Column, String, Integer, ForeignKey
from common import Base
from sqlalchemy.orm import relationship

from ejercicio1.oficina import Oficina

class Jefe(Base):
    __tablename__ = 'jefe'

    ##TODO: Insertar acá las columnas id, nombre y la relación con oficina

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))

    oficina = relationship("Oficina", back_populates="jefe")

    def __init__(self, nombre):
        self.nombre = nombre