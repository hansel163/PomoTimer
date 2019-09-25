import enum


MAX_HOUR = 100
MAX_MIN_SEC = 60


@enum.unique
class TimerState(enum.Enum):
    Invalid = 0
    Stopped = 1
    Running = 2
    Paused = 3
    Overflowed = 4
    Alarmed = 5


@enum.unique
class WorkMode(enum.Enum):
    Standalone = 0
    Alternation = 1


@enum.unique
class TimerMode(enum.Enum):
    OneShot = 0
    Cycling = 1
