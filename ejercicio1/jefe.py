from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from common import Base


class Jefe(Base):
    __tablename__ = "jefe"

    ##TODO: Insertar acá las columnas id, nombre y la relación con oficina
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    # Relacion 1 a 1 estricta, uso back_populates para que 1 jefe tenga 1 oficina y uso useList false para que SQLAlchemy interprete que no es 1 a N
    oficina = relationship("Oficina", back_populates="jefe", uselist=False)

    def __init__(self, nombre):
        self.nombre = nombre
