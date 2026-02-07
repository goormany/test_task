from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.services.players import PlayerServices
from src.schemas.players import PlayerSchemaAdd, PlayerSchemaView

router = APIRouter(prefix="/players", tags=["Players"])

@router.post("", response_model=PlayerSchemaView)
async def create_player(db: DBDep, data: PlayerSchemaAdd):
    player = await PlayerServices(db).create_player(data)
    return player

@router.get("", response_model=list[PlayerSchemaView])
async def get_all_players(db: DBDep):
    return await PlayerServices(db).get_all_players()