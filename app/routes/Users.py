from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from schemas.s_user import UserResponseSchema, UserCreateSchema, UserUpdateSchema
from schemas.s_generic import CustomStringResponse
from services.Users_services import *

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserResponseSchema])
def get_all_users(session:Session = Depends(get_db)):
  return fetch_all_users(session)

@router.get('/user', response_model=UserResponseSchema)
def get_user_by_email(email: str = None, phone:str = None, session: Session = Depends(get_db)):
  if not email and not phone:
    raise HTTPException(status_code=400, detail="Either email or phone must be provided.")
  
  if phone:
    db_user = fetch_user_by_phone(phone, session)
    if db_user:
      return db_user
  
  if email:
    db_user = fetch_user_by_email(email, session)
    if db_user:
      return db_user
    
  raise HTTPException(status_code=404, detail="User not found")

@router.post("/", response_model=UserResponseSchema)
def add_user(user:UserCreateSchema, session: Session = Depends(get_db)):
  return insert_user(session, user) 

@router.put("/{id}", response_model=UserResponseSchema)
def update_user_details(id: int, user: UserUpdateSchema, session: Session = Depends(get_db)):
  return update_user(session, id, user) 

@router.delete("/{id}", response_model=CustomStringResponse)
def delete_user(id: int, session: Session = Depends(get_db)):
  return remove_user(session, id)
