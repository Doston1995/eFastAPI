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
    is_staff  = Column(Boolean, default = False)
    create_at = Column(String(50))

    def __repr__(self):
        return f"<User {self.username}>"