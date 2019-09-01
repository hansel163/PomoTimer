#-------------------------------------------------------------------------------
# Name:        timer
# Purpose:     implement timer functions
#
# Author:      Hansel He
#
# Created:     01/09/2019
# Copyright:   (c) Hansel He 2019
# Licence:     MIT
#-------------------------------------------------------------------------------
import threading
import wx
import time
import enum
from events import *

MAX_HOUR = 100
MAX_MIN_SEC = 60


class TimerData():
    def __init__(self, hour=0, minute=0, second=0):
        self.set(hour, minute, second)

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if value < MAX_HOUR:
            self._hour = value
        else:
            self._hour = value % MAX_HOUR   # overflowed

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        if value < MAX_MIN_SEC:
            self._minute = value
        else:
            self._minute = value % MAX_MIN_SEC   # overflowed

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, value):
        if value < MAX_MIN_SEC:
            self._second = value
        else:
            self._second = value % MAX_MIN_SEC   # overflowed

    def copy(self, source):
        if isinstance(source, TimerData):
            self.hour = source.hour
            self.minute = source.minute
            self.second = source.second

    def is_max(self):
        return (self._hour == (MAX_HOUR-1)) \
            and (self._minute == (MAX_MIN_SEC-1)) \
            and (self._second == (MAX_MIN_SEC-1))

    def is_zero(self):
        return (self._hour == 0) and (self._minute == 0) and (self._second == 0)

    def set(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def clear(self): # set hour, minute and second to 0
        self.set()

    def set_max(self):
        self._hour = MAX_HOUR - 1
        self._minute = MAX_MIN_SEC - 1
        self._second = MAX_MIN_SEC - 1

    def get_str(self):
        return "{:0>2d}:{:0>2d}:{:0>2d}".format(self.hour, self.minute, self.second)

    def __str__(self):
        return self.get_str()

    def step_second(self, value):
        second = self.second + value
        self.second = second % MAX_MIN_SEC
        return second // MAX_MIN_SEC # borrow or loan from minute

    def step_minute(self, value):
        minute = self.minute + value
        self.minute = minute % MAX_MIN_SEC
        return minute // MAX_MIN_SEC  # borrow or loan from hour

    # return: 1 is for overflow, -1 is for underflow, 0 is okay
    def step_hour(self, value):
        hour = self.hour + value
        # if overflow, set time to max data
        if hour >= MAX_HOUR:
            self.set_max()
            return 1
        elif hour < 0: # underflow, set to all zero
            self.clear()
            return -1
        else:
            self.hour = hour
            return 0
    
    # negative value is decrease, positive value is increase
    def step(self, value=1):
        minute = self.step_second(value)
        hour = self.step_minute(minute)
        overflow = self.step_hour(hour)
        return overflow       

class TimerThread(threading.Thread):
    def __init__(self, frame=None, sleep=1):
        super(TimerThread, self).__init__()
        self.frame = frame
        self.sleep = sleep
        self.running = False
        self.exit_flag = False

    def tick(self):
        if self.frame is None:
            return
        # Create the event
        evt = TimerTickEvent()
        # Post the event
        wx.PostEvent(self.frame, evt)

    def set_sleep(self, sleep):
        self.sleep = sleep

    def go(self):
        self.running = True

    def stop(self):
        self.running = False

    def exit(self):
        self.exit_flag = True

    def run(self):
        while (not self.exit_flag):
            time.sleep(self.sleep)
            if self.running:
                self.tick()


@enum.unique
class TimerState(enum.Enum):
    Stopped = 0
    Running = 1
    Paused = 2

class PomoTimer():
    def __init__(self, frame, timer_data=None):
        if timer_data is None:
            self.timer_data = TimerData()
        else:
            self.timer_data = timer_data
        self.frame = frame
        self.timer_thread = TimerThread(frame)
        self.timer_thread.start()
        self.step = 1
        self.running_timer_data = TimerData()
        self.running_timer_data.copy(self.timer_data)
        self.state = TimerState.Stopped
        self.show_blank = False     # for flashing timer display

    def exit(self):
        if self.timer_thread.is_alive():
            self.timer_thread.exit()
            self.timer_thread.join()
            self.state = TimerState.Stopped

    def __del__(self):
        self.exit()

    def set(self, timer_data):
        self.timer_data = timer_data
        self.running_timer_data.copy(self.timer_data)

    def get_state(self):
        return self.state

    def start(self):
        if self.state != TimerState.Paused:
            if self.timer_data.is_zero():
                self.step = 1   # count up
            else:
                self.step = -1  # count down

        self.timer_thread.go()
        self.state = TimerState.Running

    def pause(self):
        self.state = TimerState.Paused

    def stop(self):
        self.timer_thread.stop()
        # restore original timer data
        self.running_timer_data.copy(self.timer_data)
        self.update_display()
        self.state = TimerState.Stopped

    def clear(self):
        # do not clear timer data when timer is running
        if self.state == TimerState.Running:
            return

        self.timer_data.clear()
        self.running_timer_data.clear()
        self.update_display()
        # after clear timer data, set timer to stopped status
        self.state = TimerState.Stopped

    def update_display(self, str=None):
        if str is not None:
            self.frame.update_display(str)
        else:
            self.frame.update_display(self.running_timer_data.get_str())

    def flash_timer(self):
        if self.show_blank:
            self.update_display("")
            self.show_blank = False
        else:
            self.update_display()
            self.show_blank = True

    def alarm_timer(self):
        self.frame.alarm_timer()

    def OnTimerTick(self, event):
        if self.state == TimerState.Running:
            self.running_timer_data.step(self.step)
            # update UI
            self.update_display()
        elif self.state == TimerState.Paused:
            self.flash_timer()

                
            



