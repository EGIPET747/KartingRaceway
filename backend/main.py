import fastapi as F
from fastapi.middleware.cors import CORSMiddleware

from backend import router

from backend.settings import base

app = F.FastAPI(
    title=base.TITLE,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=router, prefix="", tags=["krw"])


@app.get("/")
async def main_page():
    return base.TITLE_FULL
