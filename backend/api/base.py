import datetime

from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, MessageType
from broker.schemas import EmailSchema
from broker.settings import conf

router = APIRouter()


@router.get("/current_datetime/")
async def main_page():
    return datetime.datetime.now(tz=datetime.timezone.utc)



@router.post("/email/")
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
