from enum import Enum, auto


class ChunkType(Enum):

    EXISTS = auto()
    NORMAL = auto()
    DETAILED = auto()
