from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from user.models import UserRegistrModel
from user.creation import create_user
from user.autorization import get_user_token, get_user_info


user_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/token")


@user_router.post('/user/create', response_class=JSONResponse)
async def creation(user: UserRegistrModel):
    return create_user(user)


@user_router.get('/user/info', response_class=JSONResponse)
async def get_my_info(token: str):
    return get_user_info(token)


@user_router.get('/user/token', response_class=JSONResponse)
async def get_token(username: str, password: str):
    return get_user_token({'username': username, 'password': password})
