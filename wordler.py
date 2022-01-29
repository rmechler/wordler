import sys
from colorama import Fore
import random

UNUSED = Fore.LIGHTBLACK_EX
MISS = Fore.RED
HIT = Fore.LIGHTBLUE_EX
EXACT = Fore.GREEN

WORD_SIZE = 5

class Wordler(object):

    def __init__(self, word=None):
        self.all = [chr(x) for x in range(ord('a'), ord('z') + 1)]
        self.miss = []
        self.hit = []
        self.exact = []

        with open('resources/many-words.txt') as f:
            self.words = [word.strip() for word in f if len(word.strip()) == WORD_SIZE]

        if word:
            if word not in self.words:
                print("not a word")
                sys.exit(1)
        else:
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

        print(Fore.RESET)
        sys.stdout.flush()


    def guess(self, guess_word):

        if len(guess_word) != WORD_SIZE:
            return

        if guess_word not in self.words:
            print("not a word")
            return

        self.hit = []
        self.exact = []

        word = [c for c in self.word]

        for index, letter in enumerate(guess_word):
            if letter == word[index]:
                self.exact.append(letter)
                word[index] = None
                sys.stdout.write(EXACT + letter)
            elif letter in word:
                self.hit.append(letter)
                for i, c in enumerate(word):
                    if c == letter and guess_word[i] != letter:
                        word[i] = None
                sys.stdout.write(HIT + letter)
            else:
                self.miss.append(letter)
                sys.stdout.write(Fore.WHITE + '*')

        print(Fore.RESET)
        sys.stdout.flush()

        if guess_word == self.word:
            sys.exit(0)

        self.show()
