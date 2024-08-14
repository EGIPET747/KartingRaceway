from typing import Any, Optional
from sqlmodel import SQLModel

from backend.club.schemas.raceway import RacewayBase


class ClubBase(SQLModel):
    logo: Optional[str]
    name: str
    description: dict


class ClubCreate(ClubBase):
    pass
