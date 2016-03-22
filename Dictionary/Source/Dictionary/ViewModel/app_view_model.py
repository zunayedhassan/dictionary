__author__ = 'Zunayed Hassan'

import tempfile, pickle, os
from Model.app_settings_model import *

DictionaryConfigurationFileName = os.path.expanduser(path = "~") + "/.dictionary_config.cfg"

# FUNCTION NAME:    SaveOrCreateApplicationSettingsFile
# PARAMETER:        Model.ApplicationSettingsModel
# RETURN:           None
# PURPOSE:          Create 'dictionary_config.cfg'file with default values
def SaveOrCreateApplicationSettingsFile(settings = ApplicationSettingsModel()):
    fout = open(
                name = DictionaryConfigurationFileName,
                mode = "wb"
    )
    
    pickle.dump(
                obj = settings,
                file = fout
    )
    
    fout.close()

# FUNCTION NAME:    LoadApplicationSettings
# PARAMETER:        None
# RETURN:           Model.ApplicationSettingsModel()
# PURPOSE:          Load settings from 'dictionary_config.cfg'file and return them to the caller function.
def LoadApplicationSettings():
    fin = open(
               name = DictionaryConfigurationFileName,
               mode = "rb"
    )
    
    _appSettings = pickle.load(file = fin)
    
    fin.close()
    
    return _appSettings
    