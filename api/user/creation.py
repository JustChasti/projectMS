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
    user = User(username=user_model.username, password=encrypted_password)
    session = Session()
    session.add(user)
    session.commit()
    session.close()
    return {'message': f'User {user_model.username} created'}
