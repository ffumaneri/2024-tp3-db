from sqlalchemy import Column, String, Date, Integer, Numeric
from sqlalchemy.orm import relationship

from common import Base


class Jefe(Base):
    __tablename__ = 'jefe'

    ##TODO: Insertar acá las columnas id, nombre y la relación con oficina
    
    id=Column(Integer, primary_key=True)
    nombre = Column(String)

    oficina = relationship("Oficina", uselist=False, back_populates="jefe")

    def __init__(self, nombre):
        self.nombre = nombre