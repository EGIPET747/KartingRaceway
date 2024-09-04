from fastapi import APIRouter, Body, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from backend.club.models import Raceway
from backend.club.schemas.raceway import RacewayBase, RacewayCreate
from backend.settings.database import get_session

router = APIRouter()


@router.delete("/")
async def delete_raceway(pk: int = Body(), session: AsyncSession = Depends(get_session)) -> None:
    return (await Raceway.delete(pk, session))


@router.post("/", status_code=201)
async def create_raceway(data: RacewayCreate = Body(), session: AsyncSession = Depends(get_session)) -> None:
    return (await Raceway.create(data, session))