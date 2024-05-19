from fastapi import APIRouter

from raceway.api import api_router
from raceway.pages import pages_router

router = APIRouter()
router.include_router(router=api_router, prefix="/api")
router.include_router(router=pages_router, prefix="")
