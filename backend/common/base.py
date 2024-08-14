from fastapi import APIRouter

from backend.common import api
from backend.club.api import club

api_router = APIRouter()
api_router.include_router(api.router, prefix="/base", tags=["base"])
api_router.include_router(club.router, prefix="/club", tags=["club"])