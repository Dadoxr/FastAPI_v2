from fastapi import APIRouter

from ..schemas import UserOutput

user_rest_router = APIRouter(prefix="/users")


@user_rest_router.get("/get_all")
async def get_all() -> list[UserOutput | None]:
    return [UserOutput(email="REST не настроен")]
