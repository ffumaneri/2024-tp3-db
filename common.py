from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQALCHEMY_DATABASE_URL = 'postgresql://postgres:admin@localhost:5432/tp3-db'

engine = create_engine(SQALCHEMY_DATABASE_URL)
# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()
