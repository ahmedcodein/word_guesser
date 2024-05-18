from classes.wordsbank import WordBank
from classes.wordselector import WordSelector


class DifficultySelection:
    """
    Present the user the three game difficulty options
    Get the choice from the user
    """

    def __init__(self):
        self.game_main_loop()

    def game_main_loop(self):
        while True:
            self.message = print(
            "Please enter either 1 or 2 or 3 for the difficulty level:\n\n"
            "1. Easy\n"
            "2. Intermediate\n"
            "3. Difficult\n"
            )
            self.difficulty_level = {"easy": 1, "intermediate": 2, "difficult": 3}
            self.get_difficulty_level()

    def get_difficulty_level(self):
        """
        Allow the user to input the difficulty choice
        Check if the user input is valid
        If input is not valid, raise the error to the user
        If the input is valid, display the user choice
        Go to the WordSelector
        """
        while True:
            try:
                self.difficulty_level_choice = int(
                    input("Please enter you choice here: " "\n")
                )
                loop = True
                for key, value in self.difficulty_level.items():
                    if value == self.difficulty_level_choice and loop == True:
                        print(
                            f"\nyou choose {key.capitalize()} as the difficulty level!\n"
                        )
                        WordSelector(value, WordBank().words)
                        loop = False
                        return loop
                    elif (
                        self.difficulty_level_choice
                        not in self.difficulty_level.values()
                    ):
                        raise ValueError
                    else:
                        continue

            except ValueError:
                print("\nInvalid choice, please enter either 1,2 or 3:\n")
