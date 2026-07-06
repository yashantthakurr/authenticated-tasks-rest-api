
from api.core.config import settings
from api.dependencies.database import get_db
from api.exceptions.auth import INVALID_OR_EXPIRED_TOKEN_EXCEPTION, JWTError
from api.models.user import User
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session

oauth2scheme = OAuth2PasswordBearer(tokenUrl='/login')

def get_current_user(
        token: str = Depends(oauth2scheme),
        db: Session = Depends(get_db)
) -> User:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise INVALID_OR_EXPIRED_TOKEN_EXCEPTION
    except JWTError:
        raise INVALID_OR_EXPIRED_TOKEN_EXCEPTION
    user = db.query(User).filter(User.username==username).first()
    if not user:
        raise INVALID_OR_EXPIRED_TOKEN_EXCEPTION
    return user
