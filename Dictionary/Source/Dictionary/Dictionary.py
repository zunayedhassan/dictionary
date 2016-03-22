"""
APPLICATION NAME: Dictionary
VERSION:          1.0
LICENSE:          GNU GPL 2
DESCRIPTION:      A simple English to English, English to Bengali,
                  Bengali  to  English  and  Bengali  to  Bengali
                  Dictionary.

TARGET PLATFORM:  Windows, Linux, Mac OS
INTERFACE:        GUI
FRAMEWORK:        wxPython

AUTHOR:           Mohammod Zunayed Hassan
EMAIL:            zunayed-hassan@live.com
"""


from View import *

if __name__ == "__main__":
    app = DictionaryApplication()
    app.MainLoop()
    