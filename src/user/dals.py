from sqlalchemy import select, update as sql_update
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserPutInput, UserPatchInput
from .models import User


class UserDAL:
    @staticmethod
    async def get_all(session: AsyncSession) -> list[User | None]:
        stmp = select(User)
        print(type(session), session)
        return await session.scalars(stmp)

    @staticmethod
    async def get_by_id(session: AsyncSession, user_id: int) -> User | None:
        stmp = select(User).where(User.id == user_id)
        return await session.scalar(stmp)

    @staticmethod
    async def get_by_email(session: AsyncSession, email: str) -> User | None:
        stmp = select(User).where(User.email == email)
        return await session.scalar(stmp)

    @staticmethod
    async def create(session: AsyncSession, user: User) -> User:
        session.add(user)
        await session.commit()
        # await session.refresh(product)
        return user

    @staticmethod
    async def update(
        session: AsyncSession,
        user: User,
        user_update: UserPutInput | UserPatchInput,
        # partial: bool,
    ) -> User | None:
        for name, value in vars(user_update).items():
            if value:
                setattr(user, name, value)
        await session.commit()
        return user

    @staticmethod
    async def delete(session: AsyncSession, user: User) -> None:
        await session.delete(user)
        await session.commit()