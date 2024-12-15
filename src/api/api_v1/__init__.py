from fastapi import APIRouter

from config import settings

from .info import router as info_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(info_router, prefix=settings.api.v1.info)
