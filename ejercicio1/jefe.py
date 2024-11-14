from sqlalchemy import (Column, String, Date, Integer, Numeric, ForeignKey)
from sqlalchemy.orm import relationship
from common import Base


class Jefe(Base):
    __tablename__ = 'jefe'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    oficina = relationship("Oficina", back_populates="jefe",uselist=False)

    ##TODO: Insertar acá las columnas id, nombre y la relación con oficina

    def __init__(self, nombre):
        self.nombre = nombre