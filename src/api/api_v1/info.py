from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from fastapi import APIRouter, Depends, status
from models import Food
from schemas import InfoResponse, InfoRequest
from database import get_async_session
from utils import (
    calculate_calorie_standard,
    get_category
)

router = APIRouter(tags=["Room"])


@router.post("/", status_code=status.HTTP_200_OK, response_model=InfoResponse)
async def calc_info(user_info: InfoRequest, db: AsyncSession = Depends(get_async_session)):
    calorie_standard = calculate_calorie_standard(
        gender=user_info.gender,
        height=user_info.height,
        weight=user_info.weight,
        age=user_info.age,
        physical_activity_type=user_info.physical_activity_type)

    user_calorie = 0
    foods = user_info.foods
    for food in foods:
        stmt = select(Food).where(Food.name == food.name)
        result = await db.execute(stmt)
        food_model = result.scalar()
        user_calorie += food_model.kilocalories * food.quantity / 100

    category_name, category_description, category_url = get_category(
        height=user_info.height,
        weight=user_info.weight,
        age=user_info.age,
        physical_activity_type=user_info.physical_activity_type
    )
    return InfoResponse(
        category_name=category_name,
        category_description=category_description,
        category_url=category_url,
        calorie_standard=calorie_standard,
        user_calorie=user_calorie)
