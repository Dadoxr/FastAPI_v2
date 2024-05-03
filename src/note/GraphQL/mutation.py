import strawberry

from ...core import factory
from ..schemas import NoteOutput
from ..schemas import NoteCreateInput
from ..schemas import NotePutInput
from ..services import NoteService


@strawberry.type
class Mutation:
    
    @strawberry.field
    async def create_new_note(note: NoteCreateInput) -> NoteOutput:
        async with factory.get_session() as session:
            return await NoteService.create(session=session, note_create=note)

    @strawberry.field
    async def update_note(note: NotePutInput) -> NoteOutput:
        async with factory.get_session() as session:
            return await NoteService.update(session=session, note_update=note)


    @strawberry.field
    async def delete_note(note_id: int) -> None:
        async with factory.get_session() as session:
            return await NoteService.delete(session=session, note_id=note_id)
