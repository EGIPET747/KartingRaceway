from datetime import datetime
from typing import Dict
from sqlalchemy import JSON, Column
from sqlmodel import Relationship, SQLModel, Field

from backend.club.models.Raceway import Raceway
from backend.session.configuration import TABLE_PREFIX


class SessionBase(SQLModel):
    start_datetime: datetime
    club_id: int
    raceway_id: int


class Session(SessionBase, table=True):
    __tablename__ = TABLE_PREFIX + "session"

    id: int = Field(default=None, primary_key=True)
    description: Dict = Field(default_factory=dict, sa_column=Column(JSON))

    raceway_id: int = Field(default=None, foreign_key="club__raceway.id")
    raceway: Raceway = Relationship(back_populates="sessions")

    results: list["Result"] = Relationship(back_populates="session") # type: ignore

    class Config:
        arbitrary_types_allowed = True


class SessionCreate(SessionBase):
    pass