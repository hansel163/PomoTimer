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
import time
from main_frame import *
from pomo_timer import *
from events import *
from const import *


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


# Implementing MainFrame
class MyMainFrame(MainFrame):
    def __init__(self, parent):
        MainFrame.__init__(self, parent)

        # Init values
        self.icon_Tn = [self.m_IconT1, self.m_IconT2]
        self.timer_manager = TimerManager(self)
        self.edit_target = None
        self.btnStartPauseState = 0  # Start
        self.showing = True   # for icon or timer blinking
        self.timer_idx = 0

        # Connect Events
        self.Bind(EVT_TIMER_TICK, self.OnTimerTick)

        # Font info for icons
        self.base_font = self.m_IconT2.GetFont()
        self.bold_font = self.m_IconT1.GetFont()

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
        event.Skip()    # the default event handler does call Destroy()

    def OnTimerTick(self, event):
        self.timer_manager.OnTimerTick()
        self.showing = not self.showing
        self.update_display()
        self.update_icons()

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
            label = "T{}".format(idx+1)
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

    def do_alarm(self, action=True):
        # set icon, start alarm
        pass


def main():
    app = MainApp(False)
    app.MainLoop()


if __name__ == '__main__':
    main()
