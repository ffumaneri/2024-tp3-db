from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from common import Base

class Oficina(Base):
    __tablename__ = 'oficina'
    idoficina = Column(Integer, primary_key=True, autoincrement=True)  # Autoincremento para el id
    nombre = Column(String(50))
    idjefe = Column(Integer, ForeignKey('jefe.idjefe'))  # Relación con la tabla jefe

    # Relación con Jefe
    jefe = relationship("Jefe", back_populates="oficina")

    # Constructor simplificado
    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe  # Puedes pasar un objeto Jefe directamente
