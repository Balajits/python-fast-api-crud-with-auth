from typing import Optional
from pydantic import BaseModel, EmailStr


class Task(BaseModel):
    title: str
    description: str
    is_complete: bool

    class Config:
        orm_mode = True


class TaskUpdate(Task):
    title: str
    description: str
    is_complete: bool
    id: int


class TaskList(BaseModel):
    limit: int = 5
    offset: int = 0
    search: str = ''