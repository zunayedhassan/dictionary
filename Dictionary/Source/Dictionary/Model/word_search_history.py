__author__ = 'Zunayed Hassan'

class WordSearchHistory():
    def __init__(self, wordIndex, originLanguage, translatedLanguage):
        self.WordIndex          = wordIndex
        self.OriginLanguage     = originLanguage
        self.TranslatedLanguage = translatedLanguage
        
    def __str__(self):
        return (str(self.WordIndex) + " " + str(self.OriginLanguage) + " " + str(self.TranslatedLanguage))