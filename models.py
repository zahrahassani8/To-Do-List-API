from pydantic import BaseModel
from typing import Optional


class Todo(BaseModel):
    id: int
    title: str
    description: str
    status: bool


class CreateTodo(BaseModel):
    title: str
    description: str
    status: bool


class UpdateTodo(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[bool] = None
