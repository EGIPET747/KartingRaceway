
from typing import Any, Dict, TYPE_CHECKING
from sqlalchemy import JSON, Column
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Field, Relationship, select
from backend.club.configuration import TABLE_PREFIX
from backend.club.schemas.car import CarBase
from backend.club.schemas.club import ClubBase
from backend.club.schemas.raceway import RacewayBase
from backend.common.mixin import StatusMixin, TableMixin

if TYPE_CHECKING:
    from backend.session.models import Result, Session


class Club(ClubBase, TableMixin, StatusMixin, table=True):
    __tablename__ = TABLE_PREFIX + "club"

    id: int = Field(default=None, primary_key=True)
    description: Dict = Field(default_factory=dict, sa_column=Column(JSON))

    raceways: list["Raceway"] | None = Relationship(back_populates="club", sa_relationship_kwargs={"lazy": "selectin"})

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    async def get(cls, pk, session: AsyncSession) -> Any:
        statement = select(cls).join(Raceway).where(cls.id == pk)
        return (await session.execute(statement)).scalars().first()


class Raceway(RacewayBase, StatusMixin, table=True):
    __tablename__ = TABLE_PREFIX + "raceway"

    id: int = Field(default=None, primary_key=True)
    description: Dict = Field(default_factory=dict, sa_column=Column(JSON))

    club_id: int = Field(default=None, foreign_key="club__club.id")
    club: Club = Relationship(back_populates="raceways")

    sessions: list["Session"] = Relationship(back_populates="raceway")
    cars: list["Car"] = Relationship(back_populates="raceway")

    class Config:
        arbitrary_types_allowed = True


class Car(CarBase, StatusMixin, table=True):
    __tablename__ = TABLE_PREFIX + "car"

    id: int = Field(default=None, primary_key=True)
    description: Dict = Field(default_factory=dict, sa_column=Column(JSON))

    raceway_id: int = Field(default=None, foreign_key="club__raceway.id")
    raceway: Raceway = Relationship(back_populates="cars")

    results: list["Result"] = Relationship(back_populates="car")

    class Config:
        arbitrary_types_allowed = True