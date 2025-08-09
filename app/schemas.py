from pydantic import BaseModel, ConfigDict

class CensoCreate(BaseModel):
    descripcion: str

class CensoOut(CensoCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
