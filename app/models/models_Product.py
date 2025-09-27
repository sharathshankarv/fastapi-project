from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer ,String, Float, DateTime, func

Base = declarative_base()

class Product(Base):

  __tablename__ = "product"

  id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
  name = Column(String, nullable=False, unique=True)
  description = Column(String, nullable=False)
  category = Column(String, index=True, nullable=False)
  price = Column(Float, nullable=False)
  quantity = Column(Integer, nullable=False)
  created_on = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
  updated_on = Column(DateTime(timezone=True),server_default=func.now(), onupdate=func.now(), nullable=False)