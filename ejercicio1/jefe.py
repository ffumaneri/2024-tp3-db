
from sqlalchemy import Column, ForeignKey, String, Date, Integer, Numeric
from sqlalchemy.orm import relationship

from common import Base


class Jefe(Base):
    __tablename__ = 'jefe'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    oficinas = relationship("Oficina", back_populates="jefe")
       
    def __init__(self, nombre):
        self.nombre = nombre