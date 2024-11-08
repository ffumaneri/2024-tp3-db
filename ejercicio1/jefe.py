from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from common import Base

class Jefe(Base):
    __tablename__ = 'jefe'
    idjefe = Column(Integer, primary_key=True, autoincrement=True)  # Autoincremento para el id
    nombre = Column(String(50))
    apellido = Column(String(50))

    # Relación con Oficina
    oficina = relationship("Oficina", back_populates="jefe", uselist=False)

    # Constructor simplificado
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

