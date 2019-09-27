import enum
import os


APP_NAME = 'wxPomoTimer'
APP_ICON = u'res/wxPomoTimer.ico'
APP_BLANK_ICON = u'res/blank.ico'

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

class Utils(object):
    def __init__(self):
        super().__init__()
    
    @classmethod
    def is_file_access(cls, file):
        return os.access(file, os.F_OK)

    @classmethod
    def limit_int(cls, value, min_val, max_val):
        if value < min_val:
            return min_val
        elif value > max_val:
            return max_val
        else:
            return value
