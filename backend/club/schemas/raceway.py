from sqlmodel import SQLModel


class RacewayBase(SQLModel):
    city: str
    address: str
    description: dict


class RacewayCreate(RacewayBase):
    club_id: int
