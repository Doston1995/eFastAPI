from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from db.session import get_db
from typing import List
import datetime, uuid
from db.hashing import Hasher

router = APIRouter()


@router.get("/")
def hello():
    return {"message":"Request"}