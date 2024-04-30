from fastapi import APIRouter

from ..schemas import NoteOutput
from ..services import NoteService

note_rest_router = APIRouter(prefix="/notes")


@note_rest_router.get("/all")
async def get_all() -> list[NoteOutput | None]:
    return await NoteService.get_all()


@note_rest_router.get("/{note_id}")
async def get_by_id(note_id: int) -> NoteOutput | None:
    return await NoteService.get_by_id(note_id=note_id)
