__author__ = 'Zunayed Hassan'

import wx
from Model.about_box_info import *
from common_about_box_tool import *

class AboutBoxDialog(wx.Dialog):
    def __init__(self, parent, id, title, aboutBoxInfo, appSettings):
        wx.Dialog.__init__(self, parent, id, title, size = wx.Size(430, 300))
        
        # CONTROL:    Panel (wx.Panel)
        # PARENT:     self
        # LAYOUT:     Box Sizer Layout (Vertical)
        panel = wx.Panel(
            parent = self,
            id     = wx.ID_ANY
        )
        
        panelVBoxSizer = wx.BoxSizer(orient = wx.VERTICAL)
        panel.SetSizer(sizer = panelVBoxSizer)
        
        # CONTROL:    notebook (wx.Notebook)
        notebook = wx.Notebook(
            parent = panel,
            id     = wx.ID_ANY
        )
        
        panelVBoxSizer.Add(
            item       = notebook,
            proportion = 1,
            flag       = wx.ALL | wx.EXPAND,
            border     = appSettings.BorderThickness * 2
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
            label  = "Close"
        )
        
        panelVBoxSizer.Add(
            item        = self._closeButton,
            proportion  = 0,
            flag        = wx.LEFT | wx.BOTTOM | wx.RIGHT | wx.CENTER,
            border      = appSettings.BorderThickness * 2
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
    
    