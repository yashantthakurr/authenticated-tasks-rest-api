
from api.routers import task, user
from contextlib import asynccontextmanager
from fastapi import FastAPI
from typing import Dict

@asynccontextmanager
async def lifespan(
    app: FastAPI
):
    yield

app = FastAPI(
    lifespan=lifespan
)

@app.get('/', tags=["Root Route"])
def read_root() -> Dict:
    return {"message": "Welcome to the API"}

@app.get('/health', tags=["Health Check Route"])
def health_check() -> Dict:
    return {"status": "healthy", "version": "0.1.0"}

app.include_router(
    router=user.router,
    prefix='/api/v1'
)

app.include_router(
    router=task.router,
    prefix='/api/v1'
)
