import enum
import os
import sys

APP_NAME = r'wxPomoTimer'
APP_VER = '1.0'
APP_ICON = r'res\wxPomoTimer.ico'
APP_BLANK_ICON = r'res\blank.ico'

BTN_ICON_START = r'res\Start-icon-64.png'
BTN_ICON_STOP = r'res\Stop-icon-64.png'
BTN_ICON_PAUSE = r'res\Pause-icon-64.png'
BTN_ICON_CLEAR = r'res\Clear-icon-64.png'
BTN_ICON_SETTINGS = r'res\Settings-icon-64.png'

MAX_HOUR = 100
MAX_MIN_SEC = 60
TIMER_NUM = 2


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

    @classmethod
    def resource_path(cls, relative_path):
        '''    Return resource path'''
        if hasattr(sys, '_MEIPASS'):
            # PyInstaller created temp folder and save the path to _MEIPASS
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath('.')
        return os.path.join(base_path, relative_path)
