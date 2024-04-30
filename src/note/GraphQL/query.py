import strawberry

from ..schemas import NoteOutput
from ..services import NoteService


@strawberry.type
class Query:

    @strawberry.field
    async def get_all_notes() -> list[NoteOutput | None]:
        return await NoteService.get_all()

    @strawberry.field
    async def get_note_by_id(note_id: int) -> NoteOutput | None:
        return await NoteService.get_by_id(note_id=note_id)

