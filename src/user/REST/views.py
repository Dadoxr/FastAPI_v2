from fastapi import APIRouter

from ..models import User
from ..services import UserService
from ..schemas import UserOutput, UserBaseInput

user_rest_router = APIRouter(prefix="/users")


@user_rest_router.get("/all")
async def get_all() -> list[UserOutput | None]:
    return await UserService.get_all()


@user_rest_router.get("/{user_id}")
async def get_by_id(user_id: int) -> UserOutput | None:
    return await UserService.get_by_id(user_id=user_id)


@user_rest_router.get("/{email}")
async def get_by_email(user: UserBaseInput) -> UserOutput | None:
    return await UserService.get_by_email(email=user.email)
