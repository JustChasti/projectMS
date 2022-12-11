from loguru import logger
from db.connection import Session
from decorators import default_decorator
from db.models import User
from user.models import UserRegistrModel


@default_decorator('User creation error')
def create_user(user_model: UserRegistrModel):
    user = User(username=user_model.username, password=user_model.password)
    session = Session()
    session.add(user)
    session.commit()
    session.close()
    return {'message': f'User {user_model.username} created'}
