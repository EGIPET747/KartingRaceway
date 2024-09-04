import enum
from typing import Any, Optional

from pydantic import BaseModel
from sqlalchemy import Enum
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Field, select

class TableMixin:
    @classmethod
    async def get(cls, pk, session: AsyncSession) -> Any:
        statement = select(cls).where(cls.id == pk)
        return (await session.execute(statement)).scalars().first()
        
    @classmethod
    async def list(cls, session: AsyncSession, filters = None) -> list[Any]:
        statement = select(cls).where(cls.status != _Status.deleted.value)
        if filters:
            statement = statement.filter(filters)
        return (await session.execute(statement)).scalars().all()
    
    
    @classmethod
    async def delete(cls, pk: int, session: AsyncSession) -> None:
        statement = select(cls).where(cls.id == pk)
        item = (await session.execute(statement)).scalars().first()

        if not item:
            raise ValueError("Item not found")

        item.status = _Status.deleted
        await session.commit()

    
    @classmethod
    async def create(cls, data: BaseModel, session: AsyncSession) -> Any:
        item = cls(**data.__dict__)
        session.add(item)
        await session.commit()


class _Status(str, enum.Enum):
    active = "Активен"
    inactive = "Выключен"
    deleted = "Удален"


class StatusMixin:
    status: Optional[_Status] = Field(sa_type=Enum(_Status))
