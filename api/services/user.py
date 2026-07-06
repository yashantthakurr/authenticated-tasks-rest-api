
from api.auth.security import hash_password, login_user
from api.exceptions.user import EMAIL_ALREADY_TAKEN_EXCEPTION, USERNAME_ALREADY_TAKEN_EXCEPTION
from api.models.user import User
from api.schemas.user import CreateUser, UpdateUser
from sqlalchemy.orm import Session
from typing import List
    
def register(
        db: Session,
        data: CreateUser
) -> User:
    if db.query(User).filter(User.email==data.email).first():
        raise EMAIL_ALREADY_TAKEN_EXCEPTION
    if db.query(User).filter(User.username==data.username).first():
        raise USERNAME_ALREADY_TAKEN_EXCEPTION
    user = User(
        email = data.email,
        username = data.username,
        hashed_password = hash_password(data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def read_user_by_id(
        db: Session,
        id: int
) -> User | None:
    user = db.query(User).filter(User.id==id).first()
    if not user:
        return None
    return user

def read_all_users(
        db: Session
) -> List[User]:
    return db.query(User).all()

def update_user_by_id(
        db: Session,
        id: int,
        data: UpdateUser
) -> User | None:
    user = read_user_by_id(db, id)
    if not user:
        return None
    if data.email is not None:
        if db.query(User).filter(User.email==data.email, User.id!=id).first():
            raise EMAIL_ALREADY_TAKEN_EXCEPTION
        user.email=data.email
    if data.username is not None:
        if db.query(User).filter(User.username==data.username, User.id!=id).first():
            raise USERNAME_ALREADY_TAKEN_EXCEPTION
        user.username=data.username
    if data.password is not None:
        user.hashed_password=hash_password(data.password)
    db.commit()
    db.refresh(user)
    return user

def delete_user_by_id(
        db: Session,
        id: int
) -> bool:
    user = read_user_by_id(db, id)
    if not user:
        return False
    db.delete(user)
    db.commit()
    return True
