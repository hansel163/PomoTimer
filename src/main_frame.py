# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 355,228 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerMain = wx.BoxSizer( wx.VERTICAL )

		bSizerIconBar = wx.BoxSizer( wx.HORIZONTAL )

		self.m_IconT0 = wx.StaticText( self, wx.ID_ANY, u"T0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_IconT0.Wrap( -1 )

		self.m_IconT0.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizerIconBar.Add( self.m_IconT0, 0, wx.ALL, 5 )

		self.m_IconT1 = wx.StaticText( self, wx.ID_ANY, u"T1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_IconT1.Wrap( -1 )

		self.m_IconT1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizerIconBar.Add( self.m_IconT1, 0, wx.ALL, 5 )


		bSizerIconBar.Add( ( 0, 0), 3, wx.EXPAND, 5 )

		self.m_IconOverflow = wx.StaticText( self, wx.ID_ANY, u"Overflow", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_IconOverflow.Wrap( -1 )

		self.m_IconOverflow.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizerIconBar.Add( self.m_IconOverflow, 0, wx.ALL, 5 )

		self.m_IconAlarm = wx.StaticText( self, wx.ID_ANY, u"Alarm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_IconAlarm.Wrap( -1 )

		self.m_IconAlarm.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizerIconBar.Add( self.m_IconAlarm, 0, wx.ALL, 5 )

		self.m_IconMode = wx.StaticText( self, wx.ID_ANY, u"Alt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_IconMode.Wrap( -1 )

		self.m_IconMode.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizerIconBar.Add( self.m_IconMode, 0, wx.ALL, 5 )


		bSizerMain.Add( bSizerIconBar, 1, wx.EXPAND, 5 )

		self.m_panelTimer = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panelTimer.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		self.bSizerTimer = wx.BoxSizer( wx.HORIZONTAL )


		self.bSizerTimer.Add( ( 0, 0), 3, wx.EXPAND, 5 )

		self.m_spinEditHour = wx.SpinCtrl( self.m_panelTimer, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS|wx.SP_WRAP|wx.TE_PROCESS_ENTER, 0, 59, 10 )
		self.m_spinEditHour.SetFont( wx.Font( 36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_spinEditHour.Hide()

		self.bSizerTimer.Add( self.m_spinEditHour, 0, wx.ALL, 5 )

		self.m_staticHour = wx.StaticText( self.m_panelTimer, wx.ID_ANY, u"00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticHour.Wrap( -1 )

		self.m_staticHour.SetFont( wx.Font( 36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		self.bSizerTimer.Add( self.m_staticHour, 0, wx.ALL, 5 )

		self.m_staticTimerColon1 = wx.StaticText( self.m_panelTimer, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTimerColon1.Wrap( -1 )

		self.m_staticTimerColon1.SetFont( wx.Font( 36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		self.bSizerTimer.Add( self.m_staticTimerColon1, 0, wx.ALL, 5 )

		self.m_spinEditMinute = wx.SpinCtrl( self.m_panelTimer, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS|wx.SP_WRAP|wx.TE_PROCESS_ENTER, 0, 59, 10 )
		self.m_spinEditMinute.SetFont( wx.Font( 36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_spinEditMinute.Hide()

		self.bSizerTimer.Add( self.m_spinEditMinute, 0, wx.ALL, 5 )

		self.m_staticMinute = wx.StaticText( self.m_panelTimer, wx.ID_ANY, u"00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticMinute.Wrap( -1 )

		self.m_staticMinute.SetFont( wx.Font( 36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		self.bSizerTimer.Add( self.m_staticMinute, 0, wx.ALL, 5 )

		self.m_staticTimerColon2 = wx.StaticText( self.m_panelTimer, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTimerColon2.Wrap( -1 )

		self.m_staticTimerColon2.SetFont( wx.Font( 36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		self.bSizerTimer.Add( self.m_staticTimerColon2, 0, wx.ALL, 5 )

		self.m_spinEditSecond = wx.SpinCtrl( self.m_panelTimer, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS|wx.SP_WRAP|wx.TE_PROCESS_ENTER, 0, 59, 10 )
		self.m_spinEditSecond.SetFont( wx.Font( 36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_spinEditSecond.Hide()

		self.bSizerTimer.Add( self.m_spinEditSecond, 0, wx.ALL, 5 )

		self.m_staticSecond = wx.StaticText( self.m_panelTimer, wx.ID_ANY, u"00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticSecond.Wrap( -1 )

		self.m_staticSecond.SetFont( wx.Font( 36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		self.bSizerTimer.Add( self.m_staticSecond, 0, wx.ALL, 5 )


		self.bSizerTimer.Add( ( 0, 0), 3, wx.EXPAND, 5 )


		self.m_panelTimer.SetSizer( self.bSizerTimer )
		self.m_panelTimer.Layout()
		self.bSizerTimer.Fit( self.m_panelTimer )
		bSizerMain.Add( self.m_panelTimer, 9, wx.EXPAND |wx.ALL, 5 )

		bSizerButtons = wx.BoxSizer( wx.HORIZONTAL )

		self.m_btnStart = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_btnStart.SetBitmap( wx.Bitmap( u"res/Start-icon-64.png", wx.BITMAP_TYPE_ANY ) )
		bSizerButtons.Add( self.m_btnStart, 0, wx.ALL, 5 )

		self.m_btnStop = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_btnStop.SetBitmap( wx.Bitmap( u"res/Stop-icon-64.png", wx.BITMAP_TYPE_ANY ) )
		bSizerButtons.Add( self.m_btnStop, 0, wx.ALL, 5 )

		self.m_btnClear = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_btnClear.SetBitmap( wx.Bitmap( u"res/Clear-icon-64.png", wx.BITMAP_TYPE_ANY ) )
		bSizerButtons.Add( self.m_btnClear, 0, wx.ALL, 5 )

		self.m_btnSet = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_btnSet.SetBitmap( wx.Bitmap( u"res/Settings-icon-64.png", wx.BITMAP_TYPE_ANY ) )
		bSizerButtons.Add( self.m_btnSet, 0, wx.ALL, 5 )


		bSizerMain.Add( bSizerButtons, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerMain )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_IconT0.Bind( wx.EVT_LEFT_DCLICK, self.OnIconTnLeftDClick )
		self.m_IconT1.Bind( wx.EVT_LEFT_DCLICK, self.OnIconTnLeftDClick )
		self.m_spinEditHour.Bind( wx.EVT_KILL_FOCUS, self.OnExitEdit )
		self.m_spinEditHour.Bind( wx.EVT_SPINCTRL, self.m_spinEditOnSpinCtrl )
		self.m_spinEditHour.Bind( wx.EVT_TEXT_ENTER, self.OnExitEdit )
		self.m_staticHour.Bind( wx.EVT_LEFT_DCLICK, self.m_staticHourOnLeftDClick )
		self.m_spinEditMinute.Bind( wx.EVT_KILL_FOCUS, self.OnExitEdit )
		self.m_spinEditMinute.Bind( wx.EVT_SPINCTRL, self.m_spinEditOnSpinCtrl )
		self.m_spinEditMinute.Bind( wx.EVT_TEXT_ENTER, self.OnExitEdit )
		self.m_staticMinute.Bind( wx.EVT_LEFT_DCLICK, self.m_staticMinuteOnLeftDClick )
		self.m_spinEditSecond.Bind( wx.EVT_KILL_FOCUS, self.OnExitEdit )
		self.m_spinEditSecond.Bind( wx.EVT_SPINCTRL, self.m_spinEditOnSpinCtrl )
		self.m_spinEditSecond.Bind( wx.EVT_TEXT_ENTER, self.OnExitEdit )
		self.m_staticSecond.Bind( wx.EVT_LEFT_DCLICK, self.m_staticSecondOnLeftDClick )
		self.m_btnStart.Bind( wx.EVT_BUTTON, self.OnStart )
		self.m_btnStop.Bind( wx.EVT_BUTTON, self.OnStop )
		self.m_btnClear.Bind( wx.EVT_BUTTON, self.OnClear )
		self.m_btnSet.Bind( wx.EVT_BUTTON, self.OnSet )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnIconTnLeftDClick( self, event ):
		event.Skip()


	def OnExitEdit( self, event ):
		event.Skip()

	def m_spinEditOnSpinCtrl( self, event ):
		event.Skip()


	def m_staticHourOnLeftDClick( self, event ):
		event.Skip()




	def m_staticMinuteOnLeftDClick( self, event ):
		event.Skip()




	def m_staticSecondOnLeftDClick( self, event ):
		event.Skip()

	def OnStart( self, event ):
		event.Skip()

	def OnStop( self, event ):
		event.Skip()

	def OnClear( self, event ):
		event.Skip()

	def OnSet( self, event ):
		event.Skip()


###########################################################################
## Class DlgSettings
###########################################################################

class DlgSettings ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Settings", pos = wx.DefaultPosition, size = wx.Size( 494,549 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerDlgMain = wx.BoxSizer( wx.VERTICAL )

		m_TimerMgrModeChoices = [ u"Standalone", u"Alternation" ]
		self.m_TimerMgrMode = wx.RadioBox( self, wx.ID_ANY, u"Mode", wx.DefaultPosition, wx.DefaultSize, m_TimerMgrModeChoices, 1, wx.RA_SPECIFY_ROWS )
		self.m_TimerMgrMode.SetSelection( 0 )
		bSizerDlgMain.Add( self.m_TimerMgrMode, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizerTimer0 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Timer0" ), wx.VERTICAL )

		bSizerTimerName0 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticTimerName0 = wx.StaticText( sbSizerTimer0.GetStaticBox(), wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTimerName0.Wrap( -1 )

		bSizerTimerName0.Add( self.m_staticTimerName0, 0, wx.ALL, 5 )

		self.m_textTimerName0 = wx.TextCtrl( sbSizerTimer0.GetStaticBox(), wx.ID_ANY, u"Working", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textTimerName0.SetMaxLength( 128 )
		bSizerTimerName0.Add( self.m_textTimerName0, 1, wx.ALL, 5 )


		sbSizerTimer0.Add( bSizerTimerName0, 1, wx.EXPAND, 5 )

		bSizerTimerData0 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_spinHour0 = wx.SpinCtrl( sbSizerTimer0.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, 0, 99, 0 )
		bSizerTimerData0.Add( self.m_spinHour0, 0, wx.ALL, 5 )

		self.m_staticColon01 = wx.StaticText( sbSizerTimer0.GetStaticBox(), wx.ID_ANY, u"：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticColon01.Wrap( -1 )

		bSizerTimerData0.Add( self.m_staticColon01, 0, wx.ALL, 5 )

		self.m_spinMinute0 = wx.SpinCtrl( sbSizerTimer0.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, 0, 59, 0 )
		bSizerTimerData0.Add( self.m_spinMinute0, 0, wx.ALL, 5 )

		self.m_staticColon02 = wx.StaticText( sbSizerTimer0.GetStaticBox(), wx.ID_ANY, u"：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticColon02.Wrap( -1 )

		bSizerTimerData0.Add( self.m_staticColon02, 0, wx.ALL, 5 )

		self.m_spinSecond0 = wx.SpinCtrl( sbSizerTimer0.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, 0, 59, 0 )
		bSizerTimerData0.Add( self.m_spinSecond0, 0, wx.ALL, 5 )

		self.m_chkCycling0 = wx.CheckBox( sbSizerTimer0.GetStaticBox(), wx.ID_ANY, u"Cycling", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerTimerData0.Add( self.m_chkCycling0, 0, wx.ALL, 5 )


		sbSizerTimer0.Add( bSizerTimerData0, 1, wx.EXPAND, 5 )


		bSizerDlgMain.Add( sbSizerTimer0, 1, wx.EXPAND, 5 )

		sbSizerTimer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Timer1" ), wx.VERTICAL )

		bSizerTimerName1 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticTimerName1 = wx.StaticText( sbSizerTimer1.GetStaticBox(), wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTimerName1.Wrap( -1 )

		bSizerTimerName1.Add( self.m_staticTimerName1, 0, wx.ALL, 5 )

		self.m_textTimerName1 = wx.TextCtrl( sbSizerTimer1.GetStaticBox(), wx.ID_ANY, u"Break", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textTimerName1.SetMaxLength( 128 )
		bSizerTimerName1.Add( self.m_textTimerName1, 1, wx.ALL, 5 )


		sbSizerTimer1.Add( bSizerTimerName1, 1, wx.EXPAND, 5 )

		bSizerTimerData1 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_spinHour1 = wx.SpinCtrl( sbSizerTimer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, 0, 99, 0 )
		bSizerTimerData1.Add( self.m_spinHour1, 0, wx.ALL, 5 )

		self.m_staticColon11 = wx.StaticText( sbSizerTimer1.GetStaticBox(), wx.ID_ANY, u"：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticColon11.Wrap( -1 )

		bSizerTimerData1.Add( self.m_staticColon11, 0, wx.ALL, 5 )

		self.m_spinMinute1 = wx.SpinCtrl( sbSizerTimer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, 0, 59, 0 )
		bSizerTimerData1.Add( self.m_spinMinute1, 0, wx.ALL, 5 )

		self.m_staticColon12 = wx.StaticText( sbSizerTimer1.GetStaticBox(), wx.ID_ANY, u"：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticColon12.Wrap( -1 )

		bSizerTimerData1.Add( self.m_staticColon12, 0, wx.ALL, 5 )

		self.m_spinSecond1 = wx.SpinCtrl( sbSizerTimer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, 0, 59, 0 )
		bSizerTimerData1.Add( self.m_spinSecond1, 0, wx.ALL, 5 )

		self.m_chkCycling1 = wx.CheckBox( sbSizerTimer1.GetStaticBox(), wx.ID_ANY, u"Cycling", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerTimerData1.Add( self.m_chkCycling1, 0, wx.ALL, 5 )


		sbSizerTimer1.Add( bSizerTimerData1, 1, wx.EXPAND, 5 )


		bSizerDlgMain.Add( sbSizerTimer1, 1, wx.EXPAND, 5 )

		sbSizerAlarm = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Alarm" ), wx.VERTICAL )

		bSizerSound = wx.BoxSizer( wx.HORIZONTAL )

		self.m_chkAlarmSound = wx.CheckBox( sbSizerAlarm.GetStaticBox(), wx.ID_ANY, u"Sound:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_chkAlarmSound.SetValue(True)
		bSizerSound.Add( self.m_chkAlarmSound, 0, wx.ALL, 5 )

		self.m_staticSoundFile = wx.StaticText( sbSizerAlarm.GetStaticBox(), wx.ID_ANY, u"Sound File Path", wx.DefaultPosition, wx.DefaultSize, wx.ST_ELLIPSIZE_MIDDLE )
		self.m_staticSoundFile.Wrap( -1 )

		bSizerSound.Add( self.m_staticSoundFile, 2, wx.ALL, 5 )

		self.m_btnSelSound = wx.Button( sbSizerAlarm.GetStaticBox(), wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( 25,25 ), wx.BU_BOTTOM )
		bSizerSound.Add( self.m_btnSelSound, 0, wx.ALL, 5 )


		sbSizerAlarm.Add( bSizerSound, 1, wx.EXPAND, 5 )

		self.m_chkAlarmNotification = wx.CheckBox( sbSizerAlarm.GetStaticBox(), wx.ID_ANY, u"Notification", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_chkAlarmNotification.SetValue(True)
		sbSizerAlarm.Add( self.m_chkAlarmNotification, 0, wx.ALL, 5 )

		self.m_chkAlarmBlinkIcon = wx.CheckBox( sbSizerAlarm.GetStaticBox(), wx.ID_ANY, u"Blink Taskbar Icon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_chkAlarmBlinkIcon.SetValue(True)
		sbSizerAlarm.Add( self.m_chkAlarmBlinkIcon, 0, wx.ALL, 5 )

		bSizerDuration = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticDuration = wx.StaticText( sbSizerAlarm.GetStaticBox(), wx.ID_ANY, u"Duration:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticDuration.Wrap( -1 )

		bSizerDuration.Add( self.m_staticDuration, 0, wx.ALL, 5 )

		self.m_spinDuration = wx.SpinCtrl( sbSizerAlarm.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, 1, 60, 8 )
		bSizerDuration.Add( self.m_spinDuration, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( sbSizerAlarm.GetStaticBox(), wx.ID_ANY, u"Second(s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizerDuration.Add( self.m_staticText21, 0, wx.ALL, 5 )


		sbSizerAlarm.Add( bSizerDuration, 1, wx.EXPAND, 5 )


		bSizerDlgMain.Add( sbSizerAlarm, 1, wx.EXPAND, 5 )

		bSizerButton = wx.BoxSizer( wx.HORIZONTAL )


		bSizerButton.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_btnOK = wx.Button( self, wx.ID_OK, u"&OK", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_btnOK.SetDefault()
		bSizerButton.Add( self.m_btnOK, 0, wx.ALL, 5 )

		self.m_btnReset = wx.Button( self, wx.ID_ANY, u"&Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerButton.Add( self.m_btnReset, 0, wx.ALL, 5 )

		self.m_btnCancel = wx.Button( self, wx.ID_CANCEL, u"&Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerButton.Add( self.m_btnCancel, 0, wx.ALL, 5 )


		bSizerButton.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizerDlgMain.Add( bSizerButton, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerDlgMain )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_TimerMgrMode.Bind( wx.EVT_RADIOBOX, self.m_TimerMgrModeOnRadioBox )
		self.m_btnSelSound.Bind( wx.EVT_BUTTON, self.m_btnSelSoundOnButtonClick )
		self.m_btnOK.Bind( wx.EVT_BUTTON, self.m_btnOKOnButtonClick )
		self.m_btnReset.Bind( wx.EVT_BUTTON, self.m_btnResetOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_TimerMgrModeOnRadioBox( self, event ):
		event.Skip()

	def m_btnSelSoundOnButtonClick( self, event ):
		event.Skip()

	def m_btnOKOnButtonClick( self, event ):
		event.Skip()

	def m_btnResetOnButtonClick( self, event ):
		event.Skip()


