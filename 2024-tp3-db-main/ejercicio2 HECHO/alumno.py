from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from common import Base

class Alumno(Base):
    __tablename__ = 'alumno'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Clave primaria
    nombre = Column(String, nullable=False)
    aula_id = Column(Integer, ForeignKey('aula.id'), nullable=False)  # Llave foránea a la tabla `aula`

    # Relación con Aula, lado del alumno (Many-to-One)
    aula = relationship("Aula", back_populates="alumnos")

    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula

    def __repr__(self):
        return f"<Alumno(id={self.id}, nombre='{self.nombre}', aula={self.aula.nombre})>"
