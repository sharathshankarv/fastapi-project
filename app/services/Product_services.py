from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.m_Product import Product as ProductModel
from models.m_category import Category as CategoryModel
from schemas.s_Product import ProductCreate as ProductRequest

def fetch_all_products(session: Session):
  db_products = session.query(ProductModel).all()
  return db_products

def fetch_product_by_id(id: int, session: Session):
  db_product = session.query(ProductModel).filter(ProductModel.id == id).first()

  if not db_product:
    raise HTTPException(status_code=404, detail="Product not found")
  
  return db_product

def insert_product(session: Session, product: ProductRequest):
  print("Inserting product:", product)
  try:
    print("Checking category existence for ID:", product.category)
    cat = session.query(CategoryModel).filter(CategoryModel.id == product.category).first()
    print("Category:", cat)
    if not cat:
      print("Category not found")
      raise HTTPException(status_code=404, detail="Category not found")
    
    db_product = ProductModel(**product.model_dump())
    session.add(db_product)
    session.flush()
    session.refresh(db_product)
    session.commit()
    return db_product
  
  except Exception as e:
    session.rollback()
    st = "Error in adding product" + str(e)
    print("Exception:", st)
    raise HTTPException(status_code=400, detail=st)
  
# remove_product
def remove_product(session: Session, id: int):
  product = session.query(ProductModel).filter(ProductModel.id == id).first()
  if not product:
    raise HTTPException(status_code=404, detail="Product not found")
  
  try:
    session.delete(product)
    session.commit()
    return "Product delted successfully"

  except Exception as e:
    raise HTTPException(status_code=400, detail="Could not delete the product.")

# Update product
def product_update(session: Session, id: int, pro: ProductRequest):
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
  return "Product updated successfully"
  