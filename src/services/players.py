from src.schemas.players import PlayerSchemaAdd
from src.services.base import BaseServices

class PlayerServices(BaseServices):
    async def create_player(self, data: PlayerSchemaAdd):
        player = await self.db.players.add(data)
        await self.db.commit()
        return player

    async def get_all_players(self):
        players = await self.db.players.get_all()
        return players