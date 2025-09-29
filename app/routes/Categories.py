from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from schemas.s_category import CategoryCreate as CategoryRequest, CategoryResponse
from schemas.s_generic import CustomStringResponse
from services.Categories_services import *

router = APIRouter(prefix="/categories", tags=["categories"])

# Get All categories
@router.get("/", response_model=list[CategoryResponse])
def get_all_categories(session:Session = Depends(get_db)):
  return fetch_all_categories(session)

# Add a new category
@router.post("/", response_model=CategoryResponse)
def add_category(category:CategoryRequest, session: Session = Depends(get_db)):
  return insert_category(session, category)

# Delete a category
@router.delete("/{id}", response_model=CustomStringResponse)
def delete_category(id:int, session: Session = Depends(get_db)):
  return remove_category(session, id)