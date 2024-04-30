from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import User


class UserDAL:
    @staticmethod
    async def get_all(session: AsyncSession) -> list[User]:
        stmp = select(User)
        return (await session.scalars(stmp)).all()

    @staticmethod
    async def get_by_id(session: AsyncSession, user_id: int) -> User | None:
        stmp = select(User).where(User.id == user_id)
        return await session.scalar(stmp)

    @staticmethod
    async def get_by_email(session: AsyncSession, email: str) -> User | None:
        stmp = select(User).where(User.email == email)
        return await session.scalar(stmp)
