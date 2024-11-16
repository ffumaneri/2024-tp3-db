from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:admin@localhost:5433/tp3-db')

Base = declarative_base()

_SessionFactory = sessionmaker(bind=engine)

def session_factory():
    return _SessionFactory()