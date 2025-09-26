from pydantic import BaseModel

class ProductBase(BaseModel):
  name: str
  description: str
  category: str
  price: float
  quantity: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
      model_config = {"from_attributes": True}