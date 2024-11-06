from sqlalchemy import Column, String, Date, Integer, Numeric

from common import Base


class Alumno(Base):
    __tablename__ = 'alumno'

    ##TODO: Insertar acá las columnas id, nombre, id aula y relaciones con aula

    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula