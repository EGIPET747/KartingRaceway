from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

class TableMixin:

    @classmethod
    async def get(cls, pk, session: AsyncSession) -> Any:
        statement = select(cls).where(cls.id == pk)
        return (await session.execute(statement)).scalars().first()
        
    @classmethod
    async def list(cls, session: AsyncSession, filters = None) -> list[Any]:
        statement = select(cls)
        if filters:
            statement = statement.filter_by(filters)
        return (await session.execute(statement)).scalars().all()
    