from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from common import Base


class Oficina(Base):
    __tablename__ = "oficina"

    ##TODO: Insertar acá las columnas id, nombre y id del jefe.
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    id_jefe = Column(Integer, ForeignKey("jefe.id"))
    # Relacion 1 a 1 estricta, uso back_populates para que 1 jefe tenga 1 oficina y uso useList false para que SQLAlchemy interprete que no es 1 a N
    jefe = relationship("Jefe", back_populates="oficina", uselist=False)

    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe  # id jefe
