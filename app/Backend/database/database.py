from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from .config import DATABASE_URL 

engine = create_engine(DATABASE_URL) # it is sqlalchemy;s gateway to the db
# without engine , py doesn't know where u db is and how to connent it
# think engine as a manager
SessionLocal = sessionmaker( # it create a factory that can produce db sessions
    autocommit = False,
    autoflush = False,
    bind = engine
)

Base = declarative_base() # it is a base class for all our models

def get_db():
    db = SessionLocal() # it creates a new session for each request
    try:
        yield db # it is a generator fun that yields a db session to the caller
    finally:
        db.close() # it closes the session after the request is done 