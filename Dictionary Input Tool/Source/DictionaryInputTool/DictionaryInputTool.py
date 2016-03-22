"""
APPLICATION NAME: Dictionary Input Tool
VERSION:          1.0.9
LICENSE:          GNU GPL 2
DESCRIPTION:      This tool is for editing the word list of Dictionary.

TARGET PLATFORM:  Windows, Linux, Mac OS
INTERFACE:        GUI
FRAMEWORK:        wxPython

AUTHOR:           Mohammod Zunayed Hassan
EMAIL:            zunayed-hassan@live.com
"""

import wx, os, pickle, gzip, zlib, tempfile, wx.richtext as rt

class WordList():
    Words = []

class WordDefinition():
    def __init__(self, title, wordDetails, grammaticalSyntax = u""):
        self.Title = title
        self.GrammaticalSyntax = grammaticalSyntax
        self.WordDetails = wordDetails

class FileSettings():
    EnWordListFile1              = "ee_eng_word_list.obj"
    EnWordListFile2              = "eb_eng_word_list.obj"
    EnToEnWordDefinitionListFile = "eng_to_eng_word_definition_list.obj"
    EnToBnWordDefinitionListFile = "eng_to_bn_word_definition_list.obj"
    BnWordListFile1              = "be_bn_word_list.obj"
    BnWordListFile2              = "bb_bn_word_list.obj"
    BnToEnWordDefinitionListFile = "bn_to_eng_word_definition_list.obj"
    BnToBnWordDefinitionListFile = "bn_to_bn_word_definition_list.obj"

    LibraryLocation              = "Resources/Library/"


