from sqlalchemy import Column, ForeignKey, String, Date, Integer, Numeric

from common import Base


class Alumno(Base):
    __tablename__ = 'alumno'

    ##TODO: Insertar acá las columnas id, nombre, id aula y relaciones con aula 
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    aula_id = Column(Integer, ForeignKey("aula.id"))
    
    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula