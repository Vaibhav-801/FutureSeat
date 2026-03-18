from fastapi import FastAPI
from app.core.config import settings
from app.db.session import Base, engine
from app.api.v1.routes import router as v1_router

app = FastAPI(title=settings.APP_NAME)

Base.metadata.create_all(bind=engine)

app.include_router(v1_router, prefix="/api/v1")


@app.get("/health")
def health():
    return {"status": "ok"}