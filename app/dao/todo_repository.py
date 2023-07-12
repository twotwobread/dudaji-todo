from abc import ABC, abstractmethod
from app.model.todo import Todo
from app.model.status import Status


class TodoRepository(ABC):
    @abstractmethod
    def insert(self, todo: Todo) -> Todo:
        ...

    @abstractmethod
    def get(self, todo_id: int) -> Todo:
        ...

    @abstractmethod
    def get_all(self) -> list:
        ...

    @abstractmethod
    def delete(self, todo_id: int) -> int:
        ...

    @abstractmethod
    def clear(self) -> int:
        ...

    @abstractmethod
    def update_status(self, todo: Todo, status: Status) -> Todo:
        ...

    @abstractmethod
    def update_content(self, todo: Todo, content: str) -> Todo:
        ...
