
from typing import Dict, Optional
from sqlalchemy import JSON, Column
from sqlmodel import Field, Relationship, SQLModel

from backend.club.configuration import TABLE_PREFIX
from backend.club.models.Raceway import Raceway


class CarBase(SQLModel):
    photo: Optional[str]
    name: str
    power: float
    description: dict

    raceway_id: int


class Car(CarBase, table=True):
    __tablename__ = TABLE_PREFIX + "car"

    id: int = Field(default=None, primary_key=True)
    description: Dict = Field(default_factory=dict, sa_column=Column(JSON))

    raceway_id: int = Field(default=None, foreign_key="club__raceway.id")
    raceway: Raceway = Relationship(back_populates="cars")

    results: list["Result"] = Relationship(back_populates="car") # type: ignore

    class Config:
        arbitrary_types_allowed = True


class CarCreate(CarBase):
    pass