__author__ = 'Zunayed Hassan'

import wx, os, tempfile, pickle
from dictionary_window_view import *
from ViewModel.app_view_model import *

class DictionaryApplication(wx.App):
    _appSettings = None

    def OnInit(self):
        # 1. Check if 'dictionary_config.cfg' file exist or not.
        # 2. If 'dictionary_config.cfg' file doesn't exist, then create a new file
        # 3. Then load settings 
        if (not FileSettings.DictionaryConfigurationFile):
            SaveOrCreateApplicationSettingsFile()

        DictionaryWindowView.AppSettings = self._appSettings = LoadApplicationSettings()
        
        # Load dictionary window
        DictionaryWindow = DictionaryWindowView(
            parent = None,
            id     = wx.ID_ANY,
            title  = self._appSettings.MainWindowTitle
        )

        DictionaryWindow.SetIcon(
            icon = wx.Icon(
                name = self._appSettings.IconLocation + "icon.ico",
                type = wx.BITMAP_TYPE_ICO
            )
        )

        DictionaryWindow.Show(True)

        return True