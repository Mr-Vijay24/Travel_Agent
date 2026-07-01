from pydantic import BaseModel,EmailStr,Field

class UserRegister(BaseModel):
    name:str
    email:EmailStr
    password:str = Field(
        min_length=8,
        max_length=72
    )

class UserResponse(BaseModel):# imagine this api  is a POST/register response in it password then ,it is huge security problem
    id:int
    name:str
    email:EmailStr

    class Config:
        from_attributes = True# u can use this to convert the orm model to pydantic model
# Notice that Pydantic and SQLAlchemy have different responsibilities:

# Pydantic → Handles API requests and responses.
# SQLAlchemy → Handles database storage and retrieval.