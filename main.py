# main.py - Entry Point

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import coins, global_stats, search

app = FastAPI(
    title="Crypto API - Mock Data",
    description="Mock cryptocurrency data for Flutter app",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(coins.router, prefix="/api", tags=["Coins"])
app.include_router(global_stats.router, prefix="/api", tags=["Global"])
app.include_router(search.router, prefix="/api", tags=["Search"])

@app.get("/")
async def root():
    return {
        "message": "🚀 Crypto API Running with MOCK DATA!",
        "version": "1.0.0",
        "data_source": "MOCK (No CoinGecko API calls)",
        "endpoints": [
            {"path": "/api/coins", "description": "List of all mock coins"},
            {"path": "/api/coins/{id}", "description": "Mock coin details"},
            {"path": "/api/coins/{id}/chart", "description": "Mock chart data"},
            {"path": "/api/global", "description": "Mock global statistics"},
            {"path": "/api/search?query=bitcoin", "description": "Search mock coins"}
        ]
    }


if __name__ == "__main__":
    import uvicorn
    
    print("=" * 50)
    print("🚀 MOCK DATA SERVER STARTING!")
    print("📊 Data Source: MOCK (No CoinGecko API)")
    print("🌐 Server: http://localhost:5000")
    print("📖 API Docs: http://localhost:5000/docs")
    print("=" * 50)
    
    uvicorn.run(app, host="0.0.0.0", port=5000)