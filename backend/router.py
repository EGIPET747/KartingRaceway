from fastapi import APIRouter

from backend.common.base import api_router

router = APIRouter()
router.include_router(router=api_router, prefix="/api", tags=["api"])
