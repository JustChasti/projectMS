from pydantic import BaseModel, validator
from db.connection import Session
from db.models import User


class UserRegistrModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def check_name(username):
        session = Session()
        user = session.query(User).filter_by(username=username).scalar()
        session.close()
        if user:
            raise ValueError('User already existed')
        return username
