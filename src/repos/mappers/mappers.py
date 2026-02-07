from src.repos.mappers.base import BaseMapper
from src.models import *
from src.schemas import * # only view schemas

class TeamsDataMapper(BaseMapper):
    db_model = Teams
    schema = TeamsSchemaView

class PlayerDataMapper(BaseMapper):
    db_model = Players
    schema = PlayerSchemaView