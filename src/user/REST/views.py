from typing import Annotated
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from ...core import factory
from ..schemas import UserOutput
from ..schemas import UserEmailInput
from ..schemas import UserCreateInput
from ..schemas import UserPatchInput
from ..schemas import UserPutInput
from ..services import UserService

router = APIRouter(prefix="/users")


@router.get("/all", response_model=list[UserOutput | None], status_code=status.HTTP_200_OK)
async def get_all():
    async with factory.get_session() as session:
        return await UserService.get_all(session=session)


@router.get("/{user_id}", response_model=UserOutput | None, status_code=status.HTTP_200_OK)
async def get_by_id(user_id: int):
    async with factory.get_session() as session:
        return await UserService.get_by_id(session=session, user_id=user_id)


@router.get("/", response_model=UserOutput | None, status_code=status.HTTP_200_OK)
async def get_by_email(user: UserEmailInput):
    async with factory.get_session() as session:
        return await UserService.get_by_email(session=session, email=user.email)


@router.post("/", response_model=UserOutput, status_code=status.HTTP_201_CREATED)
async def create(user: UserCreateInput):
    async with factory.get_session() as session:
        return await UserService.create(session=session, user=user)


@router.put("/", response_model=UserOutput, status_code=status.HTTP_200_OK)
async def update(user: UserEmailInput, user_update: UserPutInput):
    async with factory.get_session() as session:
        return await UserService.update(session=session, email=user.email, user_update=user_update)


@router.patch("/", response_model=UserOutput, status_code=status.HTTP_200_OK)
async def update_partial(user: UserEmailInput, user_update: UserPatchInput):
    async with factory.get_session() as session:
        return await UserService.update(session=session, email=user.email, user_update=user_update)


@router.delete("/", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete(user: UserEmailInput):
    async with factory.get_session() as session:
        return await UserService.delete(session=session, email=user.email)
