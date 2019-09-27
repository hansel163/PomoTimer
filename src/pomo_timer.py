# -----------------------------------------------------------------------------
# Name:        timer
# Purpose:     implement timer functions
#
# Author:      Hansel He
#
# Created:     01/09/2019
# Copyright:   (c) Hansel He 2019
# Licence:     MIT
# -----------------------------------------------------------------------------
import threading
import wx
import time
from events import *
from common import *
from state_machine import TimerStateMachine


class TimerData():
    def __init__(self, hour=0, minute=0, second=0):
        self.set(hour, minute, second)

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if value < 0:
            self._hour = 0
        elif value < MAX_HOUR:
            self._hour = value
        else:
            self._hour = value % MAX_HOUR   # overflowed

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        if value < 0:
            self._minute = 0
        elif value < MAX_MIN_SEC:
            self._minute = value
        else:
            self._minute = value % MAX_MIN_SEC   # overflowed

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, value):
        if value < 0:
            self._second = 0
        elif value < MAX_MIN_SEC:
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
        return (self._hour == 0) \
            and (self._minute == 0) and (self._second == 0)

    def set(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def set_from_string(self, timer_data_str):
        data = timer_data_str.split(':')
        time = [int(x) for x in data]
        if len(time) != 3:
            return False
        else:
            self.set(time[0], time[1], time[2])
            return True

    def clear(self):  # set hour, minute and second to 0
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
        return second // MAX_MIN_SEC  # borrow or loan from minute

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
        elif hour < 0:  # underflow, set to all zero
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
    def __init__(self, win=None, sleep=1):
        super(TimerThread, self).__init__()
        self.win = win
        self.sleep = sleep
        self.running = False
        self.exit_flag = False

    def tick(self):
        if self.win:
            # Create the event
            evt = TimerTickEvent()
            # Post the event
            wx.PostEvent(self.win, evt)

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


class PomoTimer():
    def __init__(self, manager, id, name="",
                 timer_data=None, mode=TimerMode.OneShot):
        if timer_data is None:
            self.timer_data = TimerData()
        else:
            self.timer_data = timer_data
        self.manager = manager
        self.id = id
        self.name = name

        self.step = 1
        self.mode = mode
        self.state_machine = TimerStateMachine(self)
        self.running_timer_data = TimerData()
        self.running_timer_data.copy(self.timer_data)

        # running flags
        self.delay_to_restart = -1  # delay x second to restart timer

    def start(self):
        self.state_machine.on_start()

    def stop(self):
        self.state_machine.on_stop()

    def pause(self):
        self.state_machine.on_pause()

    def restart(self):
        self.restore_timer()
        self.start()

    def set_timer_data(self, timer_data):
        self.timer_data = timer_data
        self.running_timer_data.copy(self.timer_data)

    def set_mode(self, mode):
        self.mode = mode

    def get_state(self):
        return self.state_machine.get_state()

    def get_prev_state(self):
        return self.state_machine.get_prev_state()

    def calc_step(self):
        if self.timer_data.is_zero():
            self.step = 1   # count up
        else:
            self.step = -1  # count down

    def restore_timer(self):
        # restore original timer data
        self.running_timer_data.copy(self.timer_data)

    def clear(self):
        self.timer_data.clear()
        self.running_timer_data.clear()

    def do_delay_to_restart(self):
        if self.delay_to_restart < 0:
            return
        
        self.delay_to_restart = self.delay_to_restart - 1
        if self.delay_to_restart == 0:
            self.delay_to_restart = -1
            self.restart()

    def do_second(self):
        self.do_delay_to_restart()

    def tick(self):
        state = self.get_state()
        if state == TimerState.Running  \
            or (state == TimerState.Alarmed and self.mode != TimerMode.Cycling):
            self.running_timer_data.step(self.step)
            # count-down timer is 0:0:0
            if self.running_timer_data.is_zero():
                self.state_machine.on_alarm()
            elif self.running_timer_data.is_max():
                self.state_machine.on_overflow()
        self.do_second()


class TimerManager():
    def __init__(self, frame, mode=TimerMgrMode.Standalone):
        self.frame = frame

        # Init values
        self.timer_idx = 0
        self.mode = mode
        self.timers = []
        for i in range(TIMER_NUM):
            self.timers.append(PomoTimer(self, i))

        # Start timer thread
        self.timer_thread = TimerThread(frame)
        self.timer_thread.start()

    def OnTimerTick(self):
        for timer in self.timers:
            timer.tick()

    def OnStart(self):
        if not self.timer_thread.running:
            self.timer_thread.go()

        self.timers[self.timer_idx].start()

    def OnPause(self):
        self.timers[self.timer_idx].pause()

    def OnStop(self):
        self.timers[self.timer_idx].stop()

    def OnClear(self):
        if self.timers[self.timer_idx].get_state() == TimerState.Stopped:
            self.timers[self.timer_idx].clear()

    def OnExit(self):
        if self.timer_thread.is_alive():
            self.timer_thread.exit()
            self.timer_thread.join()

    def set_current_timer_idx(self, idx):
        if idx < TIMER_NUM:
            self.timer_idx = idx

    def get_current_timer_idx(self):
        return self.timer_idx

    def get_timer(self, idx):
        return self.timers[idx]

    def get_current_timer(self):
        return self.get_timer(self.timer_idx)

    def set_mode(self, mode):
        if isinstance(mode, TimerMgrMode):
            self.mode = mode

    def set_timer_mode(self, idx, mode):
        if isinstance(mode, TimerMode):
            self.timers[idx].set_mode(mode)

    def get_timer_state(self, timer_idx):
        return self.timers[timer_idx].get_state()

    def get_current_timer_state(self):
        return self.get_timer_state(self.timer_idx)

    def get_timer_prev_state(self, timer_idx):
        return self.timers[timer_idx].get_prev_state()

    def get_current_timer_prev_state(self):
        return self.get_timer_prev_state(self.timer_idx)

    def get_work_mode(self):
        if self.mode == TimerMgrMode.Alternation:
            return WorkMode.Alternation
        elif self.timers[self.timer_idx].mode == TimerMode.Cycling:
            return WorkMode.Cycling
        else:
            return WorkMode.OneShot

    def get_next_timer_id(self, current_id):
        next_id = current_id + 1
        next_id = next_id if next_id < TIMER_NUM else 0
        return next_id

    def alternate_timer(self, current_id):
        next_id = self.get_next_timer_id(current_id)

    def timer_expired(self, timer):
        self.frame.do_alarm(timer)
        if self.mode == TimerMgrMode.Alternation:
            self.alternate_timer(timer.id)

    def timer_overflow(self, timer):
        pass

    def on_timer_state_changed(self, timer):
        # update UI if current timer state changed
        if timer.id == self.timer_idx:
            self.frame.update_view()


def test():
    pass


if __name__ == '__main__':
    test()
