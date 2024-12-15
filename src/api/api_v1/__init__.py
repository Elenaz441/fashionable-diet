from fastapi import APIRouter

from config import settings

from .info import router as info_router
from .food import router as food_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(info_router, prefix=settings.api.v1.info)
router.include_router(food_router, prefix=settings.api.v1.foods)
