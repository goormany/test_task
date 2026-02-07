from fastapi import APIRouter, Path

from src.api.dependencies import DBDep
from src.services.teams import TeamServices
from src.schemas.teams import TeamsSchemaAdd, TeamsSchemaView, TeamsSchemaAllView
from src.utils.exceptions import TeamNotFoundException
from src.utils.http_exceptions import TeamNotFoundHTTPException

router = APIRouter(prefix="/teams", tags=["Teams"])

@router.get("", response_model=TeamsSchemaAllView)
async def get_all_teams(db: DBDep):
    teams = await TeamServices(db).get_all()
    return {"data": teams}

@router.post("", response_model=TeamsSchemaView)
async def create_team(db: DBDep, data: TeamsSchemaAdd):
    team = await TeamServices(db).create_team(data)
    return team

@router.get("/{team_id}", response_model=TeamsSchemaView)
async def get_team_by_id(db: DBDep, team_id: int = Path(ge=0)):
    try:
        team = await TeamServices(db).get_team_by_id(team_id)
    except TeamNotFoundException:
        raise TeamNotFoundHTTPException
    return team

@router.delete("/{team_id}")
async def delete_team_by_id(db: DBDep, team_id: int = Path()):
    team = await TeamServices(db).delete_team_by_id(team_id)
    return {"ok": True}

@router.put("/{team_id}", response_model=TeamsSchemaView)
async def update_team_by_id(db: DBDep, data: TeamsSchemaAdd, team_id: int = Path()):
    try:
        team = await TeamServices(db).update_team_by_id(team_id, data)
    except TeamNotFoundException:
        raise TeamNotFoundHTTPException
    return team