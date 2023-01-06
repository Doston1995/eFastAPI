from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from db.session import get_db
from typing import List
import datetime, uuid
from db.hashing import Hasher
from schemas.requests import ShowRequest, CreateRequest
from db.models import Request, User
from core.config import settings
from routers.login_route import get_current_user_from_token
import requests

router = APIRouter()


@router.get("/all", response_model=List[ShowRequest])
def get_all_request(db:Session = Depends(get_db)):
    all_request = db.query(Request).all()
    return all_request



@router.post("/create/", status_code = status.HTTP_201_CREATED)
def create_request(request: CreateRequest, user:User = Depends(get_current_user_from_token), db: Session = Depends(get_db)):
    URL = settings.URL
    payload = {
                "pinpp": f"{request.pinpp}",
                "secret": settings.SERVICE_SECRET_KEY
              }
    response = requests.post(URL, json = payload)
    if response.json()['status']['code'] == 200:
        data = response.json()['data']
        status = response.json()['status']['code']
        message = response.json()['status']['message']
        return {"data": data, "status":status, "message":message}
    elif response.json()['status']['code'] == 500:
        data = response.json()['data']
        status = response.json()['status']['code']
        message = response.json()['status']['message']
        return {"data": data, "status":status, "message":message}
    elif response.json()['status']['code'] == 204:
        data = response.json()['data']
        status = response.json()['status']['code']
        message = response.json()['status']['message']
        return {"data": data, "status":status, "message":message}
    # request_date      = str(datetime.datetime.now())
    # request_id        = str(uuid.uuid1())
    # user_id           = user
    # request_object = Request(
    #     id         = request_id,
    #     pinpp      = request.pinpp,
    #     user_id    = user,
    #     create_at  = request_date,
    # )
    # db.add(request_object)
    # db.commit()
    # db.refresh(request_object)