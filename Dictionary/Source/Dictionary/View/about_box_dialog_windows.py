__author__ = 'Zunayed Hassan'

import wx
from Model.about_box_info import *
import wx.lib.scrolledpanel as scrolled
from common_about_box_tool import *

class AboutBoxDialogWindows(wx.Dialog):
    def __init__(self, parent, id, title, aboutBoxInfo, appSettings):
        wx.Dialog.__init__(self, parent, id, title, size = wx.Size(430, 300))
        
        # CONTROL:    Panel (wx.Panel)
        # PARENT:     self
        panel = wx.Panel(
            parent = self,
            id     = wx.ID_ANY,
            size   = wx.Size(self.GetSize().width, self.GetSize().height)
        )
        
        # CONTROL:    notebook (wx.Notebook)
        notebook = wx.Notebook(
            parent = panel,
            id     = wx.ID_ANY,
            pos    = wx.Point(appSettings.BorderThickness, appSettings.BorderThickness),
            size   = wx.Size((self.GetSize().width - appSettings.BorderThickness * 4), (self.GetSize().height - 60))
        )

        # CONTROL:    VersionPanel
        # PARENT:     Notebook
        versionPage = VersionPanel(
            parent       = notebook,
            id           = wx.ID_ANY,
            aboutBoxInfo = aboutBoxInfo,
            appSettings  = appSettings
        )

        notebook.AddPage(versionPage, "Version")

        # CONTROL:    LicensePanel
        # PARENT:     Notebook
        licensePage = LicensePanel(
            parent       = notebook,
            id           = wx.ID_ANY,
            aboutBoxInfo = aboutBoxInfo,
            appSettings  = appSettings
        )

        notebook.AddPage(licensePage, "License")

        # CONTROL:    CreditsPanel
        # PARENT:     Notebook
        creditsPage = CreditsPanel(
            parent       = notebook,
            id           = wx.ID_ANY,
            aboutBoxInfo = aboutBoxInfo,
            appSettings  = appSettings
        )

        notebook.AddPage(creditsPage, "Credits")

        # CONTROL:    CloseButton (wx.Button)
        self._closeButton = wx.Button(
            parent = panel,
            id     = wx.ID_CLOSE,
            label  = "Close",
            pos    = wx.Point((self.GetSize().width)/2 - 40, self.GetSize().height - 55)
        )

        # EVENT
        # EVENT FOR: CloseButton
        self.Bind(
            event   = wx.EVT_BUTTON,
            handler = self.OnCloseButtonClicked,
            id      = self._closeButton.GetId()
        )
        
    # METHOD NAME:    OnCloseButtonClicked
    # PARAMETER:      Event
    # RETURN:         None
    # PURPOSE:        Close this dialog
    def OnCloseButtonClicked(self, event):
        self.Close()