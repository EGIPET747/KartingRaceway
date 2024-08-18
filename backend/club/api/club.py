from fastapi import APIRouter, Body, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from backend.club.models import Club
from backend.club.schemas.club import ClubItem
from backend.settings.database import get_session

router = APIRouter()


@router.get("/")
async def get_club(pk: int = Query(), session: AsyncSession = Depends(get_session)) -> ClubItem|None:
    return (await Club.get(pk, session))


@router.get("/list/")
async def get_club_list(session: AsyncSession = Depends(get_session)) -> list[ClubItem]:
    return (await Club.list(session=session))


@router.delete("/")
async def delete_club(pk: int = Body(), session: AsyncSession = Depends(get_session)) -> None:
    return (await Club.delete(pk, session))