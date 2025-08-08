from pydantic import BaseModel

class CensoCreate(BaseModel):
    descripcion: str

class CensoOut(CensoCreate):
    id: int

    class Config:
        orm_mode = True
