# routes/coins.py - Coin Endpoints

from fastapi import APIRouter
from data.coins import MOCK_COINS
from data.coin_details import MOCK_COIN_DETAIL
from services.chart_service import generate_mock_chart

router = APIRouter()


@router.get("/coins")
async def get_coins():
    """Return MOCK coin list"""
    return MOCK_COINS


@router.get("/coins/{coin_id}")
async def get_coin_detail(coin_id: str):
    """Return MOCK coin detail"""
    if coin_id in MOCK_COIN_DETAIL:
        return MOCK_COIN_DETAIL[coin_id]
    return {"error": "Coin not found"}


@router.get("/coins/{coin_id}/chart")
async def get_chart(coin_id: str, days: int = 7):
    """Return MOCK chart data for specific timeframe"""
    return {"prices": generate_mock_chart(days)}