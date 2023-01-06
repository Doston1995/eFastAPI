from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from datetime import timedelta
from fastapi import status,HTTPException
from db.session import get_db
from db.hashing import Hasher
from schemas.tokens import Token
from core.security import create_access_token
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from db.models import User 
from schemas.login import LoginSchema
router = APIRouter()


def get_user(username:str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    return user


def authenticate_user(username: str, password: str, db: Session):
    user = get_user(username=username, db=db)
    if not user:
        return False
    if not Hasher.verify_password(password, user.password):
        return False
    return user


@router.post("/token")
def login_for_access_token(login: LoginSchema,db: Session= Depends(get_db)):
    user = authenticate_user(login.username, login.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    user_token = user.token
    return {"access_token": user_token, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login/token")


def get_current_user_from_token(token: str = Depends(oauth2_scheme), db: Session=Depends(get_db)): 
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    user = db.query(User).filter(User.token == token).first()
    if user is None:
        raise credentials_exception
    return user.id