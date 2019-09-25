import enum


MAX_HOUR = 100
MAX_MIN_SEC = 60


@enum.unique
class TimerState(enum.Enum):
    Stopped = 0
    Running = 1
    Paused = 2
    Overflowed = 3
    Alarmed = 4


@enum.unique
class WorkMode(enum.Enum):
    Standalone = 0
    Alternation = 1


@enum.unique
class TimerMode(enum.Enum):
    OneShot = 0
    Cycling = 1
