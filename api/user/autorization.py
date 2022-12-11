from loguru import logger
from db.connection import Session
from decorators import default_decorator
from db.models import User


@default_decorator('autorization error')
def get_user_token(user_model):
    session = Session()
    user = session.query(User).filter_by(
        username=user_model['username'],
        password=user_model['password']
    ).scalar()
    session.close()
    if not user:
        return {'message': f'Username or pasword unmatch'}
    return {"access_token": user.username, "token_type": "bearer"}
