from typing import Dict
from sqlalchemy import JSON, Column
from sqlmodel import Relationship, SQLModel, Field

from backend.club.configuration import TABLE_PREFIX
from backend.club.models.Club import Club


class RacewayBase(SQLModel):
    city: str
    address: str
    description: dict


class Raceway(RacewayBase, table=True):
    __tablename__ = TABLE_PREFIX + "raceway"

    id: int = Field(default=None, primary_key=True)
    description: Dict = Field(default_factory=dict, sa_column=Column(JSON))

    club_id: int = Field(default=None, foreign_key="club__club.id")
    club: Club = Relationship(back_populates="results")

    sessions: list["Session"] = Relationship(back_populates="raceway") # type: ignore
    cars: list["Car"] = Relationship(back_populates="raceway") # type: ignore

    class Config:
        arbitrary_types_allowed = True


class RaceWayCreate(RacewayBase):
    pass
