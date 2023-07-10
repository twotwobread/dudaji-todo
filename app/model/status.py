from enum import Enum


class Status(str, Enum):
    YET = "YET"
    PROCESS = "PROCESS"
    DONE = "DONE"
