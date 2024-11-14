from sqlalchemy import Column, String, Date, Integer, Numeric

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

from common import Base


class Oficina(Base):
    __tablename__ = 'oficina'

    ##TODO: Insertar acá las columnas id, nombre y id del jefe.
    id = Column(Integer, primary_key=True)
    jefe_id = Column(Integer, ForeignKey("jefe.id"))
    jefe = relationship("Jefe",back_populates="oficina")

    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe
        
