from typing import Dict, Optional
from sqlalchemy import JSON, Column
from sqlmodel import Relationship, SQLModel, Field

from backend.club.configuration import TABLE_PREFIX


class ClubBase(SQLModel):
    logo: Optional[str]
    name: str
    description: dict


class Club(ClubBase, table=True):
    __tablename__ = TABLE_PREFIX + "club"

    id: int = Field(default=None, primary_key=True)
    description: Dict = Field(default_factory=dict, sa_column=Column(JSON))

    raceways: list["Raceway"] = Relationship(back_populates="club") # type: ignore

    class Config:
        arbitrary_types_allowed = True


class ClubCreate(ClubBase):
    pass
