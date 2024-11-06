from sqlalchemy import Column, String, Date, Integer, Numeric

from common import Base


class Jefe(Base):
    __tablename__ = 'jefe'

    ##TODO: Insertar acá las columnas id, nombre y la relación con oficina

    def __init__(self, nombre):
        self.nombre = nombre