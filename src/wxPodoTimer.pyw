#-------------------------------------------------------------------------------
# Name:        wxPodoTimer
# Purpose:      Main GUI for wxPodoTimer
#
# Author:      Hansel He
#
# Created:     01/09/2019
# Copyright:   (c) Hansel He 2019
# Licence:     MIT
#-------------------------------------------------------------------------------
import os
import wx
import wx.adv
import time
from main_frame import *
from pomo_timer import *
from events import *
from utils import *
from config import TimerConfig


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


class MyDlgSettings(DlgSettings):
    def __init__(self, parent):
        DlgSettings.__init__(self, parent)


class FrameTaskBarIcon(wx.adv.TaskBarIcon):
    ID_MENU_EXIT = wx.NewId()
    def __init__(self, frame, icon):
        wx.adv.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.Icon(name=icon,
                             type=wx.BITMAP_TYPE_ICO), APP_NAME)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)
        self.Bind(wx.EVT_MENU, self.OnMenuExit, id=self.ID_MENU_EXIT)

    def OnTaskBarLeftDClick(self, event):
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()

    def OnMenuExit(self, event):
        self.frame.Close()

    # override
    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(self.ID_MENU_EXIT, 'Exit')
        return menu


# Implementing MainFrame
class MyMainFrame(MainFrame):
    def set_frame_icon(self, icon):
        self.SetIcon(wx.Icon(icon, wx.BITMAP_TYPE_ICO))

    def __init__(self, parent):
        MainFrame.__init__(self, parent)
        icon = u'res/wxPomoTimer.ico'
        self.set_frame_icon(icon)
        self.taskbarIcon = FrameTaskBarIcon(self, icon)

        self.config = TimerConfig()

        # Init values
        self.icon_Tn = [self.m_IconT0, self.m_IconT1]
        self.timer_manager = TimerManager(self)
        self.timer_manager.set_mode(self.config.timer_mgr_mode)
        for idx in [0,1]:
            self.timer_manager.set_timer_mode(idx, self.config.timer_mode[idx])
            self.timer_manager.timers[idx].set_timer_data(
                self.config.timer_data[idx]
            )

        self.edit_target = None
        self.btnStartPauseState = 0  # Start
        self.showing = True   # for icon or timer blinking
        self.timer_idx = 0
        self.play_alarm_times = 0

        # Connect Events
        self.Bind(EVT_TIMER_TICK, self.OnTimerTick)

        # Font info for icons
        self.base_font = self.m_IconT1.GetFont()
        self.bold_font = self.m_IconT0.GetFont()

        # init view
        self.update_view()

    def SetStartBtn(self, start=True):
        if start:
            self.m_btnStart.SetBitmap(
                wx.Bitmap(u"res/Start-icon-64.png", wx.BITMAP_TYPE_ANY))
            self.btnStartPauseState = 0
        else:
            self.m_btnStart.SetBitmap(
                wx.Bitmap(u"res/Pause-icon-64.png", wx.BITMAP_TYPE_ANY))
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
        if self.edit_target is not None:
            return
        self.show_spin_ctrl_edit(
            self.m_staticHour, self.m_spinEditHour, (MAX_HOUR - 1))

    def m_staticMinuteOnLeftDClick(self, event):
        if self.edit_target is not None:
            return
        self.show_spin_ctrl_edit(
            self.m_staticMinute, self.m_spinEditMinute, (MAX_MIN_SEC - 1))

    def m_staticSecondOnLeftDClick(self, event):
        if self.edit_target is not None:
            return
        self.show_spin_ctrl_edit(
            self.m_staticSecond, self.m_spinEditSecond, (MAX_MIN_SEC - 1))

    def OnIconTnLeftDClick(self, event):
        icon = event.GetEventObject()
        icon_idx = self.icon_Tn.index(icon)
        if icon_idx != self.timer_idx:
            self.timer_idx = icon_idx
            self.timer_manager.set_timer_idx(icon_idx)
            self.update_view()

    def OnClose(self, event):
        self.timer_manager.OnExit()
        self.taskbarIcon.RemoveIcon()
        self.taskbarIcon.Destroy()
        event.Skip()    # the default event handler does call Destroy()

    def do_secondly(self):
        self.update_display()
        self.update_icons()
        self.play_alarm()

    def OnTimerTick(self, event):
        self.timer_manager.OnTimerTick()
        self.showing = not self.showing  # for icon blinking
        self.do_secondly()

    def OnStart(self, event):
        if self.btnStartPauseState == 0:
            self.timer_manager.OnStart()
        else:
            self.timer_manager.OnPause()
        self.update_view()

    def OnStop(self, event):
        self.timer_manager.OnStop()
        self.update_view()

    def OnClear(self, event):
        self.timer_manager.OnClear()
        self.update_view()

    def OnSet(self, event):
        dialog = MyDlgSettings(self)
        result = dialog.ShowModal()
        if result == wx.ID_OK:
            pass
        else:
            pass
        dialog.Destroy()
        self.update_view()

    def OnExitEdit(self, event):
        if self.edit_target is None:
            return

        sender = event.GetEventObject()
        sender.Hide()
        self.edit_target.Show()
        self.bSizerTimer.Layout()
        self.update_target(sender.Value)
        self.edit_target = None
        event.Skip()

    def m_spinEditOnSpinCtrl(self, event):
        sender = event.GetEventObject()
        self.update_target(sender.Value)

    def show_blank_timer(self):
        self.m_staticHour.SetLabel("")
        self.m_staticMinute.SetLabel("")
        self.m_staticSecond.SetLabel("")

    def show_timer_data(self):
        timer_data = self.timer_manager.get_timer_data()

        self.m_staticHour.SetLabel("{:0>2d}".format(timer_data.hour))
        self.m_staticMinute.SetLabel("{:0>2d}".format(timer_data.minute))
        self.m_staticSecond.SetLabel("{:0>2d}".format(timer_data.second))

    def set_timer_data(self):
        timer_data = TimerData()
        timer_data.hour = int(self.m_staticHour.Label)
        timer_data.minute = int(self.m_staticMinute.Label)
        timer_data.second = int(self.m_staticSecond.Label)
        self.timer_manager.set_timer_data(timer_data)

    def set_icon_Tn_font(self):
        for idx, icon in enumerate(self.icon_Tn):
            if idx == self.timer_idx:
                icon.SetFont(self.bold_font)
            else:
                icon.SetFont(self.base_font)

    def update_icons(self):
        state = self.timer_manager.get_current_timer_state()
        prev_state = self.timer_manager.get_current_timer_prev_state()
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

        if state == TimerState.Stopped or state == TimerState.Running:
            self.m_IconOverflow.Hide()
            self.m_IconAlarm.Hide()
        elif state == TimerState.Paused or state == TimerState.Overflowed:
            if state == TimerState.Overflowed:
                self.m_IconOverflow.Show()
            else:
                self.m_IconOverflow.Hide()

            if prev_state == TimerState.Alarmed:
                self.m_IconAlarm.Show(self.showing)
            else:
                self.m_IconAlarm.Hide()
        elif state == TimerState.Alarmed:
            self.m_IconOverflow.Hide()
            self.m_IconAlarm.Show(self.showing)

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

    def update_view(self):
        self.update_display()
        self.update_btns()
        self.update_icons()

    def update_target(self, value):
        if self.edit_target is None:
            return

        self.edit_target.SetLabel("{:0>2d}".format(value))
        self.set_timer_data()

    def show_notification(self, msg):
        notify = wx.adv.NotificationMessage(
            title=APP_NAME,
            message=msg, parent=None, flags=wx.ICON_INFORMATION)
        notify.Show(timeout=6)  # 1 for short timeout, 100 for long timeout

    def play_sound(self, file):
        try:
            sound = wx.adv.Sound(file)
            sound.Play(wx.adv.SOUND_ASYNC)
            # save a reference (shoudle no need, but a bug...)
            self.sound = sound
        except NotImplementedError as v:
            wx.MessageBox(str(v), "Exception Message")

    def play_alarm(self):
        if self.play_alarm_times == 0:
            return
        self.play_sound(self.config.timer_alarm_sound_file)
        self.play_alarm_times = self.play_alarm_times - 1

    def show_balloon(self, msg):
        self.taskbarIcon.ShowBalloon(
            APP_NAME, msg,
            self.config.timer_alarm_duration*1000, wx.ICON_INFORMATION)

    def do_alarm(self, timer):
        # set icon, start alarm
        msg = "T{} Timer expired ({}).".format(
            timer.id, timer.timer_data)
        if self.config.timer_alarm_notification:
            # self.show_notification(msg)
            self.show_balloon(msg)
        if self.config.timer_alarm_sound:
            self.play_alarm_times = self.config.timer_alarm_duration


def main():
    app = MainApp(False)
    app.MainLoop()


if __name__ == '__main__':
    main()
