# routes/coins.py

from fastapi import APIRouter
from data.coins import MOCK_COINS
from data.coin_details import MOCK_COIN_DETAIL
from services.chart_service import generate_mock_chart
import time

router = APIRouter()

# Simple cache
_cache = {}
CACHE_DURATION = 60


def get_cached(key):
    if key in _cache:
        data, timestamp = _cache[key]
        if time.time() - timestamp < CACHE_DURATION:
            return data
    return None


def set_cache(key, data):
    _cache[key] = (data, time.time())


@router.get("/coins")
async def get_coins():
    """Get all coins"""
    return MOCK_COINS


@router.get("/coins/{coin_id}")
async def get_coin_detail(coin_id: str):
    """Get coin details"""
    if coin_id in MOCK_COIN_DETAIL:
        return MOCK_COIN_DETAIL[coin_id]
    return {"error": "Coin not found"}


@router.get("/coins/{coin_id}/chart")
async def get_chart(coin_id: str):
    """Get 7-day chart data"""
    cache_key = f"chart_{coin_id}"
    cached = get_cached(cache_key)
    if cached:
        return cached
    
    data = {"prices": generate_mock_chart()}
    set_cache(cache_key, data)
    return data