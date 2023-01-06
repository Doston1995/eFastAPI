from sqlalchemy import Column, Date, ForeignKey,  String,  Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    id        = Column(String, primary_key=True)
    username  = Column(String(25), unique=True)
    password  = Column(String(255))
    office    = Column(String(25))
    token     = Column(String(255), unique=True, nullable = False)
    is_staff  = Column(Boolean, default = False)
    create_at = Column(String(50))
    request   = relationship('Request', cascade = "all, delete", back_populates = 'user')

    def __repr__(self):
        return f"<User {self.username}>"


class Request(Base):
    __tablename__ = 'requests'

    id        = Column(String, primary_key=True)
    pinpp     = Column(String(14), nullable = True)
    create_at = Column(String(50))
    user_id   = Column(String, ForeignKey('users.id'))
    user      = relationship('User', back_populates = 'request')

    def __repr__(self):
        return f"<User {self.pinpp}>"