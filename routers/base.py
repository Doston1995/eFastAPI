from fastapi import APIRouter
from routers import user_route, login_route,request_route

api_router = APIRouter()



api_router.include_router(login_route.router,    prefix="/login",tags=["login"])
api_router.include_router(user_route.router,     prefix="/user",tags=["user"])
api_router.include_router(request_route.router,  prefix="/request",tags=["request"])