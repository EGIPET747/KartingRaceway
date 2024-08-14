from typing import Optional
from sqlmodel import SQLModel


class RacerBase(SQLModel):
    avatar: Optional[str]
    name: str
    second_name: str
    phone: str
    email: str
    description: dict


class RacerCreate(RacerBase):
    pass