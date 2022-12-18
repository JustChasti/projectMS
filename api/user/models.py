from pydantic import BaseModel, validator, constr
from db.connection import Session
from db.models import User
import phonenumbers


class UserRegistrModel(BaseModel):
    name: constr(max_length=64)
    surname: constr(max_length=64)
    phone: constr(min_length=11, max_length=14)
    login: constr(max_length=64)
    password: constr(max_length=64)

    @validator('login')
    def check_login(login):
        session = Session()
        user = session.query(User).filter_by(login=login).scalar()
        session.close()
        if user:
            raise ValueError('User already existed')
        return login

    @validator('phone')
    def check_phone(phone):
        session = Session()
        user = session.query(User).filter_by(phone=phone).scalar()
        session.close()
        if user:
            raise ValueError('User already existed')
        return phone
