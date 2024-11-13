from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session


from common import Base


class Jefe(Base):
    __tablename__ = 'jefes'

    ##TODO: Insertar acá las columnas id, nombre y la relación con oficina

    id = Column(Integer, primary_key=True)
    nombre = Column(String(40), nullable=False)
    oficina = relationship('Oficina', back_populates='jefe',uselist=False)
 ##

    def __init__(self, nombre):
        self.nombre = nombre