from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from common import Base
# from .jefe import Jefe


class Oficina(Base):
    __tablename__ = 'oficina'

    id = Column(Integer, primary_key=True)  
    nombre = Column(String)  
    jefe_id = Column(Integer, ForeignKey('jefe.id')) 

    jefe = relationship('Jefe', back_populates='oficina')


    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe
        