from sqlalchemy import String, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column
from common import Base
from oficina import Oficina


class Jefe(Base):
    __tablename__ = 'jefe'

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    oficina: Mapped["Oficina"] = relationship(back_populates="jefe")

    def __init__(self, nombre):
        self.nombre = nombre