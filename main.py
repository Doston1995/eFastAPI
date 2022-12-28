from fastapi import FastAPI
from routers.base import api_router
from core.config import settings
from db.session import engine
from db.models import Base

def include_router(app):
    app.include_router(api_router, prefix="/api/v1")


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    create_tables()
    return app 


app = start_application()