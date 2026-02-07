from pydantic import BaseModel, Field

class TeamsSchemaAdd(BaseModel):
    name: str = Field(max_length=32)

class TeamsSchemaView(TeamsSchemaAdd):
    id: int
    player_ids: list[int]

class TeamsSchemaAllView(BaseModel):
    data: list[TeamsSchemaView]
