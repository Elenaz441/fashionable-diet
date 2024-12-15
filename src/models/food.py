from uuid import UUID, uuid4

import sqlalchemy as alchemy
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from models import Base


class Food(Base):
    __tablename__ = "food"

    id: Mapped[UUID] = mapped_column(alchemy.UUID, primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(length=64), unique=True, nullable=False)
    kilocalories: Mapped[int] = mapped_column(Integer, nullable=False)

    def __str__(self):
        return f"{self.__class__.__name__}"
