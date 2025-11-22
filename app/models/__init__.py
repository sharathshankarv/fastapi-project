from database import Base
from .m_category import Category
from .m_Product import Product
from .m_user import User



def create_tables(engine):
    Base.metadata.create_all(bind=engine)
