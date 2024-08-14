import uuid
from sqlmodel import SQLModel


class ResultBase(SQLModel):
    session_id: int
    car_id: int
    laps: dict[int, float]
    user_id: uuid.UUID


class ResultCreate(ResultBase):
    pass