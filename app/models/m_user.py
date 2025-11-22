from database import Base
from sqlalchemy import Column,Boolean, Integer, String,Date, DateTime, func
from sqlalchemy import Enum as SqlEnum
from constants.enums import UserRole

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
  email = Column(String, nullable=False, unique=True, index=True)
  phone = Column(String, nullable=False, unique=True, index=True)
  username=  Column(String, nullable=False, index=True)
  full_name= Column(String, nullable=False)
  dob= Column(Date, nullable=False)
  is_active= Column(Boolean, default=True)
  role = Column(String, nullable=False, server_default=UserRole.USER.value)
  password= Column(String, nullable=False)
  created_at= Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
  updated_at= Column(DateTime(timezone=True),server_default=func.now(), onupdate=func.now(), nullable=False)