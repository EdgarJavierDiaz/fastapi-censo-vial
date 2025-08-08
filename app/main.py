from fastapi import FastAPI

app = FastAPI()

from app.routes.censo import router as censo_router

app.include_router(censo_router)


@app.get("/")
def read_root():
    return {"message": "Bienvenido al Censo Vial con FastAPI"}
