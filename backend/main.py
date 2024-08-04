import fastapi as F
from fastapi.middleware.cors import CORSMiddleware

from backend import router
from backend.settings import common

app = F.FastAPI(
    title=common.TITLE,
)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex="http://127.0.0.1:*",
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(router=router, prefix="", tags=[common.TITLE])


@app.get("/")
async def main_page():
    return common.TITLE_FULL
