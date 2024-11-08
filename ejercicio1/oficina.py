from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from common import Base

class Oficina(Base):
    __tablename__ = 'oficina'
    idoficina = Column(Integer, primary_key=True, autoincrement=True) 
    nombre = Column(String(50))
    idjefe = Column(Integer, ForeignKey('jefe.idjefe'))  


    jefe = relationship("Jefe", back_populates="oficina")

 
    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe  
