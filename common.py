from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine('postgresql://postgres:admin@localhost:5432/tp3-db')

_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()

def session_factory():
    try:
        Base.metadata.create_all(engine)
        return _SessionFactory()
    except SQLAlchemyError as e:
        print(f"Error al crear las tablas : {e}")
        raise