from sqlalchemy import Column, String, Date, Integer, Numeric
from sqlalchemy.orm import declarative_base, relationship, Session, Mapped

from common import Base


class Jefe(Base):
    __tablename__ = 'jefe'

    ##TODO: Insertar acá las columnas id, nombre y la relación con oficina
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120))
    oficina = relationship("Oficina", back_populates="jefe",uselist=False)


    def __init__(self, nombre):
        self.nombre = nombre