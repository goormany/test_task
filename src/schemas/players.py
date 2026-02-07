from pydantic import BaseModel, Field

class PlayerSchemaAdd(BaseModel):
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=32)
    team_id: int = Field(ge=0)

class PlayerSchemaView(PlayerSchemaAdd):
    id: int