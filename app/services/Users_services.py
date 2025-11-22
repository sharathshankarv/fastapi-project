from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models.m_user import User as UserModel
from schemas.s_user import UserCreateSchema, UserUpdateSchema
from constants.enums import UserRole

def fetch_all_users(session: Session):
  db_users = session.query(UserModel).all()
  return db_users

def fetch_user_by_email(email: str, session: Session):
  try:
    db_user = session.query(UserModel).filter(UserModel.email == email).first()
    if not db_user:
      raise HTTPException(status_code=404, detail="User not found")
    
    return db_user
  
  except Exception as e:
    raise HTTPException(status_code=400, detail="Error in fetching user by email." + str(e))
  
def fetch_user_by_phone(phone: int, session: Session):
  try:
    db_user = session.query(UserModel).filter(UserModel.phone == phone).first()
    if not db_user:
      raise HTTPException(status_code=404, detail="User not found")
    
    return db_user
  
  except Exception as e:
    raise HTTPException(status_code=400, detail="Error in fetching user by phone." + str(e))

def insert_user(session: Session, user: UserCreateSchema):
  try:
    user_data = UserModel(**user.model_dump())

    if user_data.role is None:
      user_data.role = UserRole.USER.value

    db_user = user_data

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
  except IntegrityError as e:
    session.rollback()
    
    if "ix_users_phone" in str(e.orig):
      raise HTTPException(status_code=400, detail="Phone number already exists.")
    elif "ix_users_email" in str(e.orig):
      raise HTTPException(status_code=400, detail="Email already exists.")
    else:
      raise HTTPException(status_code=400, detail="Integrity error occurred while creating the user." + str(e))
  
def update_user(session: Session, id: int, user: UserUpdateSchema):
  db_user = session.query(UserModel).filter(UserModel.id == id).first()
  if not db_user:
      raise HTTPException(status_code=404, detail="User not found")
  
  update_data = user.model_dump(exclude_unset=True)
  try:
    for field, value in update_data.items():
      setattr(update_data, field, value)
    
    session.commit()
    session.refresh(update_data)
    return update_data

  except Exception as e:
    session.rollback()
    raise HTTPException(status_code=400, detail="Could not update the user." + str(e))
  
def remove_user(session: Session, id: int):
  user = session.query(UserModel).filter(UserModel.id == id).first()
  if not user:
    raise HTTPException(status_code=404, detail="User not found")
  
  try:
    session.delete(user)
    session.commit()
    return "User deleted successfully"

  except Exception as e:
    raise HTTPException(status_code=400, detail="Could not delete the user." + str(e))