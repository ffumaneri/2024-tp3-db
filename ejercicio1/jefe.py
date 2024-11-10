from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from common import Base

class Jefe(Base):
    __tablename__ = 'jefe'

    id = Column(Integer, primary_key=True)  # Columna id
    nombre = Column(String)  # Columna nombre

    # Relación uno a uno con la clase Oficina
    oficina = relationship("Oficina", back_populates="jefe", uselist=False) 

    def __init__(self, nombre):
        self.nombre = nombre
