from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.club.models import Club
from backend.club.schemas.club import ClubItem
from backend.settings.database import get_session

router = APIRouter()


@router.get("/get/")
async def get_club(pk: int, session: AsyncSession = Depends(get_session)) -> ClubItem|None:
    return (await Club.get(pk, session))


@router.get("/list/")
async def get_club_list(session: AsyncSession = Depends(get_session)) -> list[Club]:
    return (await Club.list(session=session))
