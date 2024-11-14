from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from common import Base

class Oficina(Base):
    __tablename__ = 'oficina'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    id_jefe = Column(Integer, ForeignKey('jefe.id'))
    jefe = relationship('Jefe', back_populates = 'oficina', uselist = False)

    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe
