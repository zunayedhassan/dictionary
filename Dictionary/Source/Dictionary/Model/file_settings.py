__author__ = 'Zunayed Hassan'

import os, tempfile

class FileSettings():
    # Libray File Location
    EnWordListFile1              = "ee_eng_word_list.obj"
    EnToEnWordDefinitionListFile = "eng_to_eng_word_definition_list.obj"
    EnWordListFile2              = "eb_eng_word_list.obj"
    EnToBnWordDefinitionListFile = "eng_to_bn_word_definition_list.obj"
    BnWordListFile1              = "be_bn_word_list.obj"
    BnToEnWordDefinitionListFile = "bn_to_eng_word_definition_list.obj"
    BnWordListFile2              = "bb_bn_word_list.obj"
    BnToBnWordDefinitionListFile = "bn_to_bn_word_definition_list.obj"
    
    # Resource Location
    LibraryFileLocation          = "Resources/Library/"
    DictionaryConfigurationFile  = os.path.exists(os.path.expanduser(path = "~") + "/.dictionary_config.cfg") 