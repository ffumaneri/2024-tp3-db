from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship
from common import Base


class Aula(Base):
    __tablename__ = 'aulas'

    ##TODO: Insertar acá las columnas id, nombre y relacion con alumno

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    alumno = relationship('Alumno')

    def _init_(self, nombre):
        self.nombre = nombre