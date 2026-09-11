# Search Endpoint

from fastapi import APIRouter
from data.coins import MOCK_COINS

router = APIRouter()


@router.get("/search")
async def search_coins(query: str):
    """Search MOCK coins"""
    results = []
    for coin in MOCK_COINS:
        if query.lower() in coin["name"].lower() or query.lower() in coin["symbol"].lower():
            results.append(coin)
    return {"coins": results}