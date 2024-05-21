import random
from classes.playerguess import PlayerGuess


class WordSelector:
    """
    This class takes the difficulty level and the list of words
     and randomly select a word for the user to guess accordingly
    """

    def __init__(self, name, difficulty_key, difficulty_value, word_bank):
        self.name = name
        self.difficulty_key = difficulty_key
        self.difficulty_value = difficulty_value
        self.word_bank = word_bank
        self.counter = len(word_bank)
        self.difficulty_mapper()

    def difficulty_mapper(self):
        """
        The method maps the difficulty level
        to the length of word.
        and then randomly select the word from the list
        with specified length
        """

        if self.difficulty_value == 1:
            self.word_length = 3
        elif self.difficulty_value == 2:
            self.word_length = 5
        else:
            self.word_length = 6
        while self.counter > 0:
            self.word_container = random.choice(self.word_bank)
            self.counter -= 1
            if len(self.word_container) == self.word_length:
                break
        print(f"You have {self.word_length} chances before you lose!\n")
        PlayerGuess(self.name, self.difficulty_value, self.word_length, list(self.word_container))
