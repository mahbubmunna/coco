from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy import text
from app.core.db import engine, Base
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Setup pgvector extension if not exists
    with engine.connect() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        conn.commit()
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    yield
    # Cleanup on shutdown can go here

app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)

@app.get("/")
def health_check():
    return {"status": "ok", "project": settings.PROJECT_NAME}
