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
from main_frame import MainFrame, DlgSettings, TimerEditBox
from pomo_timer import *
from events import *


TIMER_EDIT_BOX_EXPAND_X = 30
TIMER_EDIT_BOX_EXPAND_Y = 5

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


class MyTimerEditBox(TimerEditBox):
    def __init__(self, parent):
        TimerEditBox.__init__(self, parent)

    def m_spinEditOnSpinCtrl(self, event):
        pass


class MyDlgSettings(DlgSettings):
    def __init__(self, parent):
        DlgSettings.__init__(self, parent)


# Implementing MainFrame
class MyMainFrame(MainFrame):
    def __init__(self, parent):
        MainFrame.__init__(self, parent)

        # Init values
        self.edit_box = MyTimerEditBox(self)
        self.edit_box.Hide()

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

    def show_spin_ctrl_edit(self, target, value, max):
        
        # get target position in screen coordinations
        position = self.m_panelTimer.ClientToScreen(target.Position)
        # convert to MainFrame client coordinations
        real_position = self.ScreenToClient(position)

        size = wx.Size(target.Size.Width + TIMER_EDIT_BOX_EXPAND_X,
                       target.Size.Height + TIMER_EDIT_BOX_EXPAND_Y)

        self.edit_box.m_spinEdit.SetMax(max)
        self.edit_box.m_spinEdit.SetValue(value)
        self.edit_box.SetPosition(real_position)
        self.edit_box.SetSize(size)
        self.edit_box.Show()

    # Override event handler of double Click on timer display
    def m_staticHourOnLeftDClick(self, event):
        self.show_spin_ctrl_edit(
            self.m_staticHour, self.timer.running_timer_data.hour, (MAX_HOUR - 1))

    def m_staticMinuteOnLeftDClick(self, event):
        self.m_spinEdit.SetMax(MAX_MIN_SEC - 1)
        self.m_spinEdit.SetValue(self.timer.running_timer_data.minute)

    def m_staticSecondOnLeftDClick(self, event):
        self.m_spinEdit.SetMax(MAX_MIN_SEC - 1)
        self.m_spinEdit.SetValue(self.timer.running_timer_data.second)

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

    def show_blank_timer(self):
        self.m_staticHour.SetLabel("")
        self.m_staticMinute.SetLabel("")
        self.m_staticSecond.SetLabel("")

    def show_timer_data(self):
        timer_data = self.timer.running_timer_data

        self.m_staticHour.SetLabel("{:0>2d}".format(timer_data.hour))
        self.m_staticMinute.SetLabel("{:0>2d}".format(timer_data.minute))
        self.m_staticSecond.SetLabel("{:0>2d}".format(timer_data.second))

    def update_display(self, blank=False):
        if blank:
            self.show_blank_timer()
        else:
            self.show_timer_data()
    
    def alarm_timer(self):
        pass

def main():
    app = MainApp(False)
    app.MainLoop()


if __name__ == '__main__':
    main()
