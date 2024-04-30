from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Note


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
    async def get_by_email(session: AsyncSession, email: str) -> Note | None:
        stmp = select(Note).where(Note.email == email)
        return await session.scalar(stmp)
