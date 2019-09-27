import os
import wx
from main_frame import DlgSettings
from timer_config import TimerConfig
from utils import TimerMode, TimerMgrMode

file_wildcard = "Wave Files (.wav)|*.wav|All Files|*.*"


class MyDlgSettings(DlgSettings):
    def __init__(self, parent, timer_config):
        DlgSettings.__init__(self, parent)
        self.m_chkCyclings = [self.m_chkCycling0, self.m_chkCycling1]
        self.m_spinHours = [self.m_spinHour0, self.m_spinHour1]
        self.m_spinMinutes = [self.m_spinMinute0, self.m_spinMinute1]
        self.m_spinSeconds = [self.m_spinSecond0, self.m_spinSecond1]

        self.cycling_pre_value = [self.m_chkCycling0.GetValue(),
                                  self.m_chkCycling1.GetValue()]
        self.timer_config = TimerConfig()
        self.timer_config.copy(timer_config)

    def m_btnSelSoundOnButtonClick(self, event):
        dlg = wx.FileDialog(self, "Open CFG file...",
                            defaultDir=os.getcwd(),
                            defaultFile="",
                            wildcard=file_wildcard,
                            style=wx.FD_OPEN |
                            wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST |
                            wx.FD_PREVIEW)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.m_staticSoundFile.SetLabel(self.filename)

        dlg.Destroy()
    
    def m_TimerMgrModeOnRadioBox(self, event):
        selection = self.m_TimerMgrMode.GetSelection()
        # disable cycling if alternation mode
        if selection == 1:  # Alernation mode
            self.cycling_pre_value = [self.m_chkCycling0.GetValue(),
                                      self.m_chkCycling1.GetValue()]
            self.m_chkCycling0.SetValue(False)
            self.m_chkCycling1.SetValue(False)
            self.m_chkCycling0.Enable(False)
            self.m_chkCycling1.Enable(False)
        else:
            self.m_chkCycling0.SetValue(self.cycling_pre_value[0])
            self.m_chkCycling1.SetValue(self.cycling_pre_value[1])
            self.m_chkCycling0.Enable(True)
            self.m_chkCycling1.Enable(True)

    def m_btnOKOnButtonClick(self, event):
        selection = self.m_TimerMgrMode.GetSelection()
        self.timer_config.timer_mgr_mode = TimerMgrMode(selection)
        for idx in [0,1]:
            self.timer_config.timer_data[idx].set(
                int(self.m_spinHours[idx].GetValue()),
                int(self.m_spinMinutes[idx].GetValue()),
                int(self.m_spinSeconds[idx].GetValue())
            )
            self.timer_config.timer_mode[idx] = \
                TimerMode.Cycling if self.m_chkCyclings[idx].IsChecked() \
                    else TimerMode.OneShot

        self.timer_config.timer_alarm_sound = self.m_chkAlarmSound.IsChecked()
        self.timer_config.timer_alarm_sound_file = \
            self.m_staticSoundFile.GetLabel()
        self.timer_config.timer_alarm_notification = \
            self.m_chkAlarmNotification.IsChecked()
        self.timer_config.timer_alarm_duration = self.m_spinDuration.GetValue()


def test():
    app = wx.App()
    app.MainLoop()
    dialog = MyDlgSettings(None, TimerConfig())
    result = dialog.ShowModal()
    if result == wx.ID_OK:
        print("Pressed OK")
    else:
        print("Pressed Cancel")
    dialog.Destroy()


if __name__ == '__main__':
    test()
