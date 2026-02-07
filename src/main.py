import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI

sys.path.append(str(Path(__file__).parent.parent))

from src.config import settings
from src.api.teams import router as router_team
from src.api.players import router as router_player

app = FastAPI()
app.include_router(router_team)
app.include_router(router_player)

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.APP_HOST, port=settings.APP_PORT, reload=True)