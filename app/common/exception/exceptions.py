from ..http_status import HttpStatus


class NotFoundException(Exception):
    status_code = HttpStatus.NOT_FOUND

    def __init__(self, word, payload=None) -> None:
        self.__message = f"{word} can't find data"
        self.__payload = payload

    def to_json(self):
        return dict(
            status=NotFoundException.status_code,
            message=self.__message,
            data=self.__payload,
        )


class BadRequestException(Exception):
    status_code = HttpStatus.BAD_REQUEST

    def __init__(self, payload=None) -> None:
        self.__message = "request value is invalidated"
        self.__payload = payload

    def to_json(self):
        return dict(
            status=NotFoundException.status_code,
            message=self.__message,
            data=self.__payload,
        )


class NotClassificationException(Exception):
    status_code = HttpStatus.BAD_REQUEST

    def __init__(self, word, payload=None) -> None:
        self.__message = f"{word} don't exist classification"
        self.__payload = payload

    def to_json(self):
        return dict(
            status=NotFoundException.status_code,
            message=self.__message,
            data=self.__payload,
        )
