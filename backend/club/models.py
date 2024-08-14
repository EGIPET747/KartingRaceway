
from typing import Dict, TYPE_CHECKING
from sqlalchemy import JSON, Column
from sqlmodel import Field, Relationship
from backend.club.configuration import TABLE_PREFIX
from backend.club.schemas.car import CarBase
from backend.club.schemas.club import ClubBase
from backend.club.schemas.raceway import RacewayBase
from backend.common.mixin import TableMixin

if TYPE_CHECKING:
    from backend.session.models import ResultTable, SessionTable


class Club(ClubBase, TableMixin, table=True):
    __tablename__ = TABLE_PREFIX + "club"

    id: int = Field(default=None, primary_key=True)
    description: Dict = Field(default_factory=dict, sa_column=Column(JSON))

    raceways: list["Raceway"] | None = Relationship(back_populates="club", sa_relationship_kwargs={"lazy": "selectin"})

    class Config:
        arbitrary_types_allowed = True
        

class Raceway(RacewayBase, table=True):
    __tablename__ = TABLE_PREFIX + "raceway"

    id: int = Field(default=None, primary_key=True)
    description: Dict = Field(default_factory=dict, sa_column=Column(JSON))

    club_id: int = Field(default=None, foreign_key="club__club.id")
    club: Club = Relationship(back_populates="raceways")

    sessions: list["SessionTable"] = Relationship(back_populates="raceway", sa_relationship_kwargs={"lazy": "selectin"})
    cars: list["Car"] = Relationship(back_populates="raceway", sa_relationship_kwargs={"lazy": "selectin"})

    class Config:
        arbitrary_types_allowed = True


class Car(CarBase, table=True):
    __tablename__ = TABLE_PREFIX + "car"

    id: int = Field(default=None, primary_key=True)
    description: Dict = Field(default_factory=dict, sa_column=Column(JSON))

    raceway_id: int = Field(default=None, foreign_key="club__raceway.id")
    raceway: Raceway = Relationship(back_populates="cars", sa_relationship_kwargs={"lazy": "selectin"})

    results: list["ResultTable"] = Relationship(back_populates="car", sa_relationship_kwargs={"lazy": "selectin"})

    class Config:
        arbitrary_types_allowed = True