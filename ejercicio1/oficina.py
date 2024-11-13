from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session

from common import Base


class Oficina(Base):
    __tablename__ = 'oficinas'

    ##TODO: Insertar acá las columnas id, nombre y id del jefe.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)
    jefe = relationship('Jefe', back_populates='oficina')
    id_jefe = Column(Integer, ForeignKey("jefes.id"))
       


    ##

    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe
        