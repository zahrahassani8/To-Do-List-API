from fastapi import FastAPI
from routes import todos

app = FastAPI()

app.include_router(todos.router)
