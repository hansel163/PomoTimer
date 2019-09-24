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
        self.edit_target = None


        # Connect Events
        self.m_btnStart.Bind(wx.EVT_BUTTON, self.OnStart)
        self.m_btnStop.Bind(wx.EVT_BUTTON, self.OnStop)
        self.m_btnClear.Bind(wx.EVT_BUTTON, self.OnClear)
        self.m_btnSet.Bind(wx.EVT_BUTTON, self.OnSet)

        self.timer = PomoTimer(self)
        self.Bind(EVT_TIMER_TICK, self.timer.OnTimerTick)

    def SetStartBtn(self, start=True):
        if start:
            self.m_btnStart.SetBitmap(
                wx.Bitmap(u"res/Start-icon-64.png", wx.BITMAP_TYPE_ANY))
        else:
            self.m_btnStart.SetBitmap(
                wx.Bitmap(u"res/Pause-icon-64.png", wx.BITMAP_TYPE_ANY))

    def show_spin_ctrl_edit(self, target, spinEdit, value, max):
        target.Hide()
        size = wx.Size(target.Size.Width + TIMER_EDIT_BOX_EXPAND_X,
                       target.Size.Height + TIMER_EDIT_BOX_EXPAND_Y)

        spinEdit.SetMax(max)
        spinEdit.SetValue("{:0>2d}".format(value))
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
            self.m_staticHour, self.m_spinEditHour,
            self.timer.running_timer_data.hour, (MAX_HOUR - 1))

    def m_staticMinuteOnLeftDClick(self, event):
        if self.edit_target is not None:
            return
        self.show_spin_ctrl_edit(
            self.m_staticMinute, self.m_spinEditMinute,
            self.timer.running_timer_data.minute, (MAX_MIN_SEC - 1))

    def m_staticSecondOnLeftDClick(self, event):
        if self.edit_target is not None:
            return
        self.show_spin_ctrl_edit(
            self.m_staticSecond, self.m_spinEditSecond,
            self.timer.running_timer_data.second, (MAX_MIN_SEC - 1))

    def MainFrameOnClose(self, event):
        self.timer.exit()
        event.Skip()    # the default event handler does call Destroy()

    def OnStart(self, event):
        if self.timer.get_state() == TimerState.Running: # pause timer
            self.SetStartBtn()
            self.timer.pause()
        else: # start timer
            self.timer.start()
            self.SetStartBtn(False)

    def OnStop(self, event):
        self.timer.stop()
        self.SetStartBtn()

    def OnClear(self, event):
        self.timer.clear()

    def OnSet(self, event):
        dialog = MyDlgSettings(self)
        result = dialog.ShowModal()
        if result == wx.ID_OK:
            pass
        else:
            pass
        dialog.Destroy()

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
        timer_data = self.timer.running_timer_data

        self.m_staticHour.SetLabel("{:0>2d}".format(timer_data.hour))
        self.m_staticMinute.SetLabel("{:0>2d}".format(timer_data.minute))
        self.m_staticSecond.SetLabel("{:0>2d}".format(timer_data.second))

    def set_timer_data(self):
        timer_data = TimerData()
        timer_data.hour = int(self.m_staticHour.Label)
        timer_data.minute = int(self.m_staticMinute.Label)
        timer_data.second = int(self.m_staticSecond.Label)
        self.timer.set(timer_data)

    def update_display(self, blank=False):
        if blank:
            self.show_blank_timer()
        else:
            self.show_timer_data()
    
    def update_target(self, value):
        if self.edit_target is None:
            return
        
        self.edit_target.SetLabel("{:0>2d}".format(value))
        self.set_timer_data()

    def alarm_timer(self):
        self.timer.stop()
        # start count-up timer
        self.timer.clear()
        self.timer.start()

        print("Alarm!")

def main():
    app = MainApp(False)
    app.MainLoop()


if __name__ == '__main__':
    main()
