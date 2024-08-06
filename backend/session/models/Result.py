import uuid
from typing import Dict
from sqlalchemy import JSON, Column
from sqlmodel import Relationship, SQLModel, Field

from backend.club.models.Car import Car
from backend.session.configuration import TABLE_PREFIX
from backend.session.models.Session import Session
from backend.user.models.Racer import Racer


class ResultBase(SQLModel):
    session_id: int
    car_id: int
    laps: dict[int, float]
    user_id: uuid.UUID


class Result(ResultBase, table=True):
    __tablename__ = TABLE_PREFIX + "result"

    id: int = Field(default=None, primary_key=True)
    laps: Dict = Field(default_factory=dict, sa_column=Column(JSON))

    car_id: int = Field(default=None, foreign_key="club__car.id")
    car: Car = Relationship(back_populates="results")

    racer_id: uuid.UUID = Field(default=None, foreign_key="user__racer.id")
    racer: Racer = Relationship(back_populates="results")
    
    session_id: int = Field(default=None, foreign_key="session__session.id")
    session: Session = Relationship(back_populates="results")

    class Config:
        arbitrary_types_allowed = True


class ResultCreate(ResultBase):
    pass