# -----------------------------------------------------------------------------
# Name:        wxPomoTimer
# Purpose:      Main GUI for wxPomoTimer
#
# Author:      Hansel He
#
# Created:     01/09/2019
# Copyright:   (c) Hansel He 2019
# Licence:     MIT
# -----------------------------------------------------------------------------
import os
import sys
import wx
import wx.adv
import time
import winsound
import threading
from main_frame import *
from pomo_timer import *
from events import *
from common import *
from timer_config import TimerConfig, TIMER_NUM
from dlg_settings import MyDlgSettings


TIMER_EDIT_BOX_EXPAND_X = 30
TIMER_EDIT_BOX_EXPAND_Y = 0


class MainApp(wx.App):
    """Class Main App."""
    def OnInit(self):
        """Init Main App."""
        self.frame = MyMainFrame(None)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

    def OnExit(self):
        return super().OnExit()


class AlarmThread(threading.Thread):
    def __init__(self, sound_file=None, alarm_count=0):
        super(AlarmThread, self).__init__()
        self.exit_flag = False
        self.sound_file = sound_file
        self.alarm_count = alarm_count
        self.sleep = 1
        self.running = False

    def play_alarm(self, sound_file, alarm_count):
        self.sound_file = sound_file
        self.alarm_count = alarm_count

    def stop_alarm(self):
        self.alarm_count = 0

    def _do_play_sound(self):
        if self.sound_file is not None:
            try:
                winsound.PlaySound(self.sound_file,
                               winsound.SND_FILENAME)
            except Exception:
                pass

    def run(self):
        self.running = True
        while (alarm_count > 0):
            self.alarm_count -= 1
            self._do_play_sound()
            time.sleep(self.sleep)
        self.running = False

class FrameTaskBarIcon(wx.adv.TaskBarIcon):
    ID_MENU_EXIT = wx.NewId()
    ID_MENU_SETTINGS = wx.NewId()

    def __init__(self, frame, icon=APP_ICON):
        wx.adv.TaskBarIcon.__init__(self)
        self.frame = frame
        self.icon = icon
        self.SetIcon(wx.Icon(name=Utils.resource_path(icon),
                             type=wx.BITMAP_TYPE_ICO), APP_NAME)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)
        self.Bind(wx.EVT_MENU, self.OnMenuExit, id=self.ID_MENU_EXIT)
        self.Bind(wx.EVT_MENU, self.OnMenuSettings, id=self.ID_MENU_SETTINGS)

    def update_taskbar_icon(self, icon, tooltip):
        if self.IsOk():
            self.SetIcon(wx.Icon(name=Utils.resource_path(icon),
                         type=wx.BITMAP_TYPE_ICO), tooltip)

    def update(self):
        tooltip = "{}".format(APP_NAME)
        alarmed = False
        for idx in range(TIMER_NUM):
            timer = self.frame.timer_manager.timers[idx]
            tooltip = tooltip + \
                "\nT{} ({}): {}\n  {}".format(
                    idx, timer.name, timer.get_state().name,
                    timer.running_timer_data.get_str()
                )
            if timer.alarm_count > 0:  # alarmed
                tooltip = tooltip + "  (Alarmed)"
                alarmed = True

        # blink icon for alarm
        if self.frame.config.timer_alarm_blink_icon  \
                and alarmed and not self.frame.showing:
            icon = APP_BLANK_ICON
        else:
            icon = self.icon

        self.update_taskbar_icon(icon, tooltip)

    def OnTaskBarLeftDClick(self, event):
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()

    def OnMenuSettings(self, event):
        self.frame.show_settings()

    def OnMenuExit(self, event):
        self.frame.Close()

    # override
    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(self.ID_MENU_SETTINGS, '&Settings')
        menu.Append(self.ID_MENU_EXIT, '&Exit')
        return menu


