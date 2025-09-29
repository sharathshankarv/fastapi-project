from database import Base
from .m_category import Category
from .m_Product import Product



def create_tables(engine):
    Base.metadata.create_all(bind=engine)
