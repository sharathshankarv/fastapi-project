from sqlalchemy.orm import Session
from models.m_category import Category as CategoryModel

def fetch_all_categories(session: Session):
  db_categories = session.query(CategoryModel).all()
  return db_categories

def insert_category(session: Session, category: CategoryModel):
  try:
    latestSortOrder = session.query(CategoryModel).order_by(CategoryModel.sort_order.desc()).first()
    if latestSortOrder:
      category.sort_order = latestSortOrder.sort_order + 1
    else:
      category.sort_order = 1
    db_category = CategoryModel(**category.model_dump())
    session.add(db_category)
    session.flush()
    session.refresh(db_category)
    session.commit()
    return db_category
  
  except Exception as e:
    session.rollback()
    st = "Error in adding category" + str(e)
    raise Exception(st)

# remove_category
def remove_category(session: Session, id: int):
  category = session.query(CategoryModel).filter(CategoryModel.id == id).first()
  if not category:
    raise Exception("Category not found")
  
  try:
    session.delete(category)
    session.commit()
    return "Category delted successfully"

  except Exception as e:
    raise Exception("Could not delete the category.")