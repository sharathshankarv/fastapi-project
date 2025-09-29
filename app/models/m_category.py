from database import Base
from sqlalchemy import Column,Integer,String, func, DateTime, Sequence, text

class Category(Base):

  __tablename__ = "categories"

  id= Column(Integer, autoincrement=True, primary_key=True, index=True, unique=True)
  name= Column(String, nullable=False, unique=True, index=True)
  description = Column(String, nullable=True)
  sort_order = Column(Integer ,nullable=False)
  is_active = Column(Integer, nullable=False, server_default=text("1"))
  created_on = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
  updated_on = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())