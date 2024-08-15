
from typing import Dict
import uuid
from sqlalchemy import JSON, Column
from sqlmodel import Field, Relationship
from backend.club.models import Car, Raceway
from backend.session.configuration import TABLE_PREFIX
from backend.session.schemas.result import ResultBase
from backend.session.schemas.session import SessionBase
from backend.user.models import Racer


class Session(SessionBase, table=True):
    __tablename__ = TABLE_PREFIX + "session"

    id: int = Field(default=None, primary_key=True)
    description: Dict = Field(default_factory=dict, sa_column=Column(JSON))

    raceway_id: int = Field(default=None, foreign_key="club__raceway.id")
    raceway: Raceway = Relationship(back_populates="sessions")

    results: list["Result"] = Relationship(back_populates="session") # type: ignore

    class Config:
        arbitrary_types_allowed = True


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
