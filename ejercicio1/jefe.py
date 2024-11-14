from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from common import Base

class Jefe(Base):
    __tablename__ = 'jefe'

    id = Column(Integer, primary_key = True)
    nombre = Column(String(50))
    oficina = relationship('Oficina', back_populates = 'jefe', uselist = False)
    
    def __init__(self, nombre):
        self.nombre = nombre
