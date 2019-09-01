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
from main_frame import MainFrame
from pomo_timer import PomoTimer, TimerData, TimerState
from events import *


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

   
# Implementing MainFrame
class MyMainFrame(MainFrame):
    def __init__(self, parent):
        MainFrame.__init__(self, parent)

        # Init values
        # Connect Events
        self.m_btnExit.Bind(wx.EVT_BUTTON, self.OnExit)
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

    def OnExit(self, event):
        self.timer.exit()
        self.Close()

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
        pass

    def update_display(self, timer):
        self.m_staticTimer.SetLabel(timer)
    
    def alarm_timer(self):
        pass

def main():
    app = MainApp(False)
    app.MainLoop()


if __name__ == '__main__':
    main()
