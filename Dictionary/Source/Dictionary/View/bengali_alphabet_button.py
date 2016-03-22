__author__ = 'Zunayed Hassan'

import wx

class BengaliAlphabetButton(wx.Button):
    """
    CONSTRUCTOR:    BengaliAlphabetButton(
                        (Window)       parent,
                        (long)         id,
                        (String)       label,
                        (GridBagSizer) sizer,
                        (Point)        point,
                        (Point)        span,
                        (SearchCtrl)   control
                    )
    """
    def __init__(self, parent, id, label, sizer, position, span, control):
        wx.Button.__init__(self, parent, id, label, size = wx.Size(30, 30))
        
        if (span == None):
            sizer.Add(self, (position.x, position.y), wx.DefaultSpan,   wx.EXPAND | wx.ALL, 2)
        else:
            sizer.Add(self, (position.x, position.y), (span.x, span.y), wx.EXPAND | wx.ALL, 2)
            
        self.SetFont(font = wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        
        sizer.AddGrowableRow(position.x)
        sizer.AddGrowableCol(position.y)
        
        self.Control = control
        
        # EVENT FOR: self
        self.Bind(wx.EVT_BUTTON, self.OnClicked, id = self.GetId())
        

    # METHOD NAME:    OnClicked
    # PARAMETER:      Event
    # RETURN:         None
    # PURPOSE:        To set bengali alphabet on control
    def OnClicked(self, event):
        self.Control.SetValue(self.Control.GetValue() + self.GetLabel())
        
        