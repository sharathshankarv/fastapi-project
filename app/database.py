from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Settings

settings = Settings()
# db_url = "postgresql://postgres:admin@localhost:5432/fast_api_practice"
engine = create_engine(settings.DATABASE_URL)
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()

def get_db():
  db = session()
  try:
    yield db
  finally:
    db.close()
