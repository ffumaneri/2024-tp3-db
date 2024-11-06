from sqlalchemy import Column, String, Date, Integer, Numeric

from common import Base


class Oficina(Base):
    __tablename__ = 'oficina'

    ##TODO: Insertar acá las columnas id, nombre y id del jefe.

    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe
        