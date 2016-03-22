#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'Zunayed Hassan'

import wx, sys, re
from bengali_alphabet_button import *
from Model.app_settings_model import *

class BengaliKeyboardFrame(wx.Frame):
    _borderStyle = None
    
    def __init__(self, parent, id, title, control, appSettings):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(760, 430))
        
        # If platorm is Windows, then use BORDER_THEME
        if (sys.platform.startswith("win32")):
            self._borderStyle = wx.BORDER_THEME
        # Otherwise, use SUNKEN_BORDER
        else:
            self._borderStyle = wx.SUNKEN_BORDER
        
        # CONTROL: Panel1 (wx.Panel)
        # LAYOUT:  BoxSizer Layout (Horizontal)
        panel1 = wx.Panel(parent = self, id = wx.ID_ANY)
        panel1HBoxSizer = wx.BoxSizer(orient = wx.HORIZONTAL)
        panel1.SetSizer(sizer = panel1HBoxSizer)

        # CONTROL: Panel2 (wx.Panel)
        # LAYOUT:  BoxSizer Layout (Vertical)
        panel2 = wx.Panel(parent = panel1, id = wx.ID_ANY)
        panel2VBoxSizer = wx.BoxSizer(orient = wx.VERTICAL)
        panel2.SetSizer(sizer = panel2VBoxSizer)
        panel1HBoxSizer.Add(item = panel2, proportion = 3, flag = wx.EXPAND)
        
        # CONTROL: wx.StaticText
        panel2VBoxSizer.Add(item = wx.StaticText(parent = panel2, id = wx.ID_ANY, label = u"ব্যঞ্জনবর্ণ"), proportion = 0, flag = wx.EXPAND | wx.ALL, border = appSettings.BorderThickness)

        # CONTROL: Panel3 (wx.Panel)
        # LAYOUT:  BoxSizer Layout (Vertical)
        panel3 = wx.Panel(parent = panel1, id = wx.ID_ANY)
        panel3VBoxSizer = wx.BoxSizer(orient = wx.VERTICAL)
        panel3.SetSizer(sizer = panel3VBoxSizer)
        panel1HBoxSizer.Add(item = panel3, proportion = 1, flag = wx.EXPAND)

        # CONTROL: Panel4 (wx.Panel)
        # LAYOUT:  Grid Bag Sizer Layout
        panel4 = wx.Panel(parent = panel2, id = wx.ID_ANY, style = self._borderStyle)
        panel4GridBagSizer = wx.GridBagSizer()
        panel4.SetSizerAndFit(sizer = panel4GridBagSizer)
        panel2VBoxSizer.Add(item = panel4, proportion = 2, flag = wx.EXPAND | wx.ALL, border = appSettings.BorderThickness * 2)
        
        # CONTROL: wx.StaticText
        panel2VBoxSizer.Add(item = wx.StaticText(parent = panel2, id = wx.ID_ANY, label = u"স্বরবর্ণ"), proportion = 0, flag = wx.EXPAND | wx.ALL, border = appSettings.BorderThickness)
        
        # CONTROL: Panel5 (wx.Panel)
        # LAYOUT:  Grid Bag Sizer
        panel5 = wx.Panel(panel2, wx.ID_ANY, style = self._borderStyle)
        panel5GridBagSizer = wx.GridBagSizer()
        panel5.SetSizer(sizer = panel5GridBagSizer)
        panel2VBoxSizer.Add(item = panel5, proportion = 1, flag = wx.EXPAND | wx.ALL, border = appSettings.BorderThickness * 2)
        
        # CONTROL: wx.StaticText
        panel3VBoxSizer.Add(item = wx.StaticText(parent = panel3, id = wx.ID_ANY, label = u"কিছু যুক্তাক্ষর"), proportion = 0, flag = wx.EXPAND | wx.ALL, border = appSettings.BorderThickness)
        
        # CONTROL: Panel7 (wx.Panel)
        # LAYOUT:  Grid Bag Sizer Layout
        panel7 = wx.Panel(parent = panel3, id = wx.ID_ANY, style = self._borderStyle)
        panel7GridBagSizer = wx.GridBagSizer()
        panel7.SetSizerAndFit(sizer = panel7GridBagSizer)
        panel3VBoxSizer.Add(item = panel7, proportion = 2, flag = wx.EXPAND | wx.ALL, border = appSettings.BorderThickness * 2)
        
        # CONTROL: wx.StaticText
        panel3VBoxSizer.Add(item = wx.StaticText(parent = panel3, id = wx.ID_ANY, label = u"সংখ্যা"), proportion = 0, flag = wx.EXPAND | wx.ALL, border = appSettings.BorderThickness)
        
        # CONTROL: Panel8 (wx.Panel)
        # LAYOUT:  Grid Bag Sizer Layout
        panel8 = wx.Panel(parent = panel3, id = wx.ID_ANY, style = self._borderStyle)
        panel8GridBagSizer = wx.GridBagSizer()
        panel8.SetSizerAndFit(sizer = panel8GridBagSizer)
        panel3VBoxSizer.Add(item = panel8, proportion = 1, flag = wx.EXPAND | wx.ALL, border = appSettings.BorderThickness * 2)
        
        # CONTROL: wx.StaticText
        panel3VBoxSizer.Add(item = wx.StaticText(parent =  panel3, id = wx.ID_ANY, label = u"অতিরিক্ত"), proportion = 0, flag = wx.EXPAND | wx.ALL, border = appSettings.BorderThickness)
        
        # CONTROL: Panel6 (wx.Panel)
        # LAYOUT:  Grid Bag Sizer Layout
        panel6 = wx.Panel(parent = panel3, id = wx.ID_ANY, style = self._borderStyle)
        panel6GridBagSizer = wx.GridBagSizer()
        panel6.SetSizerAndFit(sizer = panel6GridBagSizer)
        panel3VBoxSizer.Add(item = panel6, proportion = 1, flag = wx.EXPAND | wx.ALL, border = appSettings.BorderThickness * 2)

        """
        BengaliAlphabetButton(
            (Window)       parent,
            (long)         id,
            (String)       label,
            (GridBagSizer) sizer,
            (Point)        point,
            (Point)        span,
            (SearchCtrl)   control
        )
        """
        # Consonet
        kaButton            = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ক",  panel4GridBagSizer, wx.Point(0, 0), None, control)
        khaButton           = BengaliAlphabetButton(panel4, wx.ID_ANY, u"খ",  panel4GridBagSizer, wx.Point(0, 1), None, control)
        gaButton            = BengaliAlphabetButton(panel4, wx.ID_ANY, u"গ",  panel4GridBagSizer, wx.Point(0, 2), None, control)
        ghaButton           = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ঘ",  panel4GridBagSizer, wx.Point(0, 3), None, control)
        uumaButton          = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ঙ",  panel4GridBagSizer, wx.Point(0, 4), None, control)
        caButton            = BengaliAlphabetButton(panel4, wx.ID_ANY, u"চ",  panel4GridBagSizer, wx.Point(1, 0), None, control)
        chaButton           = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ছ",  panel4GridBagSizer, wx.Point(1, 1), None, control)
        zaButton            = BengaliAlphabetButton(panel4, wx.ID_ANY, u"জ",  panel4GridBagSizer, wx.Point(1, 2), None, control)
        zhaButton           = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ঝ",  panel4GridBagSizer, wx.Point(1, 3), None, control)
        neoButton           = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ঞ",  panel4GridBagSizer, wx.Point(1, 4), None, control)
        taButton            = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ট",  panel4GridBagSizer, wx.Point(2, 0), None, control)
        thaButton           = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ঠ",  panel4GridBagSizer, wx.Point(2, 1), None, control)
        daButton            = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ড",  panel4GridBagSizer, wx.Point(2, 2), None, control)
        dhaButton           = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ঢ",  panel4GridBagSizer, wx.Point(2, 3), None, control)
        muddhannaNaButton   = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ণ",  panel4GridBagSizer, wx.Point(2, 4), None, control)
        taaButton           = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ত",  panel4GridBagSizer, wx.Point(3, 0), None, control)
        thaaButton          = BengaliAlphabetButton(panel4, wx.ID_ANY, u"থ",  panel4GridBagSizer, wx.Point(3, 1), None, control)
        daaButton           = BengaliAlphabetButton(panel4, wx.ID_ANY, u"দ",  panel4GridBagSizer, wx.Point(3, 2), None, control)
        dhaaButton          = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ধ",  panel4GridBagSizer, wx.Point(3, 3), None, control)
        dantaNaButton       = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ন",  panel4GridBagSizer, wx.Point(3, 4), None, control)
        paButton            = BengaliAlphabetButton(panel4, wx.ID_ANY, u"প",  panel4GridBagSizer, wx.Point(4, 0), None, control)
        faButton            = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ফ",  panel4GridBagSizer, wx.Point(4, 1), None, control)
        baButton            = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ব",  panel4GridBagSizer, wx.Point(4, 2), None, control)
        vaButton            = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ভ",  panel4GridBagSizer, wx.Point(4, 3), None, control)
        maButton            = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ম",  panel4GridBagSizer, wx.Point(4, 4), None, control)
        hasantaButton       = BengaliAlphabetButton(panel4, wx.ID_ANY, u"্", panel4GridBagSizer, wx.Point(0, 5), wx.Point(5, 1), control)
        zaaButton           = BengaliAlphabetButton(panel4, wx.ID_ANY, u"য",  panel4GridBagSizer, wx.Point(0, 6), None, control)
        raButton            = BengaliAlphabetButton(panel4, wx.ID_ANY, u"র",  panel4GridBagSizer, wx.Point(0, 7), None, control)
        laButton            = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ল",  panel4GridBagSizer, wx.Point(0, 8), None, control)
        talobbaShaButton    = BengaliAlphabetButton(panel4, wx.ID_ANY, u"শ",  panel4GridBagSizer, wx.Point(1, 6), None, control)
        muddhannoShaButton  = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ষ",  panel4GridBagSizer, wx.Point(1, 7), None, control)
        dantaShaButton      = BengaliAlphabetButton(panel4, wx.ID_ANY, u"স",  panel4GridBagSizer, wx.Point(1, 8), None, control)
        haButton            = BengaliAlphabetButton(panel4, wx.ID_ANY, u"হ",  panel4GridBagSizer, wx.Point(2, 6), None, control)
        dayBinduRaButton    = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ড়",  panel4GridBagSizer, wx.Point(2, 7), None, control)
        dhayBinduRaButton   = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ঢ়",  panel4GridBagSizer, wx.Point(2, 8), None, control)
        ontosthoYoButton    = BengaliAlphabetButton(panel4, wx.ID_ANY, u"য়",  panel4GridBagSizer, wx.Point(3, 6), None, control)
        khandeTaaButton     = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ৎ",  panel4GridBagSizer, wx.Point(3, 7), None, control)
        onshkerButton       = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ং", panel4GridBagSizer, wx.Point(3, 8), None, control)
        bishorgoButton      = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ঃ", panel4GridBagSizer, wx.Point(4, 6), None, control)
        chandraBinduButton  = BengaliAlphabetButton(panel4, wx.ID_ANY, u"ঁ", panel4GridBagSizer, wx.Point(4, 7), None, control)
        
        # Vowel
        aAkarButton         = BengaliAlphabetButton(panel5, wx.ID_ANY, u"া",  panel5GridBagSizer, wx.Point(0,  0), None, control)
        rosshhoEekarButton  = BengaliAlphabetButton(panel5, wx.ID_ANY, u"ি",  panel5GridBagSizer, wx.Point(0,  1), None, control)
        dirghoEekarButton   = BengaliAlphabetButton(panel5, wx.ID_ANY, u"ী",  panel5GridBagSizer, wx.Point(0,  2), None, control)
        rosshUkarButton     = BengaliAlphabetButton(panel5, wx.ID_ANY, u"ু",  panel5GridBagSizer, wx.Point(0,  3), None, control)
        dirghoUukarButton   = BengaliAlphabetButton(panel5, wx.ID_ANY, u"ূ",  panel5GridBagSizer, wx.Point(0,  4), None, control)
        reekarButton        = BengaliAlphabetButton(panel5, wx.ID_ANY, u"ৃ",  panel5GridBagSizer, wx.Point(0,  5), None, control)
        aAKarButton         = BengaliAlphabetButton(panel5, wx.ID_ANY, u"ে",  panel5GridBagSizer, wx.Point(0,  6), None, control)
        oiKarButton         = BengaliAlphabetButton(panel5, wx.ID_ANY, u"ৈ",  panel5GridBagSizer, wx.Point(0,  7), None, control)
        okarButton          = BengaliAlphabetButton(panel5, wx.ID_ANY, u"ো", panel5GridBagSizer, wx.Point(0,  8), None, control)
        ouikarButton        = BengaliAlphabetButton(panel5, wx.ID_ANY, u"ৌ", panel5GridBagSizer, wx.Point(0,  9), None, control)
        shoreOButton        = BengaliAlphabetButton(panel5, wx.ID_ANY, u"অ",   panel5GridBagSizer, wx.Point(1,  0), None, control)
        shoreAaButton       = BengaliAlphabetButton(panel5, wx.ID_ANY, u"অা",  panel5GridBagSizer, wx.Point(1,  1), None, control)
        rosshoEButton       = BengaliAlphabetButton(panel5, wx.ID_ANY, u"ই",   panel5GridBagSizer, wx.Point(1,  2), None, control)
        dirghoEeButton      = BengaliAlphabetButton(panel5, wx.ID_ANY, u"ঈ",   panel5GridBagSizer, wx.Point(1,  3), None, control)
        rosshUButton        = BengaliAlphabetButton(panel5, wx.ID_ANY, u"উ",   panel5GridBagSizer, wx.Point(1,  4), None, control)
        dirghoUuButton      = BengaliAlphabetButton(panel5, wx.ID_ANY, u"ঊ",   panel5GridBagSizer, wx.Point(1,  5), None, control)
        reeButton           = BengaliAlphabetButton(panel5, wx.ID_ANY, u"ঋ",   panel5GridBagSizer, wx.Point(1,  6), None, control)
        aaButton            = BengaliAlphabetButton(panel5, wx.ID_ANY, u"এ",   panel5GridBagSizer, wx.Point(1,  7), None, control)
        oiBotton            = BengaliAlphabetButton(panel5, wx.ID_ANY, u"ঐ",   panel5GridBagSizer, wx.Point(1,  8), None, control)
        oBotton             = BengaliAlphabetButton(panel5, wx.ID_ANY, u"ও",   panel5GridBagSizer, wx.Point(1,  9), None, control)
        ouButton            = BengaliAlphabetButton(panel5, wx.ID_ANY, u"ঔ",   panel5GridBagSizer, wx.Point(1, 10), None, control)
        
        # Conjuncts
        khiyoButton               = BengaliAlphabetButton(panel7, wx.ID_ANY, u"ক্ষ",   panel7GridBagSizer, wx.Point(0,  0), None, control)
        uumaKButton               = BengaliAlphabetButton(panel7, wx.ID_ANY, u"ঙ্ক",   panel7GridBagSizer, wx.Point(0,  1), None, control)
        uumaGaButton              = BengaliAlphabetButton(panel7, wx.ID_ANY, u"ঙ্গ",   panel7GridBagSizer, wx.Point(0,  2), None, control)
        zaNeoButton               = BengaliAlphabetButton(panel7, wx.ID_ANY, u"জ্ঞ",   panel7GridBagSizer, wx.Point(1,  0), None, control)
        neoCaButton               = BengaliAlphabetButton(panel7, wx.ID_ANY, u"ঞ্চ",   panel7GridBagSizer, wx.Point(1,  1), None, control)
        neoChaButton              = BengaliAlphabetButton(panel7, wx.ID_ANY, u"ঞ্ছ",   panel7GridBagSizer, wx.Point(1,  2), None, control)
        neoZaButton               = BengaliAlphabetButton(panel7, wx.ID_ANY, u"ঞ্জ",   panel7GridBagSizer, wx.Point(2,  0), None, control)
        taaTaaButton              = BengaliAlphabetButton(panel7, wx.ID_ANY, u"ত্ত",   panel7GridBagSizer, wx.Point(2,  1), None, control)
        muddhannoShaDantaNaButton = BengaliAlphabetButton(panel7, wx.ID_ANY, u"ষ্ণ",  panel7GridBagSizer, wx.Point(2,  2), None, control)
        haMaButton                = BengaliAlphabetButton(panel7, wx.ID_ANY, u"হ্ম",   panel7GridBagSizer, wx.Point(3,  0), None, control)
        muddhannaNaDaButton       = BengaliAlphabetButton(panel7, wx.ID_ANY, u"ণ্ড",  panel7GridBagSizer, wx.Point(3,  1), None, control)
        
        # Number
        oneButton   = BengaliAlphabetButton(panel8, wx.ID_ANY, u"১",  panel8GridBagSizer, wx.Point(0,  0), None, control)
        twoButton   = BengaliAlphabetButton(panel8, wx.ID_ANY, u"২",  panel8GridBagSizer, wx.Point(0,  1), None, control)
        threeButton = BengaliAlphabetButton(panel8, wx.ID_ANY, u"৩",  panel8GridBagSizer, wx.Point(0,  2), None, control)
        fourButton  = BengaliAlphabetButton(panel8, wx.ID_ANY, u"৪",  panel8GridBagSizer, wx.Point(0,  3), None, control)
        fiveButton  = BengaliAlphabetButton(panel8, wx.ID_ANY, u"৫",  panel8GridBagSizer, wx.Point(0,  4), None, control)
        sixButton   = BengaliAlphabetButton(panel8, wx.ID_ANY, u"৬",  panel8GridBagSizer, wx.Point(1,  0), None, control)
        sevenButton = BengaliAlphabetButton(panel8, wx.ID_ANY, u"৭",  panel8GridBagSizer, wx.Point(1,  1), None, control)
        eightButton = BengaliAlphabetButton(panel8, wx.ID_ANY, u"৮",  panel8GridBagSizer, wx.Point(1,  2), None, control)
        nineButton  = BengaliAlphabetButton(panel8, wx.ID_ANY, u"৯",  panel8GridBagSizer, wx.Point(1,  3), None, control)
        zeroButton  = BengaliAlphabetButton(panel8, wx.ID_ANY, u"০",  panel8GridBagSizer, wx.Point(1,  4), None, control)
        
        # Extras
        zaaFolaButton = BengaliAlphabetButton(panel6, wx.ID_ANY, u"্য", panel6GridBagSizer, wx.Point(0,  0), None, control)
        raFolaButton  = BengaliAlphabetButton(panel6, wx.ID_ANY, u"্র", panel6GridBagSizer, wx.Point(0,  1), None, control)
        daariButton   = BengaliAlphabetButton(panel6, wx.ID_ANY, u"।",  panel6GridBagSizer, wx.Point(0,  2), None, control)
        bdtButton     = BengaliAlphabetButton(panel6, wx.ID_ANY, u"৳",   panel6GridBagSizer, wx.Point(0,  3), None, control)
        
