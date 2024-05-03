from fastapi import APIRouter
from fastapi import status

from ...core import factory
from ..schemas import NoteOutput
from ..schemas import NoteCreateInput
from ..schemas import NotePatchInput
from ..schemas import NotePutInput
from ..services import NoteService

router = APIRouter(prefix="/notes")

@router.get("/all", response_model=list[NoteOutput | None], status_code=status.HTTP_200_OK)
async def get_all():
    async with factory.get_session() as session:
        return await NoteService.get_all(session=session)


@router.get("/{note_id}", response_model=NoteOutput | None, status_code=status.HTTP_200_OK)
async def get_by_id(note_id: int):
    async with factory.get_session() as session:
        return await NoteService.get_by_id(session=session, note_id=note_id)


@router.post("/", response_model=NoteOutput, status_code=status.HTTP_201_CREATED)
async def create(note: NoteCreateInput):
    async with factory.get_session() as session:
        return await NoteService.create(session=session, note_create=note)


@router.put("/", response_model=NoteOutput, status_code=status.HTTP_200_OK)
async def update(note: NotePutInput):
    async with factory.get_session() as session:
        return await NoteService.update(session=session, note_update=note)


@router.patch("/", response_model=NoteOutput, status_code=status.HTTP_200_OK)
async def update_partial(note: NotePatchInput):
    async with factory.get_session() as session:
        return await NoteService.update(session=session, note_update=note)


@router.delete("/", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete(note_id: int):
    async with factory.get_session() as session:
        return await NoteService.delete(session=session, note_id=note_id)
