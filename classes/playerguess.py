from classes.gamemixins import GameMixins


class PlayerGuess(GameMixins):
    """
    This class gets player guesses
    and then processes the inputs
    """

    def __init__(self, name, dif_value, word_len, word):
        self.name = name
        self.dif_value = dif_value
        self.word = word
        self.word_len = word_len
        self.correct_lett = ["_"] * word_len
        self.wrong_lett = []
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
                self.guessed_lett = input(
                    "Please enter a letter:\n "
                    )
                if (self.guessed_lett.isalpha()
                   and len(self.guessed_lett)) == 1:
                    self.evaluate_guessed_letters()
                elif (
                    len(self.guessed_lett) > 1
                    and self.guessed_lett.isalpha() is True
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

        if self.guessed_lett not in self.word:
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

        if self.guessed_lett in self.wrong_lett:
            print("You have already chosen this letter")
        else:
            self.wrong_lett.append(self.guessed_lett)
            print(f"Wrong Guesses: {self.wrong_lett}")
        self.game_status()

    def letter_is_correct(self):
        """
        Checks if the letter is already guesssed
        if not, it adds it to the correct letters storage
        then it hands over a counter
        to check if game win occurs
        """

        if self.guessed_lett in self.correct_lett:
            print("You have already chosen this letter")
        else:
            for index, letter in enumerate(self.word):
                if self.guessed_lett == letter:
                    self.count += 1
                    self.correct_lett[index] = letter
            print(
                "Correct Guesses: "
                +
                "".join(self.correct_lett).upper()
                )
        self.game_status()

    def game_status(self):
        """
        checks if win or lose occures
        if so, it announces
        the final game status
        """

        if len(self.wrong_lett) == self.word_len:
            print(
                f"\nAuch, you had {self.word_len} worng attempts. "
                "\nThe correct word is "
                f"{''.join(self.word).capitalize()}. "
                "\nYou lost this time.\n"
            )
            self.reset_game()
            self.reset_signal = True
            self.game_over(self.reset_signal)
        elif self.count == self.word_len:
            print(
                "\nGreat Job, you guessed the word!"
                "\nThe correct word is "
                f"{''.join(self.word).capitalize()}."
            )
            self.reset_game()
            self.reset_signal = True
            self.game_over(self.reset_signal)

    def game_over(self, reset_signal):
        """
        It is used to signal a reset 
        is needed
        """
        if reset_signal:
            return True
        else:
            return False
