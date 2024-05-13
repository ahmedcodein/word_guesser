class PlayerGuess:
    """
    This class gets player guesses
    It converts the input letters into a list
    Then it returns the list for further 
    processing
    """

    def __init__(self, word_length, word_container):
        self.word_container = word_container
        self.word_length = word_length
        self.guessed_letters = []
        self.get_player_guess()

    def get_player_guess(self):
        """
        Get the plyer guess
        Check for its validity
        return a list of all the guessed letters
        """
        while True:
            try:
                self.player_letter_guessed = input("Please enter a letter:\n ")
                print(f"The length is {len(self.player_letter_guessed)}")
                if (
                    self.player_letter_guessed.isalpha()
                    and len(self.player_letter_guessed) == 1
                ):
                    print(self.player_letter_guessed)
                    self.guessed_letters.append(self.player_letter_guessed)
                    print(self.guessed_letters)
                    if len(self.guessed_letters) == self.word_length:
                        break
                elif (
                    len(self.player_letter_guessed) > 1
                    and self.player_letter_guessed.isalpha() is True
                ):
                    print("\nPlease don't enter more than one letter.\n")
                else:
                    raise ValueError
            except ValueError:
                print("\nPlease Enter only ONE LETTER.")
                print("- No Special characters.")
                print("- No spaces.")
                print("- No numbers\n")
