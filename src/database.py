from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.config import settings

engine = create_async_engine(url=settings.DB_URL)
session_maker = async_sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
