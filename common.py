from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# FACUNDO, ME DIJISTE QUE LO DEJE ACENTADO ACÁ PARA HACERTE ACUERDO, NO PUDE HACER ANDAR EL PSYCOPG
# PUDE INSTALARLO PERO AL CORRER EL EJEMPLO O EJERCICIO ME TIRA ESTE ERROR:
# ImportError: DLL load failed while importing _psycopg: No se puede encontrar el m▒dulo especificado.

engine = create_engine('postgresql+psycopg2://postgres:test@localhost:5432/tp3-db')
_SessionFactory = sessionmaker(bind=engine)
Base = declarative_base()


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()