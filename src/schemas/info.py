from enum import Enum, IntEnum
from typing import List

from pydantic import Field

from .base import PyBaseModel
from .food import FoodRequest


class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"


class PhysicalActivityType(IntEnum):
    Minimal = 1
    ThreeTimesAWeek = 2
    FiveTimesAWeek = 3
    HardFiveTimesAWeek = 4
    EveryDay = 5
    HardEveryDay = 6
    HardWorkEveryDay = 7


class InfoRequest(PyBaseModel):
    gender: Gender
    height: int = Field(ge=50, le=270)
    weight: int = Field(ge=2, le=600)
    age: int = Field(ge=14, le=150)
    physical_activity_type: PhysicalActivityType
    foods: List[FoodRequest]


class InfoResponse(PyBaseModel):
    category_name: str
    category_description: str
    calorie_standard: float
    user_calorie: float
