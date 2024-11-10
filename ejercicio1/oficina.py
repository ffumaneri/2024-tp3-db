from sqlalchemy import Column, ForeignKey, String, Date, Integer, Numeric
from sqlalchemy.orm  import relationship
from common import Base

class Oficina(Base):
    __tablename__ = 'oficina'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    jefe_id = Column(Integer, ForeignKey("jefe.id"))
    jefe = relationship("Jefe", back_populates="oficinas")

    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe
        