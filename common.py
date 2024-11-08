from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/tplab?client_encoding=utf8"
engine = create_engine(DATABASE_URL, connect_args={"client_encoding": "utf8"})
Session = sessionmaker(bind=engine)

Base = declarative_base()

def session_factory():
    return Session()
