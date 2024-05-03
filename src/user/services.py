import email
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from .dals import UserDAL
from .schemas import UserOutput
from .schemas import UserCreateInput
from .schemas import UserPatchInput
from .schemas import UserPutInput
from .models import User


class UserService:
    @staticmethod
    async def get_all(session: AsyncSession) -> list[UserOutput | None]:
        users: list[User | None] = await UserDAL.get_all(session=session)
        return [UserOutput(name=user.name, email=user.email) for user in users]

    @staticmethod
    async def get_by_id(
        session: AsyncSession, user_id: int
    ) -> UserOutput | HTTPException:
        user: User | None = await UserDAL.get_by_id(session=session, user_id=user_id)
        if user:
            return UserOutput(name=user.name, email=user.email)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user_id} not found!",
        )

    @staticmethod
    async def get_by_email(
        session: AsyncSession, email: str
    ) -> UserOutput | HTTPException:
        user: User | None = await UserDAL.get_by_email(session=session, email=email)
        if user:
            return UserOutput(name=user.name, email=user.email)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {email} not found!",
        )

    @staticmethod
    async def create(session: AsyncSession, user_create: UserCreateInput) -> UserOutput:
        user = User(name=user_create.name, email=user_create.email, password=user_create.password)
        user = await UserDAL.create(user=user, session=session)
        return UserOutput(name=user.name, email=user.email)

    @staticmethod
    async def update(
        session: AsyncSession,
        email: str,
        user_update: UserPutInput | UserPatchInput,
        # partial: bool = False,
    ) -> UserOutput | HTTPException:
        user: User | None = await UserDAL.get_by_email(session=session, email=email)
        if user:
            user = await UserDAL.update(
                session=session, user=user, user_update=user_update
            )

            return UserOutput(name=user.name, email=user.email)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {email} not found!",
        )

    @staticmethod
    async def delete(session: AsyncSession, email: str) -> None | HTTPException:
        user: User | None = await UserDAL.get_by_email(session=session, email=email)
        if user:
            await UserDAL.delete(session=session, user=user)
            return
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {email} not found!",
        )
