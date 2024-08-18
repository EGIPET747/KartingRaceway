import fastapi as F
from fastapi.middleware.cors import CORSMiddleware

from backend.router import router
from backend.settings import configuration

app = F.FastAPI(
    title=configuration.TITLE,
    version=configuration.VERSION,
    swagger_ui_parameters={
        "filter": True,
        "docExpansion": "none",
        "displayRequestDuration": True,
        "tagsSorter": "alpha",
        "operationsSorter": "alpha",
        # "defaultModelsExpandDepth": -1, # Убирает схемы из доки
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex="http://127.0.0.1:*",
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["*"],
)

app.include_router(router=router, prefix="", tags=[configuration.TITLE])


@app.get("/")
async def main_page():
    return configuration.TITLE_FULL
