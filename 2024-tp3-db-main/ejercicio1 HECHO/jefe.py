from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Jefe(Base):
    __tablename__ = 'jefe'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)

    oficina = relationship("Oficina", back_populates="jefe", uselist=False)

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return f"<Jefe(id={self.id}, nombre='{self.nombre}')>"

##NO PUDE HACERLO CORRER