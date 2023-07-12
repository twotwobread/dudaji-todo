from app.model.todo import Todo
from app.model.status import Status
from app.common.exception.exceptions import NotFoundException
from app.dao.todo_repository import TodoRepository


TODO_DB = {}


class TodoMemory(TodoRepository):
    def insert(self, todo: Todo) -> Todo:
        TODO_DB[todo.id] = todo
        return todo

    def get(self, todo_id) -> Todo:
        if not todo_id in TODO_DB:
            raise NotFoundException(todo_id)
        return TODO_DB[todo_id]

    def get_all(self) -> list:
        return list(map(lambda x: TODO_DB[x], TODO_DB.keys()))

    def delete(self, todo_id) -> int:
        if not todo_id in TODO_DB:
            return NotFoundException(todo_id)

        del TODO_DB[todo_id]
        return todo_id

    def clear(self) -> int:
        element_count = len(TODO_DB.keys())
        TODO_DB.clear()
        return element_count

    def update_status(self, todo: Todo, status: Status) -> Todo:
        todo.status = status
        TODO_DB[todo.id] = todo
        return todo

    def update_content(self, todo: Todo, content: str) -> Todo:
        todo.content = content
        TODO_DB[todo.id] = todo
        return todo
