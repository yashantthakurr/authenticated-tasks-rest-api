
from api.auth import security
from api.dependencies.database import get_db
from api.exceptions.auth import INVALID_LOGIN_CREDENTIALS_EXCEPTION
from api.exceptions.user import USER_BY_ID_NOT_FOUND_EXCEPTION
from api.models.user import User
from api.schemas.token import Token
from api.schemas.user import CreateUser, LoginUser, ResponseUser, UpdateUser
from api.services import user as userservice
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Dict, List

router = APIRouter(
    tags=["Users API Routes"],
    prefix='/users'
)

@router.post('/login', response_model=Token)
def login_user(
    data: LoginUser,
    db: Session = Depends(get_db)
) -> Dict:
    access_token = security.login_user(db, data)
    if not access_token:
        raise INVALID_LOGIN_CREDENTIALS_EXCEPTION
    return access_token

@router.post('/register', response_model=ResponseUser)
def register_user(
    data: CreateUser,
    db: Session = Depends(get_db)
) -> User:
    return userservice.register(db, data)

@router.get('/search/id/{id}', response_model=ResponseUser)
def get_user_by_id(
    id: int,
    db: Session = Depends(get_db)
) -> User:
    user = userservice.read_user_by_id(db, id)
    if not user:
        raise USER_BY_ID_NOT_FOUND_EXCEPTION
    return user

@router.get('/search/all', response_model=List[ResponseUser])
def get_all_user(
    db: Session = Depends(get_db)
) -> List[User]:
    return userservice.read_all_users(db)

@router.patch('/update/id/{id}', response_model=ResponseUser)
def update_user_by_id(
    id: int,
    data: UpdateUser,
    db: Session = Depends(get_db)
) -> User:
    user = userservice.update_user_by_id(db, id, data)
    if not user:
        raise USER_BY_ID_NOT_FOUND_EXCEPTION
    return user

@router.delete('/delete/id/{id}', response_model=None)
def delete_user_by_id(
    id: int,
    db: Session = Depends(get_db)
) -> Dict:
    user = userservice.delete_user_by_id(db, id)
    if not user:
        raise USER_BY_ID_NOT_FOUND_EXCEPTION
    return {"message": "user deleted successfully"}
