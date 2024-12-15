from pydantic import Field

from .base import PyBaseModel


class FoodRead(PyBaseModel):
    name: str = Field(max_length=64)


class FoodRequest(PyBaseModel):
    name: str = Field(max_length=64)
    quantity: int = Field(default=100)