class MainWindow(wx.Frame):
    _wordList = None
    _wordDefinitionList = None

    _addMode    = False
    _insertMode = False

    WordListFile = None
    WordDefinitionListFile = None

    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(600, 600))

        mainPanel = wx.Panel(self, wx.ID_ANY)
        mainPanelVBoxSizer = wx.BoxSizer(wx.VERTICAL)
        mainPanel.SetSizer(mainPanelVBoxSizer)

        self._toolbar = wx.ToolBar(mainPanel, wx.ID_ANY)
        mainPanelVBoxSizer.Add(self._toolbar, 0, wx.EXPAND)

        self._toolbar.AddSimpleTool(102, wx.Bitmap("Resources/Icons/document-save.png"), "Save to library")
        self._toolbar.AddSimpleTool(103, wx.Bitmap("Resources/Icons/dialog-cancel.png"), "Cancel")
        self._toolbar.AddSeparator()
        self._toolbar.AddSimpleTool(101, wx.Bitmap("Resources/Icons/list-add.png"), "Add new word")
        self._toolbar.AddSimpleTool(104, wx.Bitmap("Resources/Icons/document-edit.png"), "Edit word")
        self._toolbar.AddSimpleTool(107, wx.Bitmap("Resources/Icons/list-insert.png"), "Insert word (Above)")
        self._toolbar.AddSimpleTool(105, wx.Bitmap("Resources/Icons/edit-delete.png"), "Delete word")
        self._toolbar.AddSeparator()
        self._toolbar.AddSimpleTool(106, wx.Bitmap("Resources/Icons/help-about.png"), "About")
        self._toolbar.Realize()

        bodyPanel1 = wx.Panel(mainPanel, wx.ID_ANY)
        mainPanelVBoxSizer.Add(bodyPanel1, 1, wx.EXPAND, 3)
        bodyPanel1HBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        bodyPanel1.SetSizer(bodyPanel1HBoxSizer)

        wordEditPanel3 = wx.Panel(bodyPanel1, wx.ID_ANY)
        bodyPanel1HBoxSizer.Add(wordEditPanel3)
        wordEditPanel3VBoxSizer = wx.BoxSizer(wx.VERTICAL)
        wordEditPanel3.SetSizer(wordEditPanel3VBoxSizer)

        wordStaticText = wx.StaticText(wordEditPanel3, wx.ID_ANY, "Word:")
        wordEditPanel3VBoxSizer.Add(wordStaticText, 0, wx.LEFT | wx.TOP | wx.RIGHT, 3)

        self._wordTextCtrl = wx.TextCtrl(wordEditPanel3, wx.ID_ANY)
        wordEditPanel3VBoxSizer.Add(self._wordTextCtrl, 0, wx.LEFT | wx.TOP | wx.RIGHT, 3)

        wordDetailsPanel = wx.Panel(bodyPanel1, wx.ID_ANY)
        bodyPanel1HBoxSizer.Add(wordDetailsPanel, 1, wx.EXPAND)
        wordDetailsPanelVBoxSizer = wx.BoxSizer(wx.VERTICAL)
        wordDetailsPanel.SetSizer(wordDetailsPanelVBoxSizer)

        wordTitleStaticText = wx.StaticText(wordDetailsPanel, wx.ID_ANY, "Word Details Title:")
        wordDetailsPanelVBoxSizer.Add(wordTitleStaticText, 0, wx.LEFT | wx.TOP | wx.RIGHT, 3)

        self._wordTitleTextCtrl = wx.TextCtrl(wordDetailsPanel, wx.ID_ANY)
        wordDetailsPanelVBoxSizer.Add(self._wordTitleTextCtrl, 0, wx.LEFT | wx.TOP | wx.RIGHT, 3)

        grammaticalSyntaxStaticText = wx.StaticText(wordDetailsPanel, wx.ID_ANY, "Grammatical Syntax: (Optional)")
        wordDetailsPanelVBoxSizer.Add(grammaticalSyntaxStaticText, 0, wx.LEFT | wx.TOP | wx.RIGHT, 3)

        self._grammaticalSyntaxTextCtrl = wx.TextCtrl(wordDetailsPanel, wx.ID_ANY)
        wordDetailsPanelVBoxSizer.Add(self._grammaticalSyntaxTextCtrl, 0, wx.LEFT | wx.TOP, 3)


        wordDetailsStaticText = wx.StaticText(wordDetailsPanel, wx.ID_ANY, "Word Details:")
        wordDetailsPanelVBoxSizer.Add(wordDetailsStaticText, 0, wx.LEFT | wx.TOP | wx.RIGHT, 3)

        self._wordDetailsTextCtrl = wx.TextCtrl(wordDetailsPanel, wx.ID_ANY, style = wx.TE_MULTILINE)
        wordDetailsPanelVBoxSizer.Add(self._wordDetailsTextCtrl, 1, wx.LEFT | wx.EXPAND | wx.RIGHT | wx.BOTTOM | wx.TOP, 3)

        mainPanelVBoxSizer.Add(wx.StaticText(mainPanel, wx.ID_ANY, "Preview:"), 0, wx.TOP | wx.LEFT | wx.BOTTOM | wx.RIGHT, 3)

        bodyPanel2 = wx.Panel(mainPanel, wx.ID_ANY)
        mainPanelVBoxSizer.Add(bodyPanel2, 1, wx.EXPAND, 3)
        bodyPanel2HBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        bodyPanel2.SetSizer(bodyPanel2HBoxSizer)

        wordListPanel = wx.Panel(bodyPanel2, wx.ID_ANY)
        bodyPanel2HBoxSizer.Add(wordListPanel, 1, wx.LEFT | wx.TOP | wx.BOTTOM | wx.EXPAND, 3)
        wordListPanelVBoxSizer = wx.BoxSizer(wx.VERTICAL)
        wordListPanel.SetSizer(wordListPanelVBoxSizer)

        self._wordListCtrl = wx.ListBox(wordListPanel, wx.ID_ANY)
        wordListPanelVBoxSizer.Add(self._wordListCtrl, 1, wx.EXPAND | wx.TOP | wx.BOTTOM, 3)

        self._wordDetailsRichTextCtrl = rt.RichTextCtrl(bodyPanel2, wx.ID_ANY)
        self._wordDetailsRichTextCtrl.SetEditable(False)
        bodyPanel2HBoxSizer.Add(self._wordDetailsRichTextCtrl, 3, wx.EXPAND | wx.LEFT | wx.TOP | wx.RIGHT | wx.BOTTOM, 3)

        self.StatusBar = self.CreateStatusBar()
        self.SetStatusText("Program started")

        # Initializing
        self.CreateBlankLibrary()
        self.LoadLibrary()

        # Event
        self.Bind(wx.EVT_TOOL,      self.OnAddButtonClicked,             id = 101)
        self.Bind(wx.EVT_TOOL,      self.OnSaveButtonClicked,            id = 102)
        self.Bind(wx.EVT_TOOL,      self.OnCancelButtonClicked,          id = 103)
        self.Bind(wx.EVT_TOOL,      self.OnEditButtonClicked,            id = 104)
        self.Bind(wx.EVT_TOOL,      self.OnDeleteButtonClicked,          id = 105)
        self.Bind(wx.EVT_TOOL,      self.OnAboutButtonClicked,           id = 106)
        self.Bind(wx.EVT_TOOL,      self.OnInsertButtonClicked,          id = 107)
        self.Bind(wx.EVT_LISTBOX,   self.OnWordListCtrlSelectionChanged, id = self._wordListCtrl.GetId())
        self.Bind(wx.EVT_CLOSE,     self.OnClosed,                       id = self.GetId())

    def OnInsertButtonClicked(self, event):
        self._insertMode = True
        self.ClearEditPanel()
        self.EnableEditPanel(True)
        self.EnableToolbarButton(saveState = True, cancelState = True)

    def OnDeleteButtonClicked(self, event):
        confirmationDialog = wx.MessageDialog(self, "Are you sure that, you want to delete '" + self._wordList[self._wordListCtrl.GetSelection()] + "' word?", "Confirmation", wx.YES_NO | wx.CENTER | wx.ICON_QUESTION)
        response = confirmationDialog.ShowModal()

        if (response == wx.ID_YES):
            currentWord = self._wordList[self._wordListCtrl.GetSelection()]

            # Remove from memory
            self._wordList.remove(self._wordList[self._wordListCtrl.GetSelection()])
            self._wordDefinitionList.remove(self._wordDefinitionList[self._wordListCtrl.GetSelection()])

            # Save to library
            self.SerializeWordListFile(tempfile.gettempdir() + "/" + self.WordListFile)
            self.Compress((tempfile.gettempdir() + "/" + self.WordListFile), (FileSettings.LibraryLocation + self.WordListFile + ".gz"))

            self.SerializeWordDefinitionFile(tempfile.gettempdir() + "/" + self.WordDefinitionListFile)
            self.Compress(tempfile.gettempdir() + "/" + self.WordDefinitionListFile, (FileSettings.LibraryLocation + self.WordDefinitionListFile + ".gz"))

            self.LoadLibrary()
            self.SetStatusText("'" + currentWord + "' word deleted")

            if (self._wordList == []):
                self._wordDetailsRichTextCtrl.Clear()

    def OnEditButtonClicked(self, event):
        self._addMode = False
        self.EnableEditPanel(True)
        self.EnableToolbarButton(saveState = True, cancelState = True)
        self._wordTextCtrl.SetFocus()


    def OnWordListCtrlSelectionChanged(self, event):
        self.EnableToolbarButton(addState = True, editState = True, deleteState = True, insertState = True)
        self._wordTextCtrl.SetLabel(self._wordList[self._wordListCtrl.GetSelection()])

        if (not self._wordDefinitionList == None):
            self._wordTitleTextCtrl.SetLabel(self._wordDefinitionList[self._wordListCtrl.GetSelection()].Title)
            self._grammaticalSyntaxTextCtrl.SetLabel(self._wordDefinitionList[self._wordListCtrl.GetSelection()].GrammaticalSyntax)
            self._wordDetailsTextCtrl.SetLabel(self._wordDefinitionList[self._wordListCtrl.GetSelection()].WordDetails)

            self._wordDetailsRichTextCtrl.Clear()
            self._wordDetailsRichTextCtrl.BeginFontSize(20)
            self._wordDetailsRichTextCtrl.BeginTextColour(wx.Colour(124, 110, 229))
            self._wordDetailsRichTextCtrl.WriteText(self._wordDefinitionList[self._wordListCtrl.GetSelection()].Title)
            self._wordDetailsRichTextCtrl.EndFontSize()
            self._wordDetailsRichTextCtrl.EndTextColour()
            self._wordDetailsRichTextCtrl.Newline()
            self._wordDetailsRichTextCtrl.BeginFontSize(14)
            self._wordDetailsRichTextCtrl.BeginItalic()
            self._wordDetailsRichTextCtrl.BeginTextColour(wx.Colour(140, 140, 140))
            self._wordDetailsRichTextCtrl.WriteText(self._wordDefinitionList[self._wordListCtrl.GetSelection()].GrammaticalSyntax)
            self._wordDetailsRichTextCtrl.EndItalic()
            self._wordDetailsRichTextCtrl.EndTextColour()
            self._wordDetailsRichTextCtrl.EndFontSize()
            self._wordDetailsRichTextCtrl.Newline()
            self._wordDetailsRichTextCtrl.Newline()
            self._wordDetailsRichTextCtrl.BeginFontSize(12)
            self._wordDetailsRichTextCtrl.WriteText(self._wordDefinitionList[self._wordListCtrl.GetSelection()].WordDetails)
            self._wordDetailsRichTextCtrl.EndFontSize()

        self.SetStatusText("Looking for " + self._wordList[self._wordListCtrl.GetSelection()] + " word")

    def OnAddButtonClicked(self, event):
        self._addMode = True
        self.ClearEditPanel()
        self.EnableToolbarButton(saveState = True, cancelState = True)
        self.EnableEditPanel(True)

    def OnSaveButtonClicked(self, event):
        self.SaveToLibrary()
        self.ClearEditPanel()
        self.EnableToolbarButton(addState = True)

    def OnCancelButtonClicked(self, event):
        self.ClearEditPanel()
        self.EnableEditPanel(False)
        self.LoadLibrary()

    def OnAboutButtonClicked(self, event):
        info = wx.AboutDialogInfo()
        info.Name = "Dictionary Input Tool"
        info.Version = "(v 1.0.9)"
        info.Description = "This tool is for editing the word list of Dictionary."
        info.Developers = [ "Mohammod Zunayed Hassan\nEmail: zunayed-hassan@live.com" ]
        info.License = "GNU GPL 2"
        wx.AboutBox(info)

    def OnClosed(self, event):
        (self.GetParent()).Close()


    def EnableEditPanel(self, state):
        self._wordTextCtrl.Enabled = state
        self._wordTitleTextCtrl.Enabled = state
        self._grammaticalSyntaxTextCtrl.Enabled = state
        self._wordDetailsTextCtrl.Enabled = state

    def CreateBlankLibrary(self):
        if (not os.path.exists(FileSettings.LibraryLocation + self.WordListFile + ".gz")):
            self.SerializeWordListFile(tempfile.gettempdir() + "/" + self.WordListFile)
            self.Compress((tempfile.gettempdir() + "/" + self.WordListFile), (FileSettings.LibraryLocation + self.WordListFile + ".gz"))

        if (not os.path.exists(FileSettings.LibraryLocation + self.WordDefinitionListFile + ".gz")):
            self.SerializeWordDefinitionFile(tempfile.gettempdir() + "/" + self.WordDefinitionListFile)
            self.Compress((tempfile.gettempdir() + "/" + self.WordDefinitionListFile), (FileSettings.LibraryLocation + self.WordDefinitionListFile + ".gz"))


    def EnableToolbarButton(self, addState = False, saveState = False, cancelState = False, editState = False, deleteState = False, insertState = False):
        self._toolbar.EnableTool(101, addState)
        self._toolbar.EnableTool(102, saveState)
        self._toolbar.EnableTool(103, cancelState)
        self._toolbar.EnableTool(104, editState)
        self._toolbar.EnableTool(105, deleteState)
        self._toolbar.EnableTool(107, insertState)

    def SaveToLibrary(self):
        currentWord = self._wordTextCtrl.GetLabel()
        currentSelection = self._wordListCtrl.GetSelection()

        if (self._addMode == True and self._insertMode == False):
            # Adding word list
            if (self._wordList == None):
                self._wordList = [ self._wordTextCtrl.GetLabel() ]
            else:
                self._wordList.append(self._wordTextCtrl.GetLabel())

            # Adding word definition list
            wordDefinition = WordDefinition(self._wordTitleTextCtrl.GetLabel(), self._wordDetailsTextCtrl.GetLabel(), self._grammaticalSyntaxTextCtrl.GetLabel())

            if (self._wordDefinitionList == None):
               self._wordDefinitionList = [ wordDefinition ]
            else:
                self._wordDefinitionList.append(wordDefinition)

        elif (self._addMode == False and self._insertMode == False):
            self._wordList[self._wordListCtrl.GetSelection()] = self._wordTextCtrl.GetLabel()
            wordDefinition = WordDefinition(self._wordTitleTextCtrl.GetLabel(), self._wordDetailsTextCtrl.GetLabel(), self._grammaticalSyntaxTextCtrl.GetLabel())

            if (self._wordDefinitionList == None):
                self._wordDefinitionList = [ wordDefinition ]
            else:
                self._wordDefinitionList[self._wordListCtrl.GetSelection()] = wordDefinition

        elif ((self._insertMode == True) and (self._addMode == False) and (self._wordListCtrl.GetSelection() != -1)):
            self._wordList.insert(self._wordListCtrl.GetSelection(), self._wordTextCtrl.GetLabel())
            self._wordDefinitionList.insert(self._wordListCtrl.GetSelection(), WordDefinition(self._wordTitleTextCtrl.GetLabel(), self._wordDetailsTextCtrl.GetLabel(), self._grammaticalSyntaxTextCtrl.GetLabel()))

        self.SerializeWordListFile(tempfile.gettempdir() + "/" + self.WordListFile)
        self.Compress((tempfile.gettempdir() + "/" + self.WordListFile), (FileSettings.LibraryLocation + self.WordListFile + ".gz"))

        self.SerializeWordDefinitionFile(tempfile.gettempdir() + "/" + self.WordDefinitionListFile)
        self.Compress(tempfile.gettempdir() + "/" + self.WordDefinitionListFile, (FileSettings.LibraryLocation +self.WordDefinitionListFile + ".gz"))

        self.LoadLibrary()
        self.SetStatusText(currentWord + " word added")

        if (currentSelection != -1):
            self._wordListCtrl.SetSelection(currentSelection)

    def ClearEditPanel(self):
        self._wordTextCtrl.SetLabel("")
        self._wordTitleTextCtrl.SetLabel("")
        self._grammaticalSyntaxTextCtrl.SetLabel("")
        self._wordDetailsTextCtrl.SetLabel("")

    def LoadLibrary(self):
        self.EnableToolbarButton(addState = True)
        self.EnableEditPanel(False)
        self.ClearEditPanel()
        self._addMode = False
        self._insertMode = False

        # Loading word list
        self.Decompress((FileSettings.LibraryLocation + self.WordListFile + ".gz"), (tempfile.gettempdir() + "/" + self.WordListFile))
        self.LoadWordListToMemory(tempfile.gettempdir() + "/" + self.WordListFile)

        # Loading word definition list
        self.Decompress((FileSettings.LibraryLocation + self.WordDefinitionListFile + ".gz"), (tempfile.gettempdir() + "/" + self.WordDefinitionListFile))
        self.LoadWordDefinitionListToLibrary(tempfile.gettempdir() + "/" + self.WordDefinitionListFile)

        if (not self._wordList == None):
            self._wordListCtrl.SetItems(self._wordList)

        self.SetStatusText("Library loaded")

    def Decompress(self, input_filename, output_filename):
        fin = open(input_filename, "rb")
        decompressedData = zlib.decompress(fin.read(), 16+zlib.MAX_WBITS)
        fin.close()

        fout = open(output_filename, "wb")
        fout.write(decompressedData)
        fout.close()

    def Compress(self, input_filename, output_filename):
        fin = open(input_filename, "rb")
        compressedFile = gzip.open(output_filename, "wb")
        compressedFile.writelines(fin)
        compressedFile.close()
        fin.close()

    def SerializeWordListFile(self, filename):
        fout = open(filename, "wb")
        pickle.dump(self._wordList, fout)
        fout.close()

    def LoadWordListToMemory(self, filename):
        fin = open(filename, "rb")
        self._wordList = pickle.load(fin)
        fin.close()

    def SerializeWordDefinitionFile(self, filename):
        fout = open(filename, "wb")
        pickle.dump(self._wordDefinitionList, fout)
        fout.close()

    def LoadWordDefinitionListToLibrary(self, filename):
        fin = open(filename, "rb")
        self._wordDefinitionList = pickle.load(fin)
        fin.close()

class WizardDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size = wx.Size(265, 200))

        self._enToEnRadioButton = wx.RadioButton(self, wx.ID_ANY, "English to English", wx.Point(60, 30), style = wx.RB_GROUP)
        self._enToBnRadioButton = wx.RadioButton(self, wx.ID_ANY, "English to Bengali", wx.Point(60, 50))
        self._bnToEnRadioButton = wx.RadioButton(self, wx.ID_ANY, "Bengali to English", wx.Point(60, 70))
        self._bnToBnRadioButton = wx.RadioButton(self, wx.ID_ANY, "Bengali to Bengali", wx.Point(60, 90))

        wx.StaticBox(self, wx.ID_ANY, "Language", wx.Point(30, 10), wx.Size(205, 110))

        nextButton = wx.Button(self, wx.ID_PREVIEW_NEXT, "Next", wx.Point(80, 140))
        cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel", wx.Point(160, 140))

        self.Bind(wx.EVT_BUTTON, self.OnNextButtonClicked, id = nextButton.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCancelButtonClicked, id = cancelButton.GetId())

    def OnNextButtonClicked(self, event):
        if (self._enToEnRadioButton.GetValue()):
            MainWindow.WordListFile = FileSettings.EnWordListFile1
            MainWindow.WordDefinitionListFile = FileSettings.EnToEnWordDefinitionListFile
        elif (self._enToBnRadioButton.GetValue()):
            MainWindow.WordListFile = FileSettings.EnWordListFile2
            MainWindow.WordDefinitionListFile = FileSettings.EnToBnWordDefinitionListFile
        elif (self._bnToEnRadioButton.GetValue()):
            MainWindow.WordListFile = FileSettings.BnWordListFile1
            MainWindow.WordDefinitionListFile = FileSettings.BnToEnWordDefinitionListFile
        else:
            MainWindow.WordListFile = FileSettings.BnWordListFile2
            MainWindow.WordDefinitionListFile = FileSettings.BnToBnWordDefinitionListFile

        mainWindow = MainWindow(self, wx.ID_ANY, "Dictionary Input Tool")
        mainWindow.SetIcon(wx.Icon("Resources/Icons/icon.ico", wx.BITMAP_TYPE_ICO))
        mainWindow.Center()
        mainWindow.Show(True)
        self.Hide()

    def OnCancelButtonClicked(self, event):
        self.Destroy()


class Application(wx.App):
    def OnInit(self):
        dictionaryInputToolWizard = WizardDialog(None, wx.ID_ANY, "Wizard: Dictionary Input Tool")
        dictionaryInputToolWizard.ShowModal()

        return True

if __name__ == "__main__":
    app = Application()
    app.MainLoop()

