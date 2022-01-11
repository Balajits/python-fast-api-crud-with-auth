from fastapi import HTTPException, status
from sqlalchemy.orm import Session, session
from models import TaskModel
from schemas import TaskSchemas
from datetime import datetime
from sqlalchemy import func


def create_task(db: Session, task: TaskSchemas.Task, id: int):
    try:
        result = TaskModel.Task(title = task.title, description = task.description, is_complete = task.is_complete, created_by = id)
        db.add(result)
        db.commit()
        db.refresh(result)
        return True
    except Exception as e:
        return False, e


def get_task_by_id(db: Session, taskid: int, user_id: int):
    try:
        result = db.query(TaskModel.Task).filter(TaskModel.Task.id == taskid).first()
        if result is None:
            return False, 'task id not found'
        elif int(result.created_by) != int(user_id):
            return  False, 'Not authorized to perform requested action'
        else:
            return True, result
    except Exception as e:
        return False, e


def update_task(db: Session, task: TaskSchemas.TaskUpdate):
    try:
        result = db.query(TaskModel.Task).filter(TaskModel.Task.id == task.id)
        result.update(task.dict(), synchronize_session = False)
        db.commit()
        result.first()
        return True
    except Exception as e:
        return e


def detete_task(db: Session, id: int):
    try:
        result = db.query(TaskModel.Task).filter(TaskModel.Task.id == id)
        result.delete(synchronize_session = False)
        db.commit()
        result.first()
        return True
    except Exception as e:
        return e


def get_task_lists(db: Session, data: TaskSchemas.TaskList, id: int):
    try:
        result = db.query(TaskModel.Task).filter(TaskModel.Task.title.contains(data.search),TaskModel.Task.created_by == id).limit(data.limit).offset(data.offset).all()
        total_count = db.query(TaskModel.Task).filter(TaskModel.Task.created_by == id).count()
        return True, result, total_count
    except Exception as e:
        return False, e