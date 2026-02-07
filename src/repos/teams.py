from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from src.repos.base import BaseRepository
from src.models.teams import Teams
from src.models.players import Players
from src.repos.mappers.mappers import TeamsDataMapper
from src.utils.exceptions import TeamNotFoundException

class TeamsRepository(BaseRepository):
    model = Teams
    mapper = TeamsDataMapper

    async def get_one(self, *args, **kwargs):
        query_team = (
            select(self.model)
            .filter(*args)
            .filter_by(**kwargs)
        )
        
        res = await self.session.execute(query_team)
        try:
            team = res.scalar_one()
        except NoResultFound:
            raise TeamNotFoundException
        
        
        query_player = (
            select(Players.id)
            .filter_by(team_id=team.id)
        )
        res = await self.session.execute(query_player)
        player_ids = res.scalars().all()
        
        team_with_players = {
            "id": team.id,
            "name": team.name,
            "player_ids": player_ids
        }
        
        return self.mapper.map_to_schema(team_with_players)