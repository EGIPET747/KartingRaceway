import uuid
from typing import Dict, Optional
from sqlalchemy import JSON, Column
from sqlmodel import SQLModel, Field, Relationship

from backend.user.configuration import TABLE_PREFIX


class RacerBase(SQLModel):
    avatar: Optional[str]
    name: str
    second_name: str
    phone: str
    email: str
    description: dict


class Racer(RacerBase, table=True):
    __tablename__ = TABLE_PREFIX + "racer"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    description: Dict = Field(default_factory=dict, sa_column=Column(JSON))

    results: list["Result"] = Relationship(back_populates="racer") # type: ignore

    class Config:
        arbitrary_types_allowed = True


class RacerCreate(RacerBase):
    pass