from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from schemas.s_Products import ProductCreate as ProductRequest, ProductResponse
from schemas.s_generic import CustomStringResponse
from services.Product_services import *

router = APIRouter(prefix="/products", tags=["products"])


# Get All products
@router.get("/", response_model=list[ProductResponse])
def get_products(session:Session = Depends(get_db)):
  return fetch_all_products(session)

# Get product by id
@router.get("/{id}", response_model=ProductResponse)
def get_product_by_id(id:int, session: Session = Depends(get_db)):
  db_product = fetch_product_by_id(id, session)
    
  return db_product 

# Add a new product
@router.post("/", response_model=ProductResponse)
def add_product(product:ProductRequest, session: Session = Depends(get_db)):
  return insert_product(session, product)
  
# Delete a product
@router.delete('/{id}', response_model=ProductResponse)
def delete_product(id: int, session: Session = Depends(get_db)):
  product = remove_product(session, id)
  return product

# update product
@router.put('/{id}', response_model=CustomStringResponse)
def update_product(id: int, pro: ProductRequest, session: Session = Depends(get_db)):
  return product_update(session, id, pro)
