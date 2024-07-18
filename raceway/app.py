import fastapi as F
from fastapi import BackgroundTasks

from broker.schemas import EmailSchema
from broker.settings import conf
from raceway import router

from raceway.settings import base

from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, MessageType


app = F.FastAPI(
    title=base.TITLE,
)

app.include_router(router=router)


@app.get("/")
async def main_page():
    return base.TITLE_FULL


@app.post("/email")
async def simple_send(
    background_tasks: BackgroundTasks,
    email: EmailSchema
) -> JSONResponse:
    html = """<p>Тестируем работу библиотеки Fastapi-mail</p> """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.model_dump().get("email"),
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)

    return JSONResponse(status_code=200, content={"message": "email has been sent"})
