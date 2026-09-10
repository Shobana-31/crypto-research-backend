# Global Market Endpoints

from fastapi import APIRouter
from data.global_data import MOCK_GLOBAL

router = APIRouter()


@router.get("/global")
async def get_global():
    """Return MOCK global market data"""
    return MOCK_GLOBAL