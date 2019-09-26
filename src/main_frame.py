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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 336,215 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerMain = wx.BoxSizer( wx.VERTICAL )

		bSizerIconBar = wx.BoxSizer( wx.HORIZONTAL )

		self.m_IconT1 = wx.StaticText( self, wx.ID_ANY, u"T1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_IconT1.Wrap( -1 )

		self.m_IconT1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizerIconBar.Add( self.m_IconT1, 0, wx.ALL, 5 )

		self.m_IconT2 = wx.StaticText( self, wx.ID_ANY, u"T2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_IconT2.Wrap( -1 )

		self.m_IconT2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizerIconBar.Add( self.m_IconT2, 0, wx.ALL, 5 )


		bSizerIconBar.Add( ( 0, 0), 3, wx.EXPAND, 5 )

		self.m_IconOverflow = wx.StaticText( self, wx.ID_ANY, u"Overflow", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_IconOverflow.Wrap( -1 )

		self.m_IconOverflow.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizerIconBar.Add( self.m_IconOverflow, 0, wx.ALL, 5 )

		self.m_IconAlarm = wx.StaticText( self, wx.ID_ANY, u"Alarm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_IconAlarm.Wrap( -1 )

		self.m_IconAlarm.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizerIconBar.Add( self.m_IconAlarm, 0, wx.ALL, 5 )


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
		self.m_IconT1.Bind( wx.EVT_LEFT_DCLICK, self.OnIconTnLeftDClick )
		self.m_IconT2.Bind( wx.EVT_LEFT_DCLICK, self.OnIconTnLeftDClick )
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
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Settings", pos = wx.DefaultPosition, size = wx.Size( 292,212 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerDlgMain = wx.BoxSizer( wx.VERTICAL )

		sbSizerTimer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Timer1" ), wx.HORIZONTAL )

		self.m_spinHour1 = wx.SpinCtrl( sbSizerTimer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 99, 0 )
		sbSizerTimer1.Add( self.m_spinHour1, 0, wx.ALL, 5 )

		self.m_staticColon11 = wx.StaticText( sbSizerTimer1.GetStaticBox(), wx.ID_ANY, u"：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticColon11.Wrap( -1 )

		sbSizerTimer1.Add( self.m_staticColon11, 0, wx.ALL, 5 )

		self.m_spinMinute1 = wx.SpinCtrl( sbSizerTimer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 59, 0 )
		sbSizerTimer1.Add( self.m_spinMinute1, 0, wx.ALL, 5 )

		self.m_staticColon12 = wx.StaticText( sbSizerTimer1.GetStaticBox(), wx.ID_ANY, u"：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticColon12.Wrap( -1 )

		sbSizerTimer1.Add( self.m_staticColon12, 0, wx.ALL, 5 )

		self.m_spinSecond1 = wx.SpinCtrl( sbSizerTimer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 59, 0 )
		sbSizerTimer1.Add( self.m_spinSecond1, 0, wx.ALL, 5 )


		bSizerDlgMain.Add( sbSizerTimer1, 1, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Timer2" ), wx.HORIZONTAL )

		self.m_spinHour2 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 99, 0 )
		sbSizer2.Add( self.m_spinHour2, 0, wx.ALL, 5 )

		self.m_staticColon21 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticColon21.Wrap( -1 )

		sbSizer2.Add( self.m_staticColon21, 0, wx.ALL, 5 )

		self.m_spinMinute2 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 59, 0 )
		sbSizer2.Add( self.m_spinMinute2, 0, wx.ALL, 5 )

		self.m_staticColon22 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticColon22.Wrap( -1 )

		sbSizer2.Add( self.m_staticColon22, 0, wx.ALL, 5 )

		self.m_spinSecond2 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 59, 0 )
		sbSizer2.Add( self.m_spinSecond2, 0, wx.ALL, 5 )


		bSizerDlgMain.Add( sbSizer2, 1, wx.EXPAND, 5 )

		bSizerButton = wx.BoxSizer( wx.HORIZONTAL )


		bSizerButton.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_btnOK = wx.Button( self, wx.ID_OK, u"&OK", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_btnOK.SetDefault()
		bSizerButton.Add( self.m_btnOK, 0, wx.ALL, 5 )

		self.m_btnCancel = wx.Button( self, wx.ID_CANCEL, u"&Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerButton.Add( self.m_btnCancel, 0, wx.ALL, 5 )


		bSizerButton.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizerDlgMain.Add( bSizerButton, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerDlgMain )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


