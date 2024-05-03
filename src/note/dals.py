from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Note
from .schemas import NotePutInput, NotePatchInput


class NoteDAL:
    @staticmethod
    async def get_all(session: AsyncSession) -> list[Note]:
        stmp = select(Note)
        return await session.scalars(stmp)

    @staticmethod
    async def get_by_id(session: AsyncSession, note_id: int) -> Note | None:
        stmp = select(Note).where(Note.id == note_id)
        return await session.scalar(stmp)

    @staticmethod
    async def create(session: AsyncSession, note: Note) -> Note:
        session.add(note)
        await session.commit()
        # await session.refresh(product)
        return note

    @staticmethod
    async def update(
        session: AsyncSession,
        note: Note,
        note_update: NotePutInput | NotePatchInput,
        # partial: bool,
    ) -> Note | None:
        for name, value in vars(note_update).items():
            if value:
                setattr(note, name, value)
        await session.commit()
        return note

    @staticmethod
    async def delete(session: AsyncSession, note: Note) -> None:
        await session.delete(note)
        await session.commit()