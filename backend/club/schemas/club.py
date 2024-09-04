from typing import Optional

from pydantic import BaseModel
from backend.common.mixin import _Status
from sqlmodel import SQLModel

from backend.club.schemas.raceway import RacewayBase


class ClubBase(SQLModel):
    id: Optional[int]
    logo: Optional[str]
    name: str
    description: dict
    status: str


class ClubItem(ClubBase):
    raceways: list[RacewayBase]


class ClubCreate(BaseModel):
    name: str
    description: dict
    status: _Status = _Status.active
