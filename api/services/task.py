
from api.exceptions.task import TITLE_ALREADY_TAKEN_EXCEPTION
from api.models.task import Task
from api.schemas.task import CreateTask, UpdateTask
from sqlalchemy.orm import Session
from typing import List

def add_task(
        db: Session,
        data: CreateTask
) -> Task:
    if db.query(Task).filter(Task.title==data.title).first():
        raise TITLE_ALREADY_TAKEN_EXCEPTION
    task = Task(**data.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def read_task_by_id(
        db: Session,
        id: int
) -> Task | None:
    task = db.query(Task).filter(Task.id==id).first()
    if not task:
        return None
    return task

def read_all_tasks(
        db: Session
) -> List[Task]:
    return db.query(Task).all()

def update_task_by_id(
        db: Session,
        id: int,
        data: UpdateTask
) -> Task | None:
    task = read_task_by_id(db, id)
    if not task:
        return None
    if data.title is not None:
        if db.query(Task).filter(Task.title==data.title, Task.id!=id).first():
            raise TITLE_ALREADY_TAKEN_EXCEPTION
        task.title=data.title
    if data.description is not None:
        task.description=data.description
    if data.is_done is not None:
        task.is_done=data.is_done
    db.commit()
    db.refresh(task)
    return task

def delete_task_by_id(
        db: Session,
        id: int
) -> bool:
    task = read_task_by_id(db, id)
    if not task:
        return False
    db.delete(task)
    db.commit()
    return True
