from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from fastapi import APIRouter, Depends, status
from models import Food
from schemas import FoodRead
from database import get_async_session

router = APIRouter(tags=["Room"])


@router.get("/", response_model=List[FoodRead])
async def get_foods(db: AsyncSession = Depends(get_async_session)):
    stmt = (select(Food))
    result = await db.execute(stmt)
    food_models = result.scalars().all()
    foods = [FoodRead(name=food.name) for food in food_models]
    return foods
