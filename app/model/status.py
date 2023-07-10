from enum import Enum


class Status(str, Enum):
    YET = "YET"
    PROGRESS = "PROGRESS"
    DONE = "DONE"
