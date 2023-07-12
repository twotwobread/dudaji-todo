from app.common.exception.exceptions import (
    BadRequestException,
    NotClassificationException,
)
from app.model.todo import Todo
from app.model.status import Status
from app.dao.todo_memory import TodoMemory


todo_repository = TodoMemory()


def create(request_data) -> Todo:
    if not request_data.get("content"):
        raise BadRequestException()

    new_todo = Todo(status=Status.YET, content=request_data["content"])
    return todo_repository.insert(new_todo)


def get_todo(todo_id) -> Todo:
    return todo_repository.get(todo_id)


def get_all_todo() -> list:
    return todo_repository.get_all()


def delete_todo(todo_id) -> int:
    todo_repository.get(todo_id)
    return todo_repository.delete(todo_id)


def clear_todo() -> int:
    return todo_repository.clear()


def update_todo_status(request_data, todo_id) -> Todo:
    if not request_data.get("status"):
        raise BadRequestException()

    update_status = request_data["status"]
    if not update_status in Status.__members__:
        raise NotClassificationException(update_status)

    todo = todo_repository.get(todo_id)
    return todo_repository.update_status(todo, status=Status[update_status])


def update_todo_content(request_data, todo_id) -> Todo:
    if not request_data.get("content"):
        raise BadRequestException()

    content = request_data["content"]
    todo = todo_repository.get(todo_id)
    return todo_repository.update_content(todo, content)
