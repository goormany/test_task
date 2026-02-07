from src.repos.base import BaseRepository
from src.models.players import Players
from src.repos.mappers.mappers import PlayerDataMapper

class PlayersRepository(BaseRepository):
    model = Players
    mapper = PlayerDataMapper
