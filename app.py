from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class TodoItem(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

app = FastAPI()

todos = {}

@app.get("/")
async def home():
    return todos

@app.get(("/todo/{todo_id}"))
async def task(todo_id : int):
    if todo_id in todos:
        return todo_id,todos.get(todo_id)
    else:
        return "Not found"

@app.post("/todo")
async def create_todo(todo: TodoItem):
    todo_id = len(todos) + 1
    todos[todo_id] = todo
    return "To-do item created"

@app.put("/todo/{todo_id}")
async def update_todo(todo_id: int, todo: TodoItem):
    if todo_id in todos:
        todos[todo_id] = todo
        return "To-do item updated"
    else:
        return "To-do item not found"

@app.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int):
    if todo_id in todos:
        del todos[todo_id]
        return "To-do item deleted"
    else:
        return "To-do item not found"