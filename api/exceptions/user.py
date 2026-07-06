
from fastapi import HTTPException, status

USER_BY_ID_NOT_FOUND_EXCEPTION = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="no user found with the provided ID"
)

USER_BY_USERNAME_NOT_FOUND_EXCEPTION = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="no user found with the provided username"
)

EMAIL_ALREADY_TAKEN_EXCEPTION = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="user with this email already exists. try with some other email."
)

USERNAME_ALREADY_TAKEN_EXCEPTION = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="user with this username already exists. try with some other username."
)
