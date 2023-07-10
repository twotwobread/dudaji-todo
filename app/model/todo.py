from datetime import datetime
from json import dumps


class Todo:
    TODO_ID = 0

    def __init__(self, status, content) -> None:
        Todo.TODO_ID += 1
        self.__id = self.TODO_ID
        self.__status = status
        self.__content = content
        self.__created_at = datetime.now()

    def __str__(self) -> str:
        return f"id: {self.__id}, status: {self.__status}, content: {self.__content}, created_at: {self.__created_at}"

    @property
    def id(self):
        return self.__id

    @property
    def content(self):
        return self.__content

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    def convert_json(self) -> dict:
        return {
            "id": self.__id,
            "status": self.__status,
            "content": self.__content,
            "created_at": self.__created_at,
        }
