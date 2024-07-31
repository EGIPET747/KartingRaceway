from fastapi import APIRouter

from backend.api import base

api_router = APIRouter()
api_router.include_router(base.router, prefix="/base", tags=["base"])