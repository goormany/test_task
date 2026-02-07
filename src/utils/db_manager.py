from sqlalchemy.ext.asyncio import AsyncSession

from src.repos.teams import TeamsRepository
from src.repos.players import PlayersRepository

class DBManager:
    def __init__(self, session_factory: AsyncSession):
        self.session_factory = session_factory
    
    async def __aenter__(self):
        self.session: AsyncSession = self.session_factory()
        
        self.teams = TeamsRepository(self.session)
        self.players = PlayersRepository(self.session)
        
        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()
    
    async def commit(self):
        await self.session.commit()