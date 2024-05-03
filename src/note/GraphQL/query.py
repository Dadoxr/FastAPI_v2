import strawberry

from ...core import factory
from ..schemas import NoteOutput
from ..services import NoteService


@strawberry.type
class Query:

    @strawberry.field
    async def get_all_notes() -> list[NoteOutput | None]:
        async with factory.get_session() as session:
            return await NoteService.get_all(session=session)

    @strawberry.field
    async def get_note_by_id(note_id: int) -> NoteOutput:
        async with factory.get_session() as session:
            return await NoteService.get_by_id(session=session, note_id=note_id)

