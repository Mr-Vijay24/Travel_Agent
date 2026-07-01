from database.models import User
from sqlalchemy.orm import Session
from schemas.user import UserRegister
from fastapi import HTTPException
from services.security import hash_password

def register_user(user: UserRegister,db: Session):
    existing_user = db.query(User).filter(User.email == user.email).first()
    # filter is like where in sql email = "email@gmail.com" and first() is like limit 1 in sql
    if existing_user:
       # raise ValueError("User with this email already exists")
       raise HTTPException(
           status_code=400,
           detail="email already registered"
       )
    hashed_password = hash_password(user.password)
    new_user = User(
        name = user.name,
        email = user.email,
        password = hashed_password
    )

    db.add(new_user) # it tell sqlaichemy track thhis object so it can be inserted
    db.commit() # it add the object to the database
    db.refresh(new_user)

    return new_user