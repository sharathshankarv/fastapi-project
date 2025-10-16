from database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, func, ForeignKey

class Product(Base):

  __tablename__ = "products"

  id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
  name = Column(String, nullable=False, unique=True)
  description = Column(String, nullable=False)
  category = Column(Integer, ForeignKey('categories.id'), index=True, nullable=False)
  price = Column(Float, nullable=False)
  quantity = Column(Integer, nullable=False)
  created_on = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
  updated_on = Column(DateTime(timezone=True),server_default=func.now(), onupdate=func.now(), nullable=False)