from pydantic import BaseModel
from .s_generic import BaseResponse
from typing import Optional

class CategorySchema(BaseModel):
  name: str
  description: str | None = None
  sort_order: Optional[int] = 0
  is_active: Optional[int] = 1

class CategoryCreate(CategorySchema):
  pass

CategoryResponse = CategorySchema

