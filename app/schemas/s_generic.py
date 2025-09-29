from pydantic import BaseModel
from typing import Generic, TypeVar

class CustomStringResponse(BaseModel):
    message: str

T = TypeVar('T')

class BaseResponse(BaseModel, Generic[T] ):
    id: int
    data: T

    class Config:
      model_config = {"from_attributes": True}