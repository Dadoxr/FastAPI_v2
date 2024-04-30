"""
User models
"""
from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.core import Base

if TYPE_CHECKING:
    from ..note.models import Note

class User(Base):
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]

    notes: Mapped[list["Note"]] = relationship(back_populates="user")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(email={self.email})"

    def __repr__(self) -> str:
        return self
