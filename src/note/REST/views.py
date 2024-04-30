from fastapi import APIRouter

from ..schemas import NoteOutput


note_rest_router = APIRouter(prefix="/notes")

@note_rest_router.get("/get_all")
async def get_all() -> list[NoteOutput | None]:
    return [NoteOutput(title="REST", body=" не настроен")]
