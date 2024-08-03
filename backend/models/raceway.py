from typing import Dict
from sqlalchemy import JSON, Column
from sqlmodel import SQLModel, Field


class RaceWayBase(SQLModel):
    city: str
    address: str


class RaceWay(RaceWayBase, table=True):
    id: int = Field(default=None, primary_key=True)
    description: Dict = Field(default_factory=dict, sa_column=Column(JSON))

    class Config:
        arbitrary_types_allowed = True


class RaceWayCreate(RaceWayBase):
    pass