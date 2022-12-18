from datetime import datetime, timedelta
from loguru import logger
import bcrypt
from jose import jwt, ExpiredSignatureError
from db.connection import Session
from decorators import default_decorator
from db.models import User
from config import encrytp_salt, secret_key, algoritm, jwt_exp_days


@default_decorator('autorization error')
def get_user_token(user_model):
    session = Session()
    encrypted_password = bcrypt.hashpw(
        user_model['password'].encode('utf-8'),
        encrytp_salt
    ).decode('utf-8')
    user = session.query(User).filter_by(
        login=user_model['login'],
        password=encrypted_password
    ).scalar()
    session.close()
    if not user:
        return {'message': f'Username or pasword unmatch'}
    data = {
        'login': user.login
    }
    expire = datetime.now() + timedelta(days=jwt_exp_days)
    data.update({"exp": expire})
    token = jwt.encode(data, secret_key, algorithm=algoritm)
    return {"access_token": token}


@default_decorator('autorization error')
def get_user_info(token):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algoritm])
    except ExpiredSignatureError as e:
        print(e)
        return {'message': e}
    session = Session()
    user = session.query(User).filter_by(
        login=payload['login']
    ).scalar()
    session.close()
    data = user.__dict__
    return {'message': data}
