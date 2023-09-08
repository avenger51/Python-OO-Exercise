"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, file_path):
        self.words = []
        self.read_words_from_file(file_path)

    def read_words_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.words = file.read().splitlines()
                num_words = len(self.words)
                print(f"{num_words} words read")
        except FileNotFoundError:
            print("File not found.")

    def random(self):
        
        return random.choice(self.words)
    
# Example usage:
reader = WordFinder('words.txt')


#    # def read_file_list(filename):
#file = open("words.txt")
#
#for line in file:
#   print("line=", line)

#def random():
   #use the already 'read in' words?