from fastapi import FastAPI;
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from database import engine
from routes.Products import router
from routes.Categories import router as cat_router
from models import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
  create_tables(engine)
  yield

app = FastAPI(lifespan=lifespan)

app.include_router(router)
app.include_router(cat_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
)

@app.get("/")
def greet():
  return "Welcome to Fast api's"



