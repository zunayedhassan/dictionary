__author__ = 'Zunayed Hassan'

class WordDefinition():
    def __init__(self, title, wordDetails, grammaticalSyntax = u""):
        self.Title             = title
        self.GrammaticalSyntax = grammaticalSyntax
        self.WordDetails       = wordDetails