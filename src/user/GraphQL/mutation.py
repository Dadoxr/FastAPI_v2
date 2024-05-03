import strawberry

from ...core import factory
from ..schemas import UserOutput
from ..schemas import UserEmailInput
from ..schemas import UserCreateInput
from ..schemas import UserPutInput
from ..services import UserService


@strawberry.type
class Mutation:

    @strawberry.field
    async def create_user(user: UserCreateInput) -> UserOutput:
        async with factory.get_session() as session:
            return await UserService.create(session=session, user_create=user)

    @strawberry.field
    async def update_user(
        user: UserEmailInput, user_update: UserPutInput
    ) -> UserOutput:
        async with factory.get_session() as session:
            return await UserService.update(
                session=session, email=user.email, user_update=user_update
            )

    @strawberry.field
    async def delete_user(user: UserEmailInput) -> None:
        async with factory.get_session() as session:
            return await UserService.delete(session=session, email=user.email)
