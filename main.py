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
        "message": "Crypto API Running!",
        "version": "1.0.0",
        "endpoints": [
            "/api/coins",
            "/api/coins/{id}",
            "/api/coins/{id}/chart",
            "/api/global",
            "/api/search?query=bitcoin"
        ]
    }


if __name__ == "__main__":
    import uvicorn
    print("Server: http://localhost:5000")
    uvicorn.run(app, host="0.0.0.0", port=5000)