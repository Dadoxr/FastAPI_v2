from fastapi import HTTPException
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from .dals import NoteDAL
from .schemas import NoteOutput
from .schemas import NoteCreateInput
from .schemas import NotePatchInput
from .schemas import NotePutInput
from .models import Note


class NoteService:
    @staticmethod
    async def get_all(session: AsyncSession) -> list[NoteOutput | None]:
        notes: list[Note | None] = await NoteDAL.get_all(session=session)
        return [
            NoteOutput(id=note.id, title=note.title, body=note.body) for note in notes
        ]

    @staticmethod
    async def get_by_id(
        session: AsyncSession, note_id: int
    ) -> NoteOutput | HTTPException:
        note: Note | None = await NoteDAL.get_by_id(session=session, note_id=note_id)
        if note:
            return NoteOutput(id=note.id, title=note.title, body=note.body)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {note_id} not found!",
        )

    @staticmethod
    async def create(session: AsyncSession, note_create: NoteCreateInput) -> NoteOutput:
        note = Note(title=note_create.title, body=note_create.body)
        note = await NoteDAL.create(note=note, session=session)
        return NoteOutput(id=note.id, title=note.title, body=note.body)

    @staticmethod
    async def update(
        session: AsyncSession,
        note_update: NotePutInput | NotePatchInput,
        # partial: bool = False,
    ) -> NoteOutput | HTTPException:
        note: Note | None = await NoteDAL.get_by_id(
            session=session, note_id=note_update.id
        )
        if note:
            note = await NoteDAL.update(
                session=session, note=note, note_update=note_update
            )

            return NoteOutput(id=note.id, title=note.title, body=note.body)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id={note_update.id} not found!",
        )

    @staticmethod
    async def delete(session: AsyncSession, note_id: int) -> None | HTTPException:
        note: Note | None = await NoteDAL.get_by_id(session=session, note_id=note_id)
        if note:
            await NoteDAL.delete(session=session, note=note)
            return
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id={note_id} not found!",
        )
