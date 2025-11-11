from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Settings

settings = Settings()
# db_url = "postgresql://postgres:postgres@localhost:5432/fast_api_practice"
engine = create_engine(settings.DATABASE_URL,pool_pre_ping=True,
    future=True)
Base = declarative_base()
# Base.metadata.create_all(bind=engine)

session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
  db = session()
  try:
    yield db
  finally:
    db.close()
