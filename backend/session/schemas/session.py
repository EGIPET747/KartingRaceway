from datetime import datetime
from sqlmodel import SQLModel


class SessionBase(SQLModel):
    start_datetime: datetime
    club_id: int
    raceway_id: int


class SessionCreate(SessionBase):
    pass