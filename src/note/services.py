from ..core import factory
from .dals import NoteDAL
from .schemas import NoteOutput
from .models import Note


class NoteService:
    @staticmethod
    async def get_all() -> list[NoteOutput | None]:
        async with factory.get_session() as session:
            notes: list[Note | None] = await NoteDAL.get_all(session=session)
        return [NoteOutput(title=note.title, body=note.body) for note in notes]

    @staticmethod
    async def get_by_id(note_id: int) -> NoteOutput | None:
        async with factory.get_session() as session:
            note: Note | None = await NoteDAL.get_by_id(
                session=session, note_id=note_id
            )
        if note:
            return NoteOutput(title=note.title, body=note.body)
