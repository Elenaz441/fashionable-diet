from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from fastapi import APIRouter, Depends
from models import Food
from schemas import FoodRead
from database import get_async_session

router = APIRouter(tags=["Food"])


@router.get("/", response_model=List[FoodRead])
async def get_foods(db: AsyncSession = Depends(get_async_session)):
    stmt = (select(Food).order_by(Food.name))
    result = await db.execute(stmt)
    food_models = result.scalars().all()
    foods = [FoodRead(name=food.name) for food in food_models]
    return foods


# @router.post("/")
# async def create_foods(db: AsyncSession = Depends(get_async_session)):
#     import csv
#     with open('foods.csv', newline='', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             new_food = Food(name=row['name'], kilocalories=int(row['kkal']))
#             db.add(new_food)
#             await db.commit()
