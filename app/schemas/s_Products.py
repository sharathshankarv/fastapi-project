from pydantic import BaseModel
from .s_generic import BaseResponse

class ProductBase(BaseModel):
  name: str
  description: str
  category: str
  price: float
  quantity: int

class ProductCreate(ProductBase):
    pass

ProductResponse = ProductBase
