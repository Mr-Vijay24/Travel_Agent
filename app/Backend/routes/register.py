# The route's only job is to receive the request and call the service.
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from database.database import get_db
from schemas.user import UserRegister,UserResponse
from services.auth_service import register_user

router = APIRouter(
    prefix = "/auth",
    tags=[
        "Authentication"
    ]
)

@router.post(
    "/register",
    response_model = UserResponse
)
def register(user : UserRegister , db : Session = Depends(get_db)):
    return register_user(user,db)