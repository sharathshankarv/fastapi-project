from database import Base

def create_tables(engine):
    Base.metadata.create_all(engine)