import strawberry

from ..schemas import UserOutput


@strawberry.type
class Query:

    @strawberry.field
    async def get_all_users() -> list[UserOutput | None]:
        return [UserOutput(email="GraphQL не настроен")]