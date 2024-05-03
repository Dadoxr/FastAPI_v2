import strawberry

from ..services import UserService
from ...core import factory
from ..dals import UserDAL
from ..schemas import UserOutput
from ..schemas import UserEmailInput
from ..schemas import UserCreateInput
from ..schemas import UserPatchInput
from ..schemas import UserPutInput
from ..models import User

@strawberry.type
class Query:

    @strawberry.field
    async def get_all_users() -> list[UserOutput | None]:
        async with factory.get_session() as session:
            return await UserService.get_all(session=session)

    @strawberry.field
    async def get_user_by_id(user_id: int) -> UserOutput:
        async with factory.get_session() as session:
            return await UserService.get_by_id(session=session, user_id=user_id)

    @strawberry.field
    async def get_user_by_email(user: UserEmailInput) -> UserOutput:
        async with factory.get_session() as session:
            return await UserService.get_by_email(session=session, email=user.email)
