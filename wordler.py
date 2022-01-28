import sys
from colorama import Fore
import random

UNUSED = Fore.LIGHTBLACK_EX
MISS = Fore.RED
HIT = Fore.YELLOW
EXACT = Fore.GREEN

with open('resources/many-words.txt') as f:
    words = [word.strip() for word in f if len(word.strip()) == 5]

class Wordler(object):

    def __init__(self):
        self.all = [chr(x) for x in range(ord('a'), ord('z') + 1)]
        # self.unused = self.all[:]
        self.miss = []
        self.hit = []
        self.exact = []

        with open('resources/many-words.txt') as f:
            self.words = [word.strip() for word in f if len(word.strip()) == 5]

        self.word = random.choice(self.words)


    def show(self):
        for letter in self.all:
            if letter in self.miss:
                color = MISS
            elif letter in self.hit:
                color = HIT
            elif letter in self.exact:
                color = EXACT
            else:
                color = UNUSED
            sys.stdout.write(color + letter)
        print(Fore.WHITE)


    def guess(self, guess_word):
        if len(guess_word) != 5:
            return

        if guess_word not in self.words:
            print("not a word")
            return

        self.hit = []
        self.exact = []

        for index, letter in enumerate(guess_word):
            if letter == self.word[index]:
                self.exact.append(letter)
                sys.stdout.write(EXACT + letter)
            elif letter in self.word:
                self.hit.append(letter)
                sys.stdout.write(HIT + letter)
            else:
                self.miss.append(letter)
                sys.stdout.write(Fore.WHITE + '*')

        print(Fore.WHITE)

        if guess_word == self.word:
            sys.exit(0)

        self.show()
