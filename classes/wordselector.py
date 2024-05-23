import random
from classes.playerguess import PlayerGuess


class WordSelector:
    """
    This class takes the difficulty level
    and the words's list and randomly selects
    a word for the player to guess
    """

    def __init__(self, name, dif_key, dif_value, word_bank):
        self.name = name
        self.dif_key = dif_key
        self.dif_value = dif_value
        self.word_bank = word_bank
        self.counter = len(word_bank) # Ensures a complete search
        self.difficulty_mapper()

    def difficulty_mapper(self):
        """
        The method maps the difficulty level
        to the length of the game word. Then
        it randomly selects the word from the
        word's bank with specified length
        """

        if self.dif_value == 1:
            self.word_len = 3
        elif self.dif_value == 2:
            self.word_len = 5
        else:
            self.word_len = 6
        while self.counter > 0:
            self.word = random.choice(self.word_bank)
            self.counter -= 1
            if len(self.word) == self.word_len:
                break
        PlayerGuess(self.name, self.dif_key, self.word_len, list(self.word))
