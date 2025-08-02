from fastapi import APIRouter, HTTPException
from typing import List, Optional
from models import Todo, CreateTodo, UpdateTodo

router = APIRouter()

TODOS = [
    {"id": 1, "title": "studying", "description": "for exams", "status": False},
    {"id": 2, "title": "walking", "description": "on the street", "status": False},
    {"id": 3, "title": "going to the gym",
        "description": "for exercise", "status": False},
    {"id": 4, "title": "reading", "description": "a book", "status": False},
    {"id": 5, "title": "eating", "description": "healthy", "status": False},
]


@router.get("/", tags=["TODO List"])
async def home():
    return {"message": "FastAPI is working!"}


@router.get("/todos", response_model=List[Todo])
async def get_all_todos(limit: Optional[int] = None):
    return TODOS[:limit] if limit else TODOS


@router.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    for todo in TODOS:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Not found.")


@router.post("/todos", response_model=Todo, status_code=201)
async def create_todo(todo: CreateTodo):
    new_id = TODOS[-1]["id"] + 1 if TODOS else 1
    new_todo = todo.dict()
    new_todo["id"] = new_id
    TODOS.append(new_todo)
    return new_todo


@router.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, updated_todo: UpdateTodo):
    for todo in TODOS:
        if todo["id"] == todo_id:
            updates = updated_todo.dict(exclude_unset=True)
            todo.update(updates)
            return todo
    raise HTTPException(status_code=404, detail="Not found.")


@router.delete("/todos/{todo_id}", status_code=204)
async def delete_todo(todo_id: int):
    for index, todo in enumerate(TODOS):
        if todo["id"] == todo_id:
            TODOS.pop(index)
            return
    raise HTTPException(status_code=404, detail="Not found.")
