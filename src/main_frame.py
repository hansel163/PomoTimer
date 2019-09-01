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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 339,189 ), style = 0|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerMain = wx.BoxSizer( wx.VERTICAL )

		bSizerIconBar = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticT1Icon = wx.StaticText( self, wx.ID_ANY, u"T1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticT1Icon.Wrap( -1 )

		self.m_staticT1Icon.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizerIconBar.Add( self.m_staticT1Icon, 0, wx.ALL, 5 )

		self.m_staticT2Icon = wx.StaticText( self, wx.ID_ANY, u"T2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticT2Icon.Wrap( -1 )

		self.m_staticT2Icon.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizerIconBar.Add( self.m_staticT2Icon, 0, wx.ALL, 5 )

		self.m_staticTextSpace = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSpace.Wrap( -1 )

		bSizerIconBar.Add( self.m_staticTextSpace, 9, wx.ALL, 5 )

		self.m_btnExit = wx.Button( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizerIconBar.Add( self.m_btnExit, 1, wx.ALL, 5 )


		bSizerMain.Add( bSizerIconBar, 1, wx.EXPAND, 5 )

		self.m_panelTimer = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panelTimer.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizerTimer = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8 = wx.StaticText( self.m_panelTimer, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizerTimer.Add( self.m_staticText8, 3, wx.ALL, 5 )

		self.m_staticTimer = wx.StaticText( self.m_panelTimer, wx.ID_ANY, u"00:00:00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTimer.Wrap( -1 )

		self.m_staticTimer.SetFont( wx.Font( 36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizerTimer.Add( self.m_staticTimer, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panelTimer, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizerTimer.Add( self.m_staticText9, 3, wx.ALL, 5 )


		self.m_panelTimer.SetSizer( bSizerTimer )
		self.m_panelTimer.Layout()
		bSizerTimer.Fit( self.m_panelTimer )
		bSizerMain.Add( self.m_panelTimer, 9, wx.EXPAND |wx.ALL, 5 )

		bSizerButtons = wx.BoxSizer( wx.HORIZONTAL )

		self.m_btnStart = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_btnStart.SetDefault()
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

	def __del__( self ):
		pass


