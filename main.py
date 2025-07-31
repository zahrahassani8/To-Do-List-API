from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List


app = FastAPI()

TODOS = [
    {"id": 1, "title": "studying", "description": "for exams", "status": False},
    {"id": 2, "title": "walking", "description": "on the street", "status": False},
    {"id": 3, "title": "going to the gym",
        "description": "for exercise", "status": False},
    {"id": 4, "title": "reading", "description": "a book", "status": False},
    {"id": 5, "title": "eating", "description": "healthy", "status": False},
]


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


@app.get("/")
async def home():
    return {"message": "FastAPI is working!"}
