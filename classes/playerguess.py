from classes.gamemixins import GameMixins


class PlayerGuess(GameMixins):
    """
    This class gets player guesses
    and then processes the inputs
    """

    def __init__(self, word_length, word_container):
        self.word_container = word_container
        self.word_length = word_length
        self.correct_letters_container = ["_"] * word_length
        self.wrong_letters_container = []
        self.count = 0
        self.reset_signal = False
        self.get_player_guess()

    def get_player_guess(self):
        """
        Gets the plyer guess
        then it checks for its validity
        then it handovers the guessed letter
        to evaluate the guessed letters method
        """
        while True:
            if self.game_over(self.reset_signal):
                break
            try:
                self.letter_guessed = input("Please enter a letter:\n ")
                if self.letter_guessed.isalpha() and len(self.letter_guessed) == 1:
                    self.evaluate_guessed_letters()
                elif (
                    len(self.letter_guessed) > 1
                    and self.letter_guessed.isalpha() is True
                ):
                    print("\nPlease don't enter more than one letter.\n")
                else:
                    raise ValueError
            except ValueError:
                print("\nPlease Enter only ONE LETTER.")
                print("- No Special characters.")
                print("- No spaces.")
                print("- No numbers\n")
            except KeyboardInterrupt:
                print("\nCtrl C is not allowed!")

    def evaluate_guessed_letters(self):
        """
        Evaluates the player guess
        and it handovers the result to
        the respective method based
        on the guess correctness
        """

        if self.letter_guessed not in self.word_container:
            self.letter_is_wrong()
        else:
            self.letter_is_correct()

    def letter_is_wrong(self):
        """
        Checks if the letter is already guessed
        if not, it adds it to wrong letters storage
        then it hands over a counter
        to check if game lose occures
        """

        if self.letter_guessed in self.wrong_letters_container:
            print("You have already chosen this letter")
        else:
            self.wrong_letters_container.append(self.letter_guessed)
            print(f"This is the wrong_letter_container: {self.wrong_letters_container}")
        self.game_status()

    def letter_is_correct(self):
        """
        Checks if the letter is already guesssed
        if not, it adds it to the correct letters storage
        then it hands over a counter
        to check if game win occurs
        """

        if self.letter_guessed in self.correct_letters_container:
            print("You have already chosen this letter")
        else:
            for index, letter in enumerate(self.word_container):
                if self.letter_guessed == letter:
                    self.count += 1
                    self.correct_letters_container[index] = letter
            print("".join(self.correct_letters_container).upper())
        self.game_status()

    def game_status(self):
        """
        checks if win or lose occures
        if so, it announces
        the final game status
        """

        if len(self.wrong_letters_container) == self.word_length:
            print(
                f"\nAuch, you had {self.word_length} worng attempts. "
                f"\nThe correct word is {''.join(self.word_container).capitalize()}, "
                "you lost this time.\n"
            )
            self.reset_game()
            self.reset_signal = True
            self.game_over(self.reset_signal)
        elif self.count == self.word_length:
            print(
                "Great Job, you guessed the word!"
                f"\nThe correct word is {''.join(self.word_container).capitalize()}"
            )
            self.reset_game()
            self.reset_signal = True
            self.game_over(self.reset_signal)

    def game_over(self, reset_signal):
        if reset_signal:
            return True
        else:
            return False
