from ..core import factory
from .dals import UserDAL
from .schemas import UserBaseInput, UserOutput
from .models import User


class UserService:
    @staticmethod
    async def get_all() -> list[UserOutput | None]:
        async with factory.get_session() as session:
            users: list[User | None] = await UserDAL.get_all(session=session)
        return [UserOutput(email=user.email) for user in users]

    @staticmethod
    async def get_by_id(user_id: int) -> UserOutput | None:
        async with factory.get_session() as session:
            user: User | None = await UserDAL.get_by_id(
                session=session, user_id=user_id
            )
        if user:
            return UserOutput(email=user.email)

    @staticmethod
    async def get_by_email(user: UserBaseInput) -> UserOutput | None:
        async with factory.get_session() as session:
            user: User | None = await UserDAL.get_by_email(
                session=session, email=user.email
            )
        if user:
            return UserOutput(email=user.email)
