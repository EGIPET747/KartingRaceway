import fastapi as F

from raceway import router
from raceway.settings import base

app = F.FastAPI(
    title=base.TITLE,
)

app.include_router(router=router)


@app.get("/")
async def main_page():
    return base.TITLE_FULL
