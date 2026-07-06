
from api.core.config import settings
from api.models.user import User
from api.schemas.user import LoginUser
from datetime import datetime, timedelta, timezone
from jose import jwt
from pwdlib import PasswordHash
from sqlalchemy.orm import Session
from typing import Dict

password_hash = PasswordHash.recommended()

def hash_password(
        plain_password: str
) -> str:
    return password_hash.hash(plain_password)

def verify_password(
        plain_password: str,
        hashed_password: str
) -> bool:
    return password_hash.verify(plain_password, hashed_password)

def create_access_token(
        username: str
) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": username, "exp": expire}
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def login_user(
        db: Session,
        data: LoginUser
) -> Dict | None:
    user = db.query(User).filter(User.username==data.username).first()
    if not user or not verify_password(data.password, user.hashed_password):
        return None
    return {"access_token": create_access_token(data.username), "token_type": "bearer"}
