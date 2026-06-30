from sqlalchemy import Column, Integer , String,TIMESTAMP,text

from .database import Base

class User(Base):
    __tablename__ = "users"

    id  = Column(
        Integer,#data type
        primary_key=True,# it is a primary key for the table
        index=True# for fast acess to the data
    )
    email = Column(
        String(100),
        unique=True,
        nullable = False# it is a required field
    )
    password = Column(
        String(100),
        nullable = False
    )
    created_at  = Column(
         TIMESTAMP,
         server_default = text("CURRENT_TIMESTAMP")
    )

