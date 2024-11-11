from sqlalchemy import Column, String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from common import Base

class Oficina(Base):
    __tablename__ = 'oficina'

    ##TODO: Insertar acá las columnas id, nombre y id del jefe.
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  
    nombre: Mapped[str] = mapped_column(String, nullable=False)  
    jefe_id: Mapped[int] = mapped_column(ForeignKey("jefe.id"))  

    jefe: Mapped["Jefe"] = relationship(back_populates="oficina")

    def __init__(self, nombre, jefe):
        self.nombre = nombre
        self.jefe = jefe
        