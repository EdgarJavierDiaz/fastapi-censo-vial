from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/censos/", response_model=schemas.CensoOut)
def crear_censo(censo: schemas.CensoCreate, db: Session = Depends(get_db)):
    nuevo_censo = models.Censo(**censo.dict())
    db.add(nuevo_censo)
    db.commit()
    db.refresh(nuevo_censo)
    return nuevo_censo

@router.get("/censos/", response_model=list[schemas.CensoOut])
def obtener_censos(db: Session = Depends(get_db)):
    return db.query(models.Censo).all()

