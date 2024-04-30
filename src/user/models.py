"""
User models
"""

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.core import Base


class User(Base):
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(email={self.email})"

    def __repr__(self) -> str:
        return self