# Implementing MainFrame
class MyMainFrame(MainFrame):
    def set_frame_icon(self, icon):
        self.SetIcon(wx.Icon(Utils.resource_path(icon), wx.BITMAP_TYPE_ICO))

    def apply_config(self):
        self.timer_manager.set_mode(self.config.timer_mgr_mode)
        for idx in range(TIMER_NUM):
            timer = self.timer_manager.get_timer(idx)
            self.timer_manager.set_timer_mode(idx, self.config.timer_mode[idx])
            timer.set_timer_data(self.config.timer_data[idx])
            timer.name = self.config.timer_name[idx]
        self.sound = wx.adv.Sound(self.config.timer_alarm_sound_file)

    def _load_icons(self):
        self.m_btnStop.SetBitmap(
            wx.Bitmap(
                Utils.resource_path(BTN_ICON_STOP),
                wx.BITMAP_TYPE_ANY)
        )
        self.m_btnClear.SetBitmap(
            wx.Bitmap(
                Utils.resource_path(BTN_ICON_CLEAR),
                wx.BITMAP_TYPE_ANY)
        )
        self.m_btnSet.SetBitmap(
            wx.Bitmap(
                Utils.resource_path(BTN_ICON_SETTINGS),
                wx.BITMAP_TYPE_ANY)
        )

    def __init__(self, parent):
        MainFrame.__init__(self, parent)
        icon = APP_ICON
        self.set_frame_icon(icon)
        self.taskbarIcon = FrameTaskBarIcon(self, icon)
        self.SetTitle("{} {}".format(APP_NAME, APP_VER))

        self.config = TimerConfig()

        # Init values
        self.icon_Tn = [self.m_IconT0, self.m_IconT1]
        self.timer_manager = TimerManager(self)

        self.edit_target = None
        self.btnStartPauseState = 0  # Start
        self.showing = True   # for icon or timer blinking
        self.sound = None

        # Connect Events
        self.Bind(EVT_TIMER_TICK, self.OnTimerTick)

        # Font info for icons
        self.base_font = self.m_IconT1.GetFont()
        self.bold_font = self.m_IconT0.GetFont()

        # init view
        self.apply_config()
        self.update_view()

        # load icon file to buttons
        self._load_icons()

    def SetStartBtn(self, start=True):
        if start:
            self.m_btnStart.SetBitmap(
                wx.Bitmap(
                    Utils.resource_path(BTN_ICON_START),
                    wx.BITMAP_TYPE_ANY)
            )
            self.btnStartPauseState = 0
        else:
            self.m_btnStart.SetBitmap(
                wx.Bitmap(
                    Utils.resource_path(BTN_ICON_PAUSE),
                    wx.BITMAP_TYPE_ANY)
            )
            self.btnStartPauseState = 1
        self.m_btnStart.Enable()

    def show_spin_ctrl_edit(self, target, spinEdit, max):
        target.Hide()
        size = wx.Size(target.Size.Width + TIMER_EDIT_BOX_EXPAND_X,
                       target.Size.Height + TIMER_EDIT_BOX_EXPAND_Y)

        spinEdit.SetMax(max)
        spinEdit.SetValue(target.Label)
        spinEdit.SetMaxSize(size)
        spinEdit.Show()
        self.bSizerTimer.Layout()
        spinEdit.SetFocus()
        self.edit_target = target

    # Override event handler of double Click on timer display
    def m_staticHourOnLeftDClick(self, event):
        state = self.timer_manager.get_current_timer_state()
        if self.edit_target is not None or state != TimerState.Stopped:
            return
        self.show_spin_ctrl_edit(
            self.m_staticHour, self.m_spinEditHour, (MAX_HOUR - 1))

    def m_staticMinuteOnLeftDClick(self, event):
        state = self.timer_manager.get_current_timer_state()
        if self.edit_target is not None or state != TimerState.Stopped:
            return
        self.show_spin_ctrl_edit(
            self.m_staticMinute, self.m_spinEditMinute, (MAX_MIN_SEC - 1))

    def m_staticSecondOnLeftDClick(self, event):
        state = self.timer_manager.get_current_timer_state()
        if self.edit_target is not None or state != TimerState.Stopped:
            return
        self.show_spin_ctrl_edit(
            self.m_staticSecond, self.m_spinEditSecond, (MAX_MIN_SEC - 1))

    def OnIconTnLeftDClick(self, event):
        # not allow switching timer under alternation mode
        if self.timer_manager.mode == TimerMgrMode.Alternation:
            return
        icon = event.GetEventObject()
        icon_idx = self.icon_Tn.index(icon)
        if icon_idx != self.timer_manager.timer_idx:
            self.timer_manager.set_current_timer_idx(icon_idx)
            self.update_view()

    def OnClose(self, event):
        self.timer_manager.OnExit()
        self.taskbarIcon.RemoveIcon()
        self.taskbarIcon.Destroy()
        event.Skip()    # the default event handler does call Destroy()

    def do_secondly(self):
        self.update_display_secondly()
        self.update_icons()
        self.play_alarm()
        self.taskbarIcon.update()

    def OnTimerTick(self, event):
        self.timer_manager.OnTimerTick()
        self.showing = not self.showing  # for icon blinking
        self.do_secondly()

    def OnStart(self, event):
        if self.btnStartPauseState == 0:
            self.timer_manager.OnStart()
        else:
            self.timer_manager.OnPause()

    def OnStop(self, event):
        self.timer_manager.OnStop()
        self.stop_alarm()

    def OnClear(self, event):
        self.timer_manager.OnClear()
        self.update_display()

    def show_settings(self):
        dialog = MyDlgSettings(self, self.config)
        result = dialog.ShowModal()
        if result == wx.ID_OK:
            self.config.copy(dialog.timer_config)
            self.config.save_config()
            self.apply_config()
            self.update_view()
        else:
            pass
        dialog.Destroy()

    def OnSet(self, event):
        self.show_settings()

    def OnExitEdit(self, event):
        if self.edit_target is None:
            return

        sender = event.GetEventObject()
        sender.Hide()
        if self.edit_target:
            self.edit_target.Show()
        self.bSizerTimer.Layout()
        self.update_target(sender.Value)
        self.edit_target = None
        event.Skip()

    def m_spinEditOnSpinCtrl(self, event):
        sender = event.GetEventObject()
        self.update_target(sender.Value)

    def set_timer_data(self):
        timer_data = TimerData()
        timer_data.hour = int(self.m_staticHour.Label)
        timer_data.minute = int(self.m_staticMinute.Label)
        timer_data.second = int(self.m_staticSecond.Label)
        self.timer_manager.get_current_timer().set_timer_data(timer_data)
        return timer_data

    # set timer data and save it to timer configure
    def update_timer_data(self):
        timer_data = self.set_timer_data()
        self.config.timer_data[self.timer_manager.timer_idx].copy(timer_data)

    def set_icon_Tn_font(self):
        for idx, icon in enumerate(self.icon_Tn):
            if idx == self.timer_manager.timer_idx:
                icon.SetFont(self.bold_font)
            else:
                icon.SetFont(self.base_font)

    def update_icons(self):
        timer = self.timer_manager.get_current_timer()
        state = timer.get_state()
        # Timer Icon
        self.set_icon_Tn_font()
        for idx, icon in enumerate(self.icon_Tn):
            timer_state = self.timer_manager.get_timer_state(idx)
            label = "T{}".format(idx)
            if timer_state == TimerState.Stopped or self.showing:
                icon.SetLabel(label)
            else:
                icon.SetLabel('  ')

        # show timer mode icon
        work_mode = self.timer_manager.get_work_mode()
        self.m_IconMode.SetLabel(WORKMODE_ICON_STR[work_mode])
        # Overflow icon
        if state == TimerState.Overflowed:
            self.m_IconOverflow.Show()
        else:
            self.m_IconOverflow.Hide()

        # Alarm Icon
        if timer.alarm_count > 0:
            self.m_IconAlarm.Show()
        else:
            self.m_IconAlarm.Hide()

    def update_btns(self):
        state = self.timer_manager.get_current_timer_state()
        if state == TimerState.Stopped:
            self.SetStartBtn()
            self.m_btnStop.Enable(False)
            self.m_btnClear.Enable()
        elif state == TimerState.Paused:
            self.SetStartBtn()
            self.m_btnStop.Enable()
            self.m_btnClear.Enable(False)
        elif state == TimerState.Running or state == TimerState.Alarmed:
            self.SetStartBtn(False)
            self.m_btnStop.Enable()
            self.m_btnClear.Enable(False)
        elif state == TimerState.Overflowed:
            self.SetStartBtn()
            self.m_btnStart.Enable(False)
            self.m_btnStop.Enable()
            self.m_btnClear.Enable(False)

    def show_blank_timer(self):
        self.m_staticHour.SetLabel("")
        self.m_staticMinute.SetLabel("")
        self.m_staticSecond.SetLabel("")

    def show_timer_data(self):
        timer = self.timer_manager.get_current_timer()
        timer_data = timer.running_timer_data

        if int(self.m_staticHour.Label == ""  \
                or self.m_staticHour.Label) != timer_data.hour:
            self.m_staticHour.SetLabel("{:0>2d}".format(timer_data.hour))

        if int(self.m_staticMinute.Label == ""  \
                or self.m_staticMinute.Label) != timer_data.minute:
            self.m_staticMinute.SetLabel("{:0>2d}".format(timer_data.minute))

        if self.m_staticSecond.Label == ""  \
            or int(self.m_staticSecond.Label) != timer_data.second:
            self.m_staticSecond.SetLabel("{:0>2d}".format(timer_data.second))

    def display_timer(self, show=True):
        if show:
            self.show_timer_data()
        else:
            self.show_blank_timer()

    def update_display(self):
        state = self.timer_manager.get_current_timer_state()
        if state == TimerState.Paused:
            self.display_timer(show=self.showing)
        else:  
            self.display_timer()

    def update_display_secondly(self):
        state = self.timer_manager.get_current_timer_state()
        if state == TimerState.Paused:
            self.display_timer(show=self.showing)
        elif state == TimerState.Running  \
            or state == TimerState.Alarmed:
                self.display_timer()

    def update_view(self):
        self.update_display()
        self.update_btns()
        self.update_icons()
        self.taskbarIcon.update()

    def update_target(self, value):
        if self.edit_target is None:
            return

        self.edit_target.SetLabel("{:0>2d}".format(value))
        self.update_timer_data()

    def show_notification(self, msg):
        notify = wx.adv.NotificationMessage(
            title=APP_NAME,
            message=msg, parent=None, flags=wx.ICON_INFORMATION)
        notify.Show(timeout=6)  # 1 for short timeout, 100 for long timeout

    def play_sound(self, file=None):
        try:
            # if file is not None load it, otherwise use default file
            if file:
                self.sound = wx.adv.Sound(file)
            if self.sound.IsOk():
                # self.sound.Play(wx.adv.SOUND_ASYNC)
                winsound.PlaySound('res\\sound\\beep0.wav',
                                   winsound.SND_FILENAME | winsound.SND_ASYNC)
        except NotImplementedError as v:
            wx.MessageBox(str(v), "Exception Message")

    def play_alarm(self):
        alarm = False
        for idx in range(TIMER_NUM):
            timer = self.timer_manager.timers[idx]
            if timer.alarm_count > 0:
                alarm = True
                timer.alarm_count = timer.alarm_count - 1

        if alarm and self.config.timer_alarm_sound:
            self.play_sound(self.config.timer_alarm_sound_file)

    def show_balloon(self, msg):
        self.taskbarIcon.ShowBalloon(
            APP_NAME, msg,
            self.config.timer_alarm_duration*1000, wx.ICON_INFORMATION)

    def stop_alarm(self):
        timer = self.timer_manager.get_current_timer()
        timer.alarm_count = 0

    def do_alarm(self, timer):
        # set icon, start alarm
        msg = "T{} ({}) Timer expired ({}).".format(
            timer.id, timer.name, timer.timer_data)
        if self.config.timer_alarm_notification:
            # self.show_notification(msg)
            self.show_balloon(msg)
        timer.alarm_count = self.config.timer_alarm_duration
        if self.config.timer_alarm_sound:
            self.play_alarm()


def main():
    app = MainApp(False)
    app.MainLoop()


if __name__ == '__main__':
    main()
