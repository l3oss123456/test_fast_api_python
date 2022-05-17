from fastapi import APIRouter
from model.login import LoginModel
import jwt
import time

router = APIRouter(
    prefix="/login",
    # tags=["User"],
    responses={404: {"description": "Not found"}},
)

SECRET_KEY = 'SECRET_KEY'


@router.post('/')
def login(user: LoginModel):
    payload = {
        "username": user.username,
        "password": user.password,
        "role": user.role,
        "start_time": time.time()
    }
    encode_jwt = jwt.encode(payload,
                            SECRET_KEY, algorithm="HS256")
    return {"token": encode_jwt}
