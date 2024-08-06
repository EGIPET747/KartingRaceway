from fastapi import APIRouter

from backend.common import api

api_router = APIRouter()
api_router.include_router(api.router, prefix="/base", tags=["base"])