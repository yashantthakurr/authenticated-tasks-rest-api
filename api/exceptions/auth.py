
from fastapi import HTTPException, status
from jose import JWTError

INVALID_LOGIN_CREDENTIALS_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="invalid username or password"
)

INVALID_OR_EXPIRED_TOKEN_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="invalid or expired token",
    headers={"WWW-Authenticate": "Bearer"}
)
