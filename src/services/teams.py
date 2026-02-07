from src.services.base import BaseServices
from src.schemas.teams import TeamsSchemaAdd
from src.utils.exceptions import ObjNotFoundException, TeamNotFoundException

class TeamServices(BaseServices):
    async def get_all(self):
        return await self.db.teams.get_all()
    
    async def create_team(self, data: TeamsSchemaAdd):
        team = await self.db.teams.add(data)
        await self.db.commit()
        return team

    async def get_team_by_id(self, team_id: int):
        try:
            team = await self.db.teams.get_one(id=team_id)
        except ObjNotFoundException:
            raise TeamNotFoundException
        return team

    async def delete_team_by_id(self, team_id: int):
        team = await self.db.teams.delete(id=team_id)
        await self.db.commit()
        return team

    async def update_team_by_id(self, team_id: int, data: TeamsSchemaAdd):
        try:
            team = await self.db.teams.update(data, id=team_id)
        except ObjNotFoundException:
            raise TeamNotFoundException
        await self.db.commit()
        return team