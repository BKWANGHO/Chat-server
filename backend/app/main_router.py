from fastapi import APIRouter
from app.api.titanic.web.titanic_router import router as titanic_router

router = APIRouter()

router.include_router(titanic_router,prefix="/chat")