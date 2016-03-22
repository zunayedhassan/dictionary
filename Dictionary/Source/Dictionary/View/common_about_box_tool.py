__author__ = 'Zunayed Hassan'

import wx
import wx.lib.scrolledpanel as scrolled
from Model.about_box_info import *

class VersionPanel(wx.Panel):
    def __init__(self, parent, id, aboutBoxInfo, appSettings):
        wx.Panel.__init__(self, parent, id, wx.DefaultPosition, wx.DefaultSize)
        
        versionPanelVBoxSizer = wx.BoxSizer(orient = wx.VERTICAL)
        self.SetSizer(sizer = versionPanelVBoxSizer)
        
        icon = wx.Bitmap(
            name = aboutBoxInfo.Icon,
            type = wx.BITMAP_TYPE_PNG
        )
        
        applicationIcon = wx.StaticBitmap(
            parent = self,
            id     = wx.ID_ANY,
            bitmap = self.ScaleBitmap(bitmap = icon, width = 64, height = 64)
        )
        
        versionPanelVBoxSizer.Add(
            item       = applicationIcon,
            proportion = 0,
            flag       = wx.ALL | wx.CENTER,
            border     = appSettings.BorderThickness * 3
        )
        
        applicationTitleText = wx.StaticText(
            parent     = self,
            id         = wx.ID_ANY,
            label      = aboutBoxInfo.ApplicationName
        )
        
        applicationTitleText.SetFont(
            font = wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        )
        
        versionPanelVBoxSizer.Add(
            item       = applicationTitleText,
            proportion = 0,
            flag       = wx.ALL | wx.CENTER,
            border     = appSettings.BorderThickness
        )
        
        applicationVersionText = wx.StaticText(
            parent     = self,
            id         = wx.ID_ANY,
            label      = "Version: " + aboutBoxInfo.Version
        )
        
        applicationVersionText.SetFont(
            font = wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL)
        )
        
        versionPanelVBoxSizer.Add(
            item       = applicationVersionText,
            proportion = 0,
            flag       = wx.ALL | wx.CENTER,
            border     = appSettings.BorderThickness
        )
        
        appDescText = wx.StaticText(
            parent     = self,
            id         = wx.ID_ANY,
            label      = aboutBoxInfo.AppDesc,
            style      = wx.TE_CENTER
        )
        
        versionPanelVBoxSizer.Add(
            item       = appDescText,
            proportion = 0,
            flag       = wx.ALL | wx.CENTER,
            border     = appSettings.BorderThickness * 3
        )
        
        
    def ScaleBitmap(self, bitmap, width, height):
        image = wx.ImageFromBitmap(bitmap)
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.BitmapFromImage(image)
        
        return result
    
    
class LicensePanel(wx.Panel):
    def __init__(self, parent, id, aboutBoxInfo, appSettings):
        wx.Panel.__init__(self, parent, id, wx.DefaultPosition, wx.DefaultSize)
        
        licensePanelVBoxSizer = wx.BoxSizer(orient = wx.VERTICAL)
        self.SetSizer(sizer = licensePanelVBoxSizer)
        
        licenseTextCtrl = wx.TextCtrl(parent = self, id = wx.ID_ANY, style = wx.TE_MULTILINE)
        licenseTextCtrl.SetEditable(editable = False)
        
        licenseFile = open(name = aboutBoxInfo.License, mode = "r")
        license = licenseFile.read()
        licenseFile.close()
        
        licenseTextCtrl.SetValue(license)
        licenseTextCtrl.SetFont(
            font = wx.Font(8, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        )
        
        licensePanelVBoxSizer.Add(
            item       = licenseTextCtrl,
            proportion = 1,
            flag       = wx.ALL | wx.EXPAND,
            border     = appSettings.BorderThickness
        )
        
 
class CreditsPanel(scrolled.ScrolledPanel):
    def __init__(self, parent, id, aboutBoxInfo, appSettings):
        scrolled.ScrolledPanel.__init__(self, parent, id, wx.DefaultPosition, wx.DefaultSize)
        
        creditsPanelVBoxSizer = wx.BoxSizer(orient = wx.VERTICAL)
        self.SetSizer(sizer = creditsPanelVBoxSizer)
        
        self.SetAutoLayout(1)
        self.SetupScrolling()
        
        for authorsList in aboutBoxInfo.AuthorsList:
            contributionText = wx.StaticText(
                parent = self,
                id     = wx.ID_ANY,
                label  = authorsList.Contribution
            )
            
            contributionText.SetFont(
                font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 
            )
            
            creditsPanelVBoxSizer.Add(
                item       = contributionText,
                proportion = 0,
                flag       = wx.TOP | wx.CENTER,
                border     = appSettings.BorderThickness * 12
            )
            
            for author in authorsList.Authors:
                authorInfoPanel = wx.Panel(parent = self, id = wx.ID_ANY)
                authorInfoPanelVBoxSizer = wx.BoxSizer(orient = wx.VERTICAL)
                authorInfoPanel.SetSizer(sizer = authorInfoPanelVBoxSizer)
                
                if (author.Website != None):
                    self.name = wx.HyperlinkCtrl(
                            parent = authorInfoPanel,
                            id     = wx.ID_ANY,
                            label  = author.Name,
                            url    = author.Website
                    )
                else:
                    self.name = wx.StaticText(
                            parent = authorInfoPanel,
                            id     = wx.ID_ANY,
                            label  = author.Name
                    )
                    
                authorInfoPanelVBoxSizer.Add(
                    item       = self.name,
                    proportion = 1,
                    flag       = wx.ALL | wx.CENTER
                )
                
                if (author.Email != None):
                    self.email = wx.HyperlinkCtrl(
                            parent = authorInfoPanel,
                            id     = wx.ID_ANY,
                            label  = author.Email,
                            url    = "mailto:" + author.Email
                    )
                    
                    authorInfoPanelVBoxSizer.Add(
                        item       = self.email,
                        proportion = 1,
                        flag       = wx.ALL | wx.CENTER,
                    )
                
                creditsPanelVBoxSizer.Add(
                    item       =  authorInfoPanel,
                    proportion = 0,
                    flag       = wx.ALL | wx.CENTER,
                    border     = appSettings.BorderThickness
                )