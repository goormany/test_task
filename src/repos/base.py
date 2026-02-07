from pydantic import BaseModel
from sqlalchemy import insert, select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from src.database import Base
from src.repos.mappers.base import BaseMapper
from src.utils.exceptions import ObjNotFoundException

class BaseRepository:
    model: Base = None
    mapper: BaseMapper = None
    
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    
    async def get_all(self):
        query = select(self.model)
        res = await self.session.execute(query)
        return [self.mapper.map_to_schema(item) for item in res.scalars().all()]
    
    async def get_one(self, *args, **kwargs):
        query = (
            select(self.model)
            .filter(*args)
            .filter_by(**kwargs)
        )
        res = await self.session.execute(query)
        try:
            res = self.mapper.map_to_schema(res.scalar_one())
        except NoResultFound:
            raise ObjNotFoundException
        return res
    
    
    async def add(self, data: BaseModel, exclude_unset: bool = False):
        stmt = (
            insert(self.model)
            .values(**data.model_dump(exclude_unset=exclude_unset))
            .returning(self.model)
        )
        res = await self.session.execute(stmt)
        return self.mapper.map_to_schema(res.scalar_one())
    
    async def delete(self, *args, **kwargs):
        stmt = (
            delete(self.model)
            .filter(*args)
            .filter_by(**kwargs)
        )
        await self.session.execute(stmt)
    
    async def update(self, data: BaseModel, **kwargs):
        stmt = (
            update(self.model)
            .filter_by(**kwargs)
            .values(**data.model_dump())
            .returning(self.model)
        )
        res = await self.session.execute(stmt)
        try:
            res = self.mapper.map_to_schema(res.scalar_one())
        except NoResultFound:
            raise ObjNotFoundException
        return res