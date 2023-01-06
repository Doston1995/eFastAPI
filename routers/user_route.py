from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from db.session import get_db
from typing import List
from db.models import User
from schemas.users import CreateUser, ShowUser
import datetime, uuid
from db.hashing import Hasher
import secrets


router = APIRouter()


@router.get("/all", response_model=List[ShowUser])
def get_all_users(db:Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.post("/create/",status_code = status.HTTP_201_CREATED, response_model=ShowUser)
def create_users(user: CreateUser, db: Session = Depends(get_db)):
    db_username = db.query(User).filter(User.username == user.username).first()
    if db_username is not None:
        return HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
            detail = "This username already exist")
    user_date      = str(datetime.datetime.now())
    user_id        = str(uuid.uuid1())
    user_token     = secrets.token_hex(64)
    user_object = User(
        id         = user_id,
        username   = user.username,
        password   = Hasher.get_password_hash(user.password),
        office     = user.office,
        token      = user_token,
        create_at  = user_date,
        is_staff   = user.is_staff,
    )
    db.add(user_object)
    db.commit()
    db.refresh(user_object)
    return user_object