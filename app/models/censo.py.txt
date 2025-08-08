from sqlalchemy import Column, Integer, String
from .database import Base

class Censo(Base):
    __tablename__ = "censos"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, index=True)
