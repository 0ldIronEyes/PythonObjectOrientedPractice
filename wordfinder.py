"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """ Reads a file that contains a list of words, and chooses a random word from that list"""
    
    def __init__(self, filepath):
        """  create a WordFinder with a list called words, that contains lines from file that was passed in"""
        file = open(filepath)
        self.words = self.getLines(file)
        print(f"{len(self.words)} words read")


    def getLines(self, lines):
        """ iterate through lines and adds to list"""
        readwords = []
        for line in lines:
            readwords.append = line.strip()
        return readwords
       

    def random(self):
        """ gets a random word from words list"""
        return random.choice(self.words)
    

class SpecialWordFinder(WordFinder):
    """ Reads a file that contains a list of words, and chooses a random word from that list, ignoring lines that start with # character."""


    def getLines(self, lines):
        """ iterates through lines and adds to list if word doesn't start with #"""
        readwords = []
        for line in lines:
            if line.strip() and not line.startswith("#"):
               readwords.append = line.strip()
        return readwords