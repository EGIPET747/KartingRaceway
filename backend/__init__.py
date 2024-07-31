from fastapi import APIRouter

from backend.api import api_router

router = APIRouter()
router.include_router(router=api_router, prefix="/api", tags=["api"])
