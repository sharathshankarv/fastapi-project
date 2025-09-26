from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from models.models_Product import Product as ProductModel
from schemas.Schemas_Product import ProductCreate as ProductRequest, ProductResponse 
from database import get_db

router = APIRouter(prefix="/products", tags=["products"])


# Get All products
@router.get("/", response_model=list[ProductResponse])
def get_products(session: Session = Depends(get_db)):
  db_products = session.query(ProductModel).all()

  return db_products

# Get product by id
@router.get("/{id}", response_model=ProductResponse)
def get_product_by_id(id:int, session: Session = Depends(get_db)):
  db_product = session.query(ProductModel).filter(ProductModel.id == id).first()
  if not db_product:
      raise HTTPException(status_code=404, detail="Product not found")
    
  return db_product 

# Add a new product
@router.post("/", response_model=ProductResponse)
def add_product(product:ProductRequest, session: Session = Depends(get_db)):
  try:
    db_product = ProductModel(**product.model_dump())
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product
    
  except Exception as e:
    print("Exception:", e)
    raise HTTPException(status_code=400, detail="Error in adding product")
  
# Delete a product
@router.delete('/{id}', response_model=ProductResponse)
def delete_product(id: int, session: Session = Depends(get_db)):
  product = session.query(ProductModel).filter(ProductModel.id == id).first()
  
  if not product:
    raise HTTPException(status_code=404, detail="Product not found")
  
  session.delete(product)
  session.commit()
  return product

# update product
@router.put('/{id}', response_model=ProductResponse)
def update_product(id: int, pro: ProductRequest, session: Session = Depends(get_db)):
  db_product = session.query(ProductModel).filter(ProductModel.id == id).first()
  if not db_product:
      raise HTTPException(status_code=404, detail="Product not found")
  
  db_product.name = pro.name
  db_product.description = pro.description
  db_product.category = pro.category
  db_product.price = pro.price
  db_product.quantity = pro.quantity

  session.commit()
  session.refresh(db_product)
  return db_product
