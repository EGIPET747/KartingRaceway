

from typing import Dict, TYPE_CHECKING
import uuid

from sqlalchemy import JSON, Column
from sqlmodel import Field, Relationship
from backend.user.configuration import TABLE_PREFIX
from backend.user.schemas.racer import RacerBase

if TYPE_CHECKING:
    from backend.session.models import Result


class Racer(RacerBase, table=True):
    __tablename__ = TABLE_PREFIX + "racer"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    description: Dict = Field(default_factory=dict, sa_column=Column(JSON))

    results: list["Result"] = Relationship(back_populates="racer")

    class Config:
        arbitrary_types_allowed = True