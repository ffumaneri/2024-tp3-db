from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#cambie el puerto a 5433 porque me decia que lo tenia ocupado al otro.
engine = create_engine('postgresql://dbuser:dbpassword@localhost:5433/tp3-db')


# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()