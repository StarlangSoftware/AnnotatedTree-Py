from enum import Enum, auto


class SearchType(Enum):

    EQUALS = auto()
    EQUALS_IGNORE_CASE = auto()
    CONTAINS = auto()
    MATCHES = auto()
    STARTS = auto()
    ENDS = auto()
    IS_NULL = auto()

