from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session
from common import Base

# FACUNDO, ME DIJISTE QUE LO DEJE ACENTADO ACÁ PARA HACERTE ACUERDO, NO PUDE HACER ANDAR EL PSYCOPG
# PUDE INSTALARLO PERO AL CORRER EL EJEMPLO O EJERCICIO ME TIRA ESTE ERROR:
# ImportError: DLL load failed while importing _psycopg: No se puede encontrar el m▒dulo especificado.

class Oficina(Base):
    __tablename__ = 'oficinas'


    id = Column(Integer, primary_key=True)
    jefe_id = Column(Integer, ForeignKey("jefes.id"))
    jefe = relationship('Jefe', back_populates='oficina')
    nombre = Column(String(120), nullable=False)
   

    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe