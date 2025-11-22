from pydantic import BaseModel, EmailStr, Field, field_validator, StringConstraints
from datetime import datetime, date
from typing import Optional, Annotated
from constants.enums import UserRole
import re

class UserBaseSchema(BaseModel):
  username: Annotated[str, StringConstraints(strip_whitespace=True, min_length=5, max_length=150)]
  email: EmailStr = Field(..., max_length=255)
  phone: Annotated[str, StringConstraints(min_length=10, max_length=15)]
  full_name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=5, max_length=255)]
  dob: date
  is_active: bool = True
  role: Optional[UserRole] = UserRole.USER

  @field_validator('phone')
  def validate_phone(cls, v):
    if not re.match(r'^\+?1?\d{9,15}$', v):  
        raise ValueError('Invalid phone number format')
    return v

class UserCreateSchema(UserBaseSchema):
  password: str = Field(..., min_length=8, max_length=128)

  class Config:
    json_encoders = {
      date: lambda v: v.isoformat(),
      datetime: lambda v: v.isoformat(),
    }

class UserResponseSchema(BaseModel):
  id: int
  username: str
  email: str
  phone: str
  full_name: str
  dob: date
  is_active: bool = True
  role: str
  created_at: datetime
  updated_at: datetime

  class Config:
    from_attributes = True

class UserUpdateSchema(BaseModel):
  username: Optional[str] = Field(None, min_length=5, max_length=150)
  email: Optional[EmailStr] = None
  phone: Optional[str] = Field(None, max_length=15)
  full_name: Optional[str] = Field(None, min_length=5, max_length=255)
  dob: Optional[date] = None
  role: Optional[UserRole] = None
  is_active: Optional[bool] = None

  @field_validator('phone')
  def validate_phone(cls, v):
    if v is None:
        return v
    if not re.match(r'^\+?1?\d{9,15}$', v):  
        raise ValueError('Invalid phone number format')
    return v