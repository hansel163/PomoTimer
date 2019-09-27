import configparser
from utils import *
from pomo_timer import TimerData

CONFIG_FILE = 'wxPomoTimer.cfg'
# ------------------------------------
SECTION_TIMER_MGR = 'TimerManager'
TIMER_MGR_MODE = 'mode'
# ------------------------------------
SECTION_TIMER_PREFIX = 'Timer'
TIMER_NAME = 'name'
TIMER_MODE = 'mode'
TIMER_DATA = 'data'
# ------------------------------------
SECTION_ALARM = 'Alarm'
ALARM_SOUND = 'sound'
ALARM_SOUND_FILE = 'sound_file'
ALARM_NOTIFICATION = 'notification'
ALARM_BLINK_ICON = 'blink_icon'
ALARM_DURATION = 'duration'
# ------------------------------------
DEFAULT_ALAMR_SOUND_FILE = u"res\\sound\\beep0.wav"
DEFAULT_ALARM_DURATION = 8
DEFAULT_TIMER0_NAME = 'Working'
DEFAULT_TIMER1_NAME = 'Break'


class TimerConfig(object):
    def reset(self):
        self.timer_mgr_mode = TimerMgrMode.Standalone
        self.timer_mode = [TimerMode.OneShot, TimerMode.OneShot]
        self.timer_data = [TimerData(0, 25, 0), TimerData(0, 5, 0)]
        self.timer_name = [DEFAULT_TIMER0_NAME, DEFAULT_TIMER1_NAME]
        self.timer_alarm_sound = True
        self.timer_alarm_sound_file = DEFAULT_ALAMR_SOUND_FILE
        self.timer_alarm_notification = True
        self.timer_alarm_blink_icon = True
        self.timer_alarm_duration = DEFAULT_ALARM_DURATION

    def __init__(self, cfg_file=CONFIG_FILE):
        super().__init__()
        self.reset()
        self.cfg_file = cfg_file

        if cfg_file:
            self.read_config_file(cfg_file)

    def copy(self, source):
        if isinstance(source, TimerConfig):
            self.timer_mgr_mode = source.timer_mgr_mode
            self.timer_name = source.timer_name.copy()
            self.timer_mode = source.timer_mode.copy()
            self.timer_data = source.timer_data.copy()
            self.timer_alarm_sound = source.timer_alarm_sound
            self.timer_alarm_sound_file = source.timer_alarm_sound_file
            self.timer_alarm_notification = source.timer_alarm_notification
            self.timer_alarm_blink_icon = source.timer_alarm_blink_icon
            self.timer_alarm_duration = source.timer_alarm_duration

    def read_config_file(self, cfg_file):
        if not Utils.is_file_access(cfg_file):
            return False
        self.cfg_file = cfg_file
        config = configparser.ConfigParser()
        try:
            config.read(cfg_file)
            self.timer_mgr_mode = TimerMgrMode[config.get(
                SECTION_TIMER_MGR,
                TIMER_MGR_MODE,
                fallback='Standalone')]
            for i in [0, 1]:
                section = SECTION_TIMER_PREFIX + str(i)
                self.timer_name[i] = config.get(
                    section, TIMER_NAME,
                    fallback=DEFAULT_TIMER0_NAME if i == 0 else
                    DEFAULT_TIMER1_NAME
                )
                self.timer_mode[i] = TimerMode[config.get(
                    section, TIMER_MODE, fallback='OneShot')]
                self.timer_data[i].set_from_string(config.get(
                    section, TIMER_DATA, fallback='00:25:00' if i == 0 else
                    '00:05:00')
                )

            self.timer_alarm_sound = config.getboolean(
                SECTION_ALARM,
                ALARM_SOUND, fallback=True)
            self.timer_alarm_sound_file = config.get(
                SECTION_ALARM,
                ALARM_SOUND_FILE, fallback=DEFAULT_ALAMR_SOUND_FILE)
            self.timer_alarm_notification = config.getboolean(
                SECTION_ALARM,
                ALARM_NOTIFICATION, fallback=True)
            self.timer_alarm_blink_icon = config.getboolean(
                SECTION_ALARM,
                ALARM_BLINK_ICON, fallback=True)
            self.timer_alarm_duration = config.getint(
                SECTION_ALARM,
                ALARM_DURATION, fallback=DEFAULT_ALARM_DURATION)
        except Exception:
            return False

        return True

    def read_config(self):
        return self.read_config_file(self.cfg_file)

    def save_config_file(self, cfg_file):
        result = True
        self.cfg_file = cfg_file
        config = configparser.ConfigParser()
        config.add_section(SECTION_TIMER_MGR)
        config.set(SECTION_TIMER_MGR, TIMER_MGR_MODE, self.timer_mgr_mode.name)

        for i, mode in enumerate(self.timer_mode):
            section = SECTION_TIMER_PREFIX + str(i)
            config.add_section(section)
            config.set(section, TIMER_NAME, self.timer_name[i])
            config.set(section, TIMER_MODE, mode.name)
            config.set(section, TIMER_DATA, self.timer_data[i].get_str())

        config.add_section(SECTION_ALARM)
        config.set(SECTION_ALARM, ALARM_SOUND, str(self.timer_alarm_sound))
        config.set(
            SECTION_ALARM, ALARM_SOUND_FILE, self.timer_alarm_sound_file)
        config.set(
            SECTION_ALARM, ALARM_NOTIFICATION,
            str(self.timer_alarm_notification)
        )
        config.set(
            SECTION_ALARM, ALARM_BLINK_ICON,
            str(self.timer_alarm_blink_icon)
        )
        config.set(
            SECTION_ALARM, ALARM_DURATION, str(self.timer_alarm_duration))
        try:
            config.write(open(cfg_file, "w"))
        except Exception:
            result = False

        return result

    def save_config(self):
        return self.save_config_file(self.cfg_file)


def test():
    config = TimerConfig()
    config.save_config()


if __name__ == '__main__':
    test()
