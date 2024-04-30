"""
Note models
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from ..core.models import Base
from ..user.mixins import UserRelationMixin

class Note(UserRelationMixin, Base):
    _user_back_populates = "notes"

    title: Mapped[str] = mapped_column(String(50), default="", server_default="")
    body: Mapped[str] = mapped_column(default="", server_default="")
