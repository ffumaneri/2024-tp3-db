from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session
from common import Base

# FACUNDO, ME DIJISTE QUE LO DEJE ACENTADO ACÁ PARA HACERTE ACUERDO, NO PUDE HACER ANDAR EL PSYCOPG
# PUDE INSTALARLO PERO AL CORRER EL EJEMPLO O EJERCICIO ME TIRA ESTE ERROR:
# ImportError: DLL load failed while importing _psycopg: No se puede encontrar el m▒dulo especificado.


class Jefe(Base):
    __tablename__ = 'jefes'

    ##acá se arma la tabla y la relación con oficina. En esta relación este  no lleva FK, porque lo lleva oficina

    id = Column(Integer, primary_key=True)
    nombre = Column(String(40), nullable=False)
    oficina = relationship('Oficina', back_populates='jefe',uselist=False)
 


    def __init__(self, nombre):
        self.nombre = nombre