#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'Zunayed Hassan'

import zlib, tempfile, pickle, re
from Model.file_settings import *
from Model.library import *
from Model.word_definition import *
from Model.word_search_history import *

currentLibrary = Library()
CurrentWordSearchHistory = []


# FUNCTION NAME:    GetLibrary
# PARAMETER:        (string []) wordList, (WordDefinition []) wordDef
# RETURN:           Library
# PURPOSE:          Read word list and word definition from file and return them as library 
def GetLibrary(wordList, wordDef):
    # 1. Decompress word list file
    # 2. Load word list from that decompressed file
    Decompress(
               input_filename  = FileSettings.LibraryFileLocation + wordList + ".gz",
               output_filename = tempfile.gettempdir() + "/" + wordList
    )
    
    LoadWordList(wordListFile = wordList)
    
    # 1. Decompress word definition file
    # 2. Load word definition list from that decompressed file
    Decompress(
               input_filename  = FileSettings.LibraryFileLocation + wordDef + ".gz",
               output_filename = tempfile.gettempdir() + "/" + wordDef
    )
    
    LoadWordDefinitionList(wordDefinitionFile = wordDef)
    
    return currentLibrary
    
# FUNCTION NAME:    Decompress
# PARAMETER:        (String) input_filename, (String) output_filename
# RETURN:           None
# PURPOSE:          Extract from *.gz file
def Decompress(input_filename, output_filename):
    fin = open(input_filename, "rb")
    decompressedData = zlib.decompress(fin.read(), 16+zlib.MAX_WBITS)
    fin.close()

    fout = open(output_filename, "wb")
    fout.write(decompressedData)
    fout.close()
    
# FUNCTION NAME:    LoadWordList
# PARAMETER:        (String []) wordListFile
# RETURN:           None
# PURPOSE:          To load list of words in memory from file
def LoadWordList(wordListFile):
    fin = open(tempfile.gettempdir() + "/" + wordListFile, "rb")
    currentLibrary.WordList = pickle.load(fin)
    fin.close()
    
# FUNCTION NAME:    LoadWordDefinitionList
# PARAMETER:        (String) WordDefinitionFile
# RETURN:           None
# PURPOSE:          To load list of word definitions into file
def LoadWordDefinitionList(wordDefinitionFile):
    fin = open(tempfile.gettempdir() + "/" + wordDefinitionFile, "rb")
    currentLibrary.WordDefinitionList = pickle.load(fin)
    fin.close()

# FUNCTION NAME:    Search
# PARAMETER:        (String) keyword
# RETURN:           (integer) index OR None
# PURPOSE:          Search from word list by given keyword
def Search(keyword):
    pattern = ("^" + keyword)
    index = 0

    for word in currentLibrary.WordList:
        result = re.findall(
                    pattern = pattern,
                    string = word,
                    flags = re.IGNORECASE | re.UNICODE
        )
            
        if (result != []):
            return index
            
        index += 1
        
    return None


# FUNCTION NAME:    SaveWordSearchHistory
# PARAMETER:        (Model.WordSearchHistory) wordSearchHistory
# RETURN:           None
# PURPOSE:          Save to 'word search history' list
def SaveWordSearchHistory(wordSearchHistory):
    CurrentWordSearchHistory.append(wordSearchHistory)
    
    