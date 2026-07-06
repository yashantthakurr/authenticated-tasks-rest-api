
from api.dependencies.database import get_db
from api.dependencies.auth import get_current_user
from api.exceptions.task import TASK_BY_ID_NOT_FOUND_EXCEPTION
from api.models.task import Task
from api.models.user import User
from api.schemas.task import CreateTask, ResponseTask, UpdateTask
from api.services import task as taskservice
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Dict, List

router = APIRouter(
    tags=["Tasks API Routes"],
    prefix='/tasks'
)

@router.post('/add', response_model=ResponseTask)
def create_new_task(
        data: CreateTask,
        user: User = Depends(get_current_user),
        db: Session = Depends(get_db) 
) -> Task:
    return taskservice.add_task(db, data)

@router.get('/search/id/{id}', response_model=ResponseTask)
def get_task_by_id(
    id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> Task:
    task = taskservice.read_task_by_id(db, id)
    if not task:
        raise TASK_BY_ID_NOT_FOUND_EXCEPTION
    return task

@router.get('/search/all', response_model=List[ResponseTask])
def get_all_tasks(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> List[Task]:
    return taskservice.read_all_tasks(db)

@router.patch('/update/id/{id}', response_model=ResponseTask)
def update_task_by_id(
    id: int,
    data: UpdateTask,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> Task:
    task = taskservice.update_task_by_id(db, id, data)
    if not task:
        raise TASK_BY_ID_NOT_FOUND_EXCEPTION
    return task

@router.delete('/delete/id/{id}', response_model=None)
def delete_task_by_id(
    id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> Dict:
    task = taskservice.delete_task_by_id(db, id)
    if not task:
        raise TASK_BY_ID_NOT_FOUND_EXCEPTION
    return {"message": "task deleted successfully!"}
