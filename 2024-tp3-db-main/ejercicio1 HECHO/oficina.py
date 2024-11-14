from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from .jefe import Jefe

Base = declarative_base()

class Oficina(Base):
    __tablename__ = 'oficina'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    jefe_id = Column(Integer, ForeignKey('jefe.id'), nullable=False)

    jefe = relationship("Jefe", back_populates="oficina")

    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe

    def __repr__(self):
        return f"<Oficina(id={self.id}, nombre='{self.nombre}', jefe={self.jefe})>"

##NO PUDE HACERLO CORRER