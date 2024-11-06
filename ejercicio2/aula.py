from sqlalchemy import Column, String, Date, Integer, Numeric

from common import Base


class Aula(Base):
    __tablename__ = 'aula'

    ##TODO: Insertar acá las columnas id, nombre y relacion con alumno

    def __init__(self, nombre):
        self.name = nombre
        