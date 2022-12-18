from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64))
    surname = Column(String(64))
    password = Column(String(64))
    phone = Column(String(16))
    login = Column(String(64))
