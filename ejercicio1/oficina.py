from sqlalchemy import Column, String, Date, Integer, Numeric
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from common import Base


class Oficina(Base):
    __tablename__ = 'oficina'

    
    id= Column(Integer, primary_key=True) #Columna id
    nombre = Column(String) #Columna nombre
    id_jefe= Column(Integer, ForeignKey('jefe.id')) #Columna id_jefe

    # referencia inversa 
    jefe = relationship("Jefe", back_populates="oficina")

    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe
        