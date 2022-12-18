from loguru import logger
import bcrypt
from db.connection import Session
from decorators import default_decorator
from db.models import User
from user.models import UserRegistrModel
from config import encrytp_salt


@default_decorator('User creation error')
def create_user(user_model: UserRegistrModel):
    encrypted_password = bcrypt.hashpw(
        user_model.password.encode('utf-8'),
        encrytp_salt
    ).decode('utf-8')
    user = User(
        name=user_model.name,
        surname=user_model.surname,
        phone=user_model.phone,
        login=user_model.login,
        password=encrypted_password,
    )
    session = Session()
    session.add(user)
    session.commit()
    session.close()
    return {'message': f'User {user_model.name} created'}
