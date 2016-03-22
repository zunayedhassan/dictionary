__author__ = 'Zunayed Hassan'

import wx

class ApplicationSettingsModel():
    def __init__(self):
        # Dictionary Application Settings
        self.IconLocation       = "Resources/Icons/"
        self.LibraryLocation    = "Resources/Library/"
        self.BorderThickness    = 3

        # Main Dictionary Window Settings
        self.MainWindowTitle     = u"Dictionary"
        self.MainWindowWidth     = 680
        self.MainWindowHeight    = 480

        # ToolTip Settings
        self.ToolTip_BackButton          = u"Previous word"
        self.ToolTip_NextButton          = u"Next word"
        self.ToolTip_ClickANdTypeButton  = u"Type Bengali word with mouse click"
        self.ToolTip_FontSettingsButton  = u"Change font settings"
        self.ToolTip_AboutButton         = u"About"

        # Static Text Settings
        self.StaticText_From     = u"From"
        self.StaticText_To       = u"To"

        # ComboBox Language Settings
        self.Language                  = [ u"English", u"বাংলা" ]

        self.CurrentlySelectedLanguage = [ 0, 0 ]   # Index 0 -> From ComboBox, Index 1 -> To ComboBox,
                                                    # 0 -> English, 1 -> বাংলা

        self.SplitterProportion  = 0.25
        
        # Other
        self.LastWordIndex            = None
