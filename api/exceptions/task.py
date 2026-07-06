
from fastapi import HTTPException, status

TASK_BY_ID_NOT_FOUND_EXCEPTION = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="no task found with the provided ID"
)

TASK_BY_TITLE_NOT_FOUND_EXCEPTION = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="no task found with the provided title"
)

TITLE_ALREADY_TAKEN_EXCEPTION = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="task with this title already exists. try with some other title."
)
