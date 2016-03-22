__author__ = 'Zunayed Hassan'

import wx, sys
import wx.richtext as rt
from Model.app_settings_model import *
from Model.file_settings import *
from Model.library import *
from Model.word_search_history import *
from ViewModel.app_view_model import *
from ViewModel.dictionary_window_view_model import *
from proportional_splitter import *
from bengali_keyboard_frame import *
from about_box_dialog import *
from about_box_dialog_windows import * 
from Model.about_box_info import *


class DictionaryWindowView(wx.Frame):
    AppSettings = ApplicationSettingsModel()
    _wordSearchIndex  = None

    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(self.AppSettings.MainWindowWidth, self.AppSettings.MainWindowHeight))

        # CONTROL:  Main Panel (Panel),
        # PARENT:   DictionaryWindowView (wx.Frame)
        # LAYOUT:   Box Sizer (Vertical)
        mainPanel = wx.Panel(
            parent  = self,
            id      = wx.ID_ANY,
        )

        mainPanelVBoxSizer = wx.BoxSizer(orient = wx.VERTICAL)
        mainPanel.SetSizer(sizer = mainPanelVBoxSizer)

        # CONTROL:  Toolbar Panel (wx.Panel)
        # PARENT:   Main Panel (wx.Panel)
        # LAYOUT:   Box Sizer (Horizontal)
        toolBarPanel = wx.Panel(
            parent  = mainPanel,
            id      = wx.ID_ANY
        )

        mainPanelVBoxSizer.Add(
            item        = toolBarPanel,
            proportion  = 0,
            flag        = wx.EXPAND | wx.LEFT | wx.TOP | wx.RIGHT | wx.BOTTOM,
            border      = self.AppSettings.BorderThickness * 2
        )

        toolBarPanelHBoxSizer = wx.BoxSizer(orient = wx.HORIZONTAL)
        toolBarPanel.SetSizer(sizer = toolBarPanelHBoxSizer)

        # CONTROL:  Back Button (wx.BitmapButton)
        # PARENT:   Toolbar Panel (wx.Panel)
        # PURPOSE:  To show previous word that, user looked up before
        self._backButton = wx.BitmapButton(
            parent  = toolBarPanel,
            id      = wx.ID_ANY,
            bitmap  = wx.Bitmap(name = self.AppSettings.IconLocation + "go-previous.png")
        )

        self._backButton.SetToolTip(tip = wx.ToolTip(
            tip = self.AppSettings.ToolTip_BackButton)
        )

        toolBarPanelHBoxSizer.Add(
            item        = self._backButton,
            proportion  = 0,
            flag        = wx.LEFT
        )

        # CONTROL:  Next Button (wx.BitmapButton)
        # PARENT:   Toolbar Panel (wx.Panel)
        # PURPOSE:  To show next word that, user searched already
        self._nextButton = wx.BitmapButton(
            parent  = toolBarPanel,
            id      = wx.ID_ANY,
            bitmap  = wx.Bitmap(name = self.AppSettings.IconLocation + "go-next.png")
        )

        self._nextButton.SetToolTip(tip = wx.ToolTip(
            tip = self.AppSettings.ToolTip_NextButton)
        )

        toolBarPanelHBoxSizer.Add(
            item        = self._nextButton,
            proportion  = 0,
            flag        = wx.LEFT
        )

        # CONTROL:  From Static Text (wx.TextCtrl)
        # PARENT:   Toolbar Panel (wx.Panel)
        fromStaticText = wx.StaticText(
            parent = toolBarPanel,
            id     = wx.ID_ANY,
            label  = self.AppSettings.StaticText_From
        )

        toolBarPanelHBoxSizer.Add(
            item       = fromStaticText,
            proportion = 0,
            flag       = wx.LEFT | wx.CENTER,
            border     = self.AppSettings.BorderThickness * 3
        )

        # CONTROL:  From Language ComboBox (wx.ComboBox)
        # PARENT:   ToolBar Panel (wx.Panel)
        # PURPOSE:  To select a language for searching word
        self._fromComboBox = wx.ComboBox(
            parent   = toolBarPanel,
            id       = wx.ID_ANY,
            value    = self.AppSettings.Language[self.AppSettings.CurrentlySelectedLanguage[0]],
            choices  = self.AppSettings.Language,
            style    = wx.CB_READONLY
        )

        toolBarPanelHBoxSizer.Add(
            item       = self._fromComboBox,
            proportion = 0,
            flag       = wx.LEFT | wx.CENTER,
            border     = self.AppSettings.BorderThickness
        )

        # CONTROL:  To Static Text (wx.TextCtrl)
        # PARENT:   Toolbar Panel (wx.Panel)
        toStaticText = wx.StaticText(
            parent = toolBarPanel,
            id     = wx.ID_ANY,
            label  = self.AppSettings.StaticText_To
        )

        toolBarPanelHBoxSizer.Add(
            item       = toStaticText,
            proportion = 0,
            flag       = wx.LEFT | wx.CENTER,
            border     = self.AppSettings.BorderThickness * 2
        )

        # CONTROL:  From Language ComboBox (wx.ComboBox)
        # PARENT:   ToolBar Panel (wx.Panel)
        # PURPOSE:  To select a language for getting the meaning of word
        self._toComboBox = wx.ComboBox(
            parent   = toolBarPanel,
            id       = wx.ID_ANY,
            value    = self.AppSettings.Language[self.AppSettings.CurrentlySelectedLanguage[1]],
            choices  = self.AppSettings.Language,
            style    = wx.CB_READONLY
        )

        toolBarPanelHBoxSizer.Add(
            item       = self._toComboBox,
            proportion = 0,
            flag       = wx.LEFT | wx.CENTER,
            border     = self.AppSettings.BorderThickness
        )

        # CONTROL:  Click and Type Button (wx.BitmapButton)
        # PARENT:   Toolbar Panel (wx.Panel)
        # PURPOSE:  To type bengali word by mouse click
        self._clickAndTypeButton = wx.BitmapButton(
            parent  = toolBarPanel,
            id      = wx.ID_ANY,
            bitmap  = wx.Bitmap(name = self.AppSettings.IconLocation + "keyboard.png")
        )

        self._clickAndTypeButton.SetToolTip(tip = wx.ToolTip(
            tip = self.AppSettings.ToolTip_ClickANdTypeButton)
        )

        toolBarPanelHBoxSizer.Add(
            item       = self._clickAndTypeButton,
            proportion = 0,
            flag       = wx.LEFT,
            border     = self.AppSettings.BorderThickness * 3
        )

        # CONTROL:  About Button (wx.BitmapButton)
        # PARENT:   Toolbar Panel (wx.Panel)
        # PURPOSE:  To show Application Version, License and Credits
        self._aboutButton = wx.BitmapButton(
            parent  = toolBarPanel,
            id      = wx.ID_ANY,
            bitmap  = wx.Bitmap(name = self.AppSettings.IconLocation + "help-about.png")
        )

        self._aboutButton.SetToolTip(tip = wx.ToolTip(
            tip = self.AppSettings.ToolTip_AboutButton)
        )

        toolBarPanelHBoxSizer.Add(
            item       = self._aboutButton,
            proportion = 0,
            flag       = wx.LEFT
        )

        # CONTROL: Main Body Splitter (Proportional Splitter)
        # LAYOUT:  Vertical
        self._mainBodySplitter = ProportionalSplitter(
            parent      = mainPanel,
            id          = wx.ID_ANY,
            proportion  = self.AppSettings.SplitterProportion
        )

        mainPanelVBoxSizer.Add(
            item        = self._mainBodySplitter,
            proportion  = 1,
            flag        = wx.EXPAND | wx.LEFT | wx.TOP | wx.RIGHT | wx.BOTTOM,
            border      = self.AppSettings.BorderThickness * 2
        )

        # CONTROL:  Word List Panel (wx.Panel)
        # PARENT:   Main Body Splitter (Proportional Splitter)
        # LAYOUT:   Box Layout (Vertical)
        wordListPanel = wx.Panel(
            parent  = self._mainBodySplitter,
            id      = wx.ID_ANY
        )

        wordListPanelVBoxSizer = wx.BoxSizer(orient = wx.VERTICAL)
        wordListPanel.SetSizer(sizer = wordListPanelVBoxSizer)

        # CONTROL:  Word Meaning Rich TextCtrl (wx.richtext.RichTextCtrl)
        # PARENT:   Main Body Splitter (ProportionalSplitter)
        # PURPOSE:  To show word meaning that was searched
        self._wordMeaningRichTextCtrl = rt.RichTextCtrl(
            parent = self._mainBodySplitter,
            id     = wx.ID_ANY
        )
        
        self._wordMeaningRichTextCtrl.SetEditable(editable = False)

        self._mainBodySplitter.SplitVertically(
            win1 = wordListPanel,
            win2 = self._wordMeaningRichTextCtrl
        )

        # CONTROL:  Word Search Ctrl (wx.SearhCtrl)
        # PARENT:   Word List Panel
        # PURPOSE:  For searching word
        self._wordSearchCtrl = wx.SearchCtrl(
            parent  = wordListPanel,
            id      = wx.ID_ANY
        )

        self._wordSearchCtrl.SetFocus()

        wordListPanelVBoxSizer.Add(
            item        = self._wordSearchCtrl,
            proportion  = 0,
            flag        = wx.EXPAND | wx.BOTTOM,
            border      = self.AppSettings.BorderThickness * 2
        )

        # CONTROL:  Word List Ctrl (wx.ListBox)
        # PARENT:   Word List Panel
        # PURPOSE:  To show word list
        self._wordListBox = wx.ListBox(
            parent  = wordListPanel,
            id      = wx.ID_ANY
        )

        wordListPanelVBoxSizer.Add(
            item        = self._wordListBox,
            proportion  = 1,
            flag        = wx.EXPAND | wx.ALL
        )
        
        # Initializing
        self._defaultFont = self._wordListBox.GetFont()
        self.LoadLibrary()                          # Loading Library
        
        self._backButton.Enable(enable = False)
        self._nextButton.Enable(enable = False)
        
        # Retrieving word that was searched last time when application was closed
        if (self.AppSettings.LastWordIndex != None):
            self._wordListBox.SetSelection(self.AppSettings.LastWordIndex)
            self._wordListBox.EnsureVisible(self.AppSettings.LastWordIndex)
            self.GetWordDefinition()
            
            # Adding that last word to history
            CurrentWordSearchHistory.append(
                        WordSearchHistory(
                                wordIndex          = self.AppSettings.LastWordIndex,
                                originLanguage     = self.AppSettings.CurrentlySelectedLanguage[0],
                                translatedLanguage = self.AppSettings.CurrentlySelectedLanguage[1]
                        )
            )
        
        # EVENT:
        # EVENT FOR: DictionaryWindow
        self.Bind(
            event   = wx.EVT_CLOSE,
            handler = self.OnDictionaryWindowClosed, id = self.GetId()
        )
        
        # EVENT FOR: Back Button
        self.Bind(
            event   = wx.EVT_BUTTON,
            handler = self.OnBackButtonClicked,
            id      = self._backButton.GetId()
        )
        
        # EVENT FOR: Next Button
        self.Bind(
            event   = wx.EVT_BUTTON,
            handler = self.OnNextButtonClicked,
            id      = self._nextButton.GetId()
        )

        # EVENT FOR: FromComboBox
        self.Bind(
            event   = wx.EVT_COMBOBOX,
            handler = self.OnFromComboBoxSelectionChanged,
            id      = self._fromComboBox.GetId()
        )

        # EVENT FOR: ToComboBox
        self.Bind(
            event   = wx.EVT_COMBOBOX,
            handler = self.OnToComboBoxSelectionChanged,
            id      = self._toComboBox.GetId()
        )
        
        # EVENT FOR: AboutButton
        self.Bind(
            event   = wx.EVT_BUTTON,
            handler = self.OnAboutButtonClicked,
            id      = self._aboutButton.GetId()
        )
        
        # EVENT FOR: WordListBox
        self.Bind(
            event   = wx.EVT_LISTBOX,
            handler = self.OnWordListBoxSelectionChanged,
            id      = self._wordListBox.GetId()
        )
        
        # EVENT FOR: WordSearchCtrl (while typing)
        self.Bind(
            event   = wx.EVT_TEXT,
            handler = self.OnSearching,
            id      = self._wordSearchCtrl.GetId()
        )
        
        # EVENT FOR: ClickAndTypeButton
        self.Bind(
            event   = wx.EVT_BUTTON,
            handler = self.OnClickAndTypeButtonClicked,
            id      = self._clickAndTypeButton.GetId()
        )
        
        
        

    # METHOD NAME:     SearchOnAction
    # PARAMETER:       None
    # RETURN:          None
    # PURPOSE:         To search word from word list and show the word definition
    def SearchOnAction(self):
        result = Search(keyword = self._wordSearchCtrl.GetValue())
        
        if (result != None):
            self._wordListBox.SetSelection(result)
            self._wordListBox.EnsureVisible(result)
            
        self.GetWordDefinition()
        
    # METHOD NAME:    LoadLibrary
    # PARAMETER:      None
    # RETURN:         None
    # PURPOSE:        1. Load library (word list and word definition) into memory
    #                 2. Set word list into _wordListBox control
    def LoadLibrary(self):
        currentWordList       = ""
        currentWordDefinition = ""
        
        # If FromComboBox selection is ENGLISH and ToComboBox selection is Bengali
        if   ((self.AppSettings.CurrentlySelectedLanguage[0] == 0) and (self.AppSettings.CurrentlySelectedLanguage[1] == 0)):
            currentWordList         = FileSettings.EnWordListFile1
            currentWordDefinition   = FileSettings.EnToEnWordDefinitionListFile
        # Or, if FromComboBox selection is BENGALI and ToComboBox selection is ENGLISH
        elif ((self.AppSettings.CurrentlySelectedLanguage[0] == 0) and (self.AppSettings.CurrentlySelectedLanguage[1] == 1)):
            currentWordList         = FileSettings.EnWordListFile2
            currentWordDefinition   = FileSettings.EnToBnWordDefinitionListFile
        # Or, if FromComboBox selection is BENGALI and ToComboBox selection is Bengali
        elif ((self.AppSettings.CurrentlySelectedLanguage[0] == 1) and (self.AppSettings.CurrentlySelectedLanguage[1] == 1)):
            currentWordList         = FileSettings.BnWordListFile2
            currentWordDefinition   = FileSettings.BnToBnWordDefinitionListFile
        # Or, if FromComboBox selection is BENGALI and ToComboBox selection is ENGLISH
        else:
            currentWordList         = FileSettings.BnWordListFile1
            currentWordDefinition   = FileSettings.BnToEnWordDefinitionListFile
        
        # Now, load library from file
        self._currentLibrary = GetLibrary(
                   wordList  = currentWordList,
                   wordDef   = currentWordDefinition
        )
        
        # Set word list to _wordListBox control
        self._wordListBox.SetItems(self._currentLibrary.WordList)

        if ((sys.platform.startswith("win32")) and ((currentWordList == FileSettings.BnWordListFile1) or (currentWordList == FileSettings.BnWordListFile2))):
            self._wordListBox.SetFont(font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        else:
            self._wordListBox.SetFont(font = self._defaultFont)

        # Clear _wordMeaningRichTextCtrl
        self._wordMeaningRichTextCtrl.Clear()

    # METHOD NAME:    GetWordDefinition
    # PARAMETER:      None
    # RETURN:         None
    # PURPOSE:        To show word meaning from the word list 
    def GetWordDefinition(self):
        self._wordMeaningRichTextCtrl.Clear()
        self._wordMeaningRichTextCtrl.BeginFontSize(pointSize = 22)
        self._wordMeaningRichTextCtrl.BeginTextColour(wx.Colour(52, 101, 164))
        self._wordMeaningRichTextCtrl.WriteText(self._currentLibrary.WordDefinitionList[self._wordListBox.GetSelection()].Title)
        self._wordMeaningRichTextCtrl.EndTextColour()
        self._wordMeaningRichTextCtrl.EndFontSize()
        self._wordMeaningRichTextCtrl.Newline()
        self._wordMeaningRichTextCtrl.Newline()
        self._wordMeaningRichTextCtrl.BeginFontSize(14)
        self._wordMeaningRichTextCtrl.BeginItalic()
        self._wordMeaningRichTextCtrl.BeginTextColour(wx.Colour(100, 100, 100))
        self._wordMeaningRichTextCtrl.WriteText(self._currentLibrary.WordDefinitionList[self._wordListBox.GetSelection()].GrammaticalSyntax)
        self._wordMeaningRichTextCtrl.EndTextColour()
        self._wordMeaningRichTextCtrl.EndItalic()
        self._wordMeaningRichTextCtrl.EndFontSize()
        self._wordMeaningRichTextCtrl.Newline()
        self._wordMeaningRichTextCtrl.Newline()
        self._wordMeaningRichTextCtrl.BeginFontSize(12)
        self._wordMeaningRichTextCtrl.BeginTextColour(wx.Colour(0, 0, 0))
        self._wordMeaningRichTextCtrl.WriteText(self._currentLibrary.WordDefinitionList[self._wordListBox.GetSelection()].WordDetails)
        self._wordMeaningRichTextCtrl.EndTextColour()
        self._wordMeaningRichTextCtrl.EndFontSize()


    # METHOD NAME: OnDictionaryWindowClosed
    # PARAMETER:   Event
    # RETURN:      None
    # PURPOSE:     Save Application Settings (self.AppSettings) to 'dictionary_config.cfg' file
    def OnDictionaryWindowClosed(self, event):
        if (not self.IsMaximized()):
            self.AppSettings.MainWindowWidth    = self.GetSize().width
            self.AppSettings.MainWindowHeight   = self.GetSize().height
            self.AppSettings.SplitterProportion = self._mainBodySplitter.proportion
            
        if (self._wordListBox.GetSelection() != -1):
            self.AppSettings.LastWordIndex = self._wordListBox.GetSelection()
            
        SaveOrCreateApplicationSettingsFile(settings = self.AppSettings)
        event.Skip()

    # METHOD NAME:  OnFromComboBoxSelectionChanged
    # PARAMETER:    Event
    # RETURN:       None
    # PURPOSE:      1. Save currently selected language of FromComboBox to self.AppSettings for now
    #               2. Load library for refreshment
    #               3. If any word typed within search box, show result for that word too.
    def OnFromComboBoxSelectionChanged(self, event):
        self.AppSettings.CurrentlySelectedLanguage[0] = self._fromComboBox.GetSelection()
        self.LoadLibrary()
        
        # If search box has any word, search that to within newly loaded library
        if (self._wordSearchCtrl.GetValue() != ""):
            self.SearchOnAction()


    # METHOD NAME:  OnToComboBoxSelectionChanged
    # PARAMETER:    Event
    # RETURN:       None
    # PURPOSE:      1. Save currently selected language of ToComboBox to self.AppSettings for now.
    #               2. Load library for refreshment
    #               3. If any word typed within search box, show result for that word too.
    def OnToComboBoxSelectionChanged(self, event):
        self.AppSettings.CurrentlySelectedLanguage[1] = self._toComboBox.GetSelection()
        self.LoadLibrary()
        
        # If search box has any word, search that to within newly loaded library
        if (self._wordSearchCtrl.GetValue() != ""):
            self.SearchOnAction()
        
    
    # METHOD NAME:    OnClickAndTypeButtonClicked
    # PARAMETER:      Event
    # RETURN:         None
    # PURPOSE:        To show bengali keyboard button, where user can type using mouse click
    def OnClickAndTypeButtonClicked(self, event):
        clickAndTypeKeyboard = BengaliKeyboardFrame(self, wx.ID_ANY, "Click & Type", self._wordSearchCtrl, self.AppSettings)
        clickAndTypeKeyboard.Show(True)
        
    
    # METHOD NAME:    OnAboutButtonClicked
    # PARAMETER:      Event
    # RETURN:         None
    # PURPOSE:        Show version, license and credits
    def OnAboutButtonClicked(self, event):
        developerAuthorInfo = AuthorInfo(
            name    = "Mohammod Zunayed Hassan",
            website = None,
            email   = "zunayed-hassan@live.com"
        )
        
        artworkAuthorInfo = AuthorInfo(
            name    = "www.oxygen-icons.org",
            website = "http://www.oxygen-icons.org",
            email   = None
        )
        
        developerAuthorsInfo              = AuthorsInfo()
        developerAuthorsInfo.Contribution = "Developed by"
        developerAuthorsInfo.Authors      = [ developerAuthorInfo ]
        
        artWorkAuthorsInfo              = AuthorsInfo()
        artWorkAuthorsInfo.Contribution = "Artwork by"
        artWorkAuthorsInfo.Authors      = [ artworkAuthorInfo ] 
        
        aboutBoxInformation = AboutBoxInfo()
        aboutBoxInformation.ApplicationName = "Dictionary"
        aboutBoxInformation.Version         = "1.0"
        aboutBoxInformation.License         = "Resources/License.txt"
        aboutBoxInformation.AppDesc         = "A simple English to English, English to\nBengali, Bengali to English and\nBengali to Bengali Dictionary"
        aboutBoxInformation.Icon            = self.AppSettings.IconLocation + "dictionary.png"
        aboutBoxInformation.AuthorsList     = [ developerAuthorsInfo, artWorkAuthorsInfo ]
        
        if (sys.platform.startswith("win32")):
            aboutDialog = AboutBoxDialogWindows(
                parent       = self,
                id           = wx.ID_ANY,
                title        = "About " + aboutBoxInformation.ApplicationName,
                aboutBoxInfo = aboutBoxInformation,
                appSettings  = self.AppSettings
            )
        else:
            aboutDialog = AboutBoxDialog(
                parent       = self,
                id           = wx.ID_ANY,
                title        = "About " + aboutBoxInformation.ApplicationName,
                aboutBoxInfo = aboutBoxInformation,
                appSettings  = self.AppSettings
            )    
        
        
        aboutDialog.ShowModal()
        
    
    # METHOD NAME:    OnWordListBoxSelectionChanged
    # RAMAMETER:      Event
    # RETURN:         None
    # PURPOSE:        1. Clear the _wordMeaningRichTextCtrl
    #                 2. Show the word defenition that was selected in _wordListBox
    #                 3. Save word search history
    #                 4. Enable Back Button
    def OnWordListBoxSelectionChanged(self, event):
        self.GetWordDefinition()                # Show word definition
        self.SaveWordSearchHistoryOnAction()    # Save word search history
        
        
    # METHOD NAME:    OnSearching
    # PARAMETER:      Event
    # RETURN:         None
    # PURPOSE:        To help user to searh word and that particular word meaning
    def OnSearching(self, event):
        result = Search(keyword = self._wordSearchCtrl.GetValue())
        
        if (result != None):
            self._wordListBox.SetSelection(result)
            self._wordListBox.EnsureVisible(result)
            self.SaveWordSearchHistoryOnAction()
            
        self.GetWordDefinition()
    
    # METHOD NAME:    OnBackButtonClicked
    # PARAMETER:      Event
    # RETURN:         None
    # PURPOSE:        1. Show previous word
    #                 2. Tweak 'word search history' index or enable 'next button' if necessary
    #                 3. Enable 'next button'
    def OnBackButtonClicked(self, event):
        # Show word from history
        self.ShowWordFromHistory(wordSearchHistory = CurrentWordSearchHistory[self._wordSearchIndex])
        
        # Update 'word search history' index
        if (self._wordSearchIndex != 0):
            self._wordSearchIndex -= 1
        else:
            self._backButton.Enable(enable = False)     # Disable 'previous button' when index is in first position of the list
        
        # Enable 'next button'
        if (not self._nextButton.Enabled):
            self._nextButton.Enable(enable = True)
    
    # METHOD NAME:    OnNextButtonClicked
    # PARAMETER:      Event
    # RETURN:         None
    # PURPOSE:        1. Show next word
    #                 2. Tweak 'word search history' index or enable 'next button' if necessary
    #                 3. Enable 'back button'
    def OnNextButtonClicked(self, event):
        # Show word from history
        self.ShowWordFromHistory(wordSearchHistory = CurrentWordSearchHistory[self._wordSearchIndex + 1])
        
        # Update 'word search history' index
        if (self._wordSearchIndex != len(CurrentWordSearchHistory) - 2):
            self._wordSearchIndex += 1
        else:
            self._nextButton.Enable(enable = False)     # Disable 'next button' when index is in last position of the list
            
        # Enable 'back button'
        if (not self._backButton.IsEnabled()):
            self._backButton.Enable(enable = True)
        
    # METHOD NAME:    ShowWordFromHistory
    # PARAMETER:      (Model.WordSearchHistory) wordSearchHistory
    # RETURN:         None
    # PURPOSE:        1. Check 'word search history' if, that word is in same language that we are currently in. If not, then load that language library first.
    #                 2. Show word definition from  'word search history'
    def ShowWordFromHistory(self, wordSearchHistory):
        if ((self.AppSettings.CurrentlySelectedLanguage[0] != wordSearchHistory.OriginLanguage) or (self.AppSettings.CurrentlySelectedLanguage[1] != wordSearchHistory.TranslatedLanguage)):
            self._fromComboBox.SetSelection(wordSearchHistory.OriginLanguage)
            self._toComboBox.SetSelection(wordSearchHistory.TranslatedLanguage)
            self.AppSettings.CurrentlySelectedLanguage = [ wordSearchHistory.OriginLanguage, wordSearchHistory.TranslatedLanguage ]
            self.LoadLibrary()
            
        self._wordListBox.SetSelection(wordSearchHistory.WordIndex)
        self._wordListBox.EnsureVisible(wordSearchHistory.WordIndex)
        self.GetWordDefinition()
        
        
    # METHOD NAME:    SaveWordSearchHistoryOnAction
    # PARAMETER:      None
    # RETURN:         None
    # PURPOSE:        1. Save word history
    #                 2. Tweak 'word search history' index
    #                 2. Enable 'back button'
    def SaveWordSearchHistoryOnAction(self):
        #   if    1. 'word list box' has a selected item and current 'word search history' list is empty
        #   or,   2. 'word list box' has a selected item and current 'word search history' list is not empty and previous 'word search index' is not same as currently selected word (from word list)
        #   then, save into 'word search history' list
        if (((self._wordListBox.GetSelection() != -1) and (CurrentWordSearchHistory == [])) or ((CurrentWordSearchHistory != []) and (self._wordListBox.GetSelection() != -1) and (CurrentWordSearchHistory[len(CurrentWordSearchHistory) - 1].WordIndex != self._wordListBox.GetSelection()))):
            # Save 'word search history' list
            SaveWordSearchHistory(
                    wordSearchHistory      = WordSearchHistory(
                        wordIndex          = self._wordListBox.GetSelection(),
                        originLanguage     = self.AppSettings.CurrentlySelectedLanguage[0],
                        translatedLanguage = self.AppSettings.CurrentlySelectedLanguage[1] 
                    )
            )
            
            # Tweak 'word search history' index
            self._wordSearchIndex = len(CurrentWordSearchHistory) - 2
            
            # Enable 'back button' only when 'word search history' list has more than one element
            if ((not self._backButton.IsEnabled()) and (len(CurrentWordSearchHistory) != 1)):
                self._backButton.Enable(enable = True)
