import random


class WordSelector:
    """
    This class takes the difficulty level and the list of words
     and randomly select a word for the user to guess accordingly
    """

    def __init__(self, difficulty_level, word_list):
        self.difficulty_level = difficulty_level
        self.word_list = word_list
        self.counter = len(word_list)
        self.difficulty_mapper()

    def difficulty_mapper(self):
        """
        The method maps the difficulty level
        to the length of word.
        and then randomly select the word from the list
        with specified length
        """

        if self.difficulty_level == 1:
            self.word_length = 3
        elif self.difficulty_level == 2:
            self.word_length = 5
        else:
            self.word_length = 6
        while self.counter > 0:
            self.word_container = random.choice(self.word_list)
            self.counter -= 1
            if len(self.word_container) == self.word_length:
                print(f'"Only for TEST", the random word is: {self.word_container}')
                return self.word_container
