import enum


APP_NAME = 'wxPomoTimer'
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
class TimerMgrMode(enum.Enum):
    Standalone = 0
    Alternation = 1


@enum.unique
class TimerMode(enum.Enum):
    OneShot = 0
    Cycling = 1


@enum.unique
class WorkMode(enum.Enum):
    OneShot = 0
    Cycling = 1
    Alternation = 2


# Timer Work Mode Icon String
WORKMODE_ICON_STR = {
    WorkMode.OneShot: '   ',
    WorkMode.Cycling: 'Cyc',
    WorkMode.Alternation: 'Alt'
}
