
from typing import Optional
from sqlmodel import SQLModel


class CarBase(SQLModel):
    photo: Optional[str]
    name: str
    power: float
    description: dict

    raceway_id: int


class CarCreate(CarBase):
    pass