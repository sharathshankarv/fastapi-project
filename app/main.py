from fastapi import FastAPI;
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from database import engine
from models.models_Product import Base
from routes.Products import router

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
)

@asynccontextmanager
async def lifespan(app: FastAPI):
  Base.metadata.create_all(bind=engine)
  yield

@app.get("/")
def greet():
  return "Welcome to Fast api's"



