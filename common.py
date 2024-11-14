from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#engine = create_engine('postgresql://#dbuser:dbpassword@localhost:5432/tp3-db')

#direccion bd
URL_DATABASE = 'postgresql://Simón://postgres@localhost:5432/tp3-db'
engine = create_engine(URL_DATABASE)

# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()

def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()