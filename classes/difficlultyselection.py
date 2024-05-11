from classes.wordsbank import WordBank
from classes.wordselector import WordSelector


class DifficultySelection:
    """
    Present the user the three game difficulty options
    Get the choice from the user
    """

    def __init__(self):
        self.message = print(
            "Please enter 1 or 2 or 3 for the difficulty level:\n\n 1. Easy\n 2. Intermediate\n 3. Difficult\n"
        )
        self.difficulty_level = None
        self.easy = "easy"
        self.intermediate = "intermediate"
        self.difficult = "difficult"
        self.display_difficulty_level()

    def display_difficulty_level(self):
        """
        Display the difficulty options
        Check if the user input are valid
        If input is not valid, raise the error to the user
        If the input is valid, display the user choice
        """
        while True:
            try:
                self.difficulty_level = int(input())
                if self.difficulty_level == 1:
                    print(
                        f"\nyou choose {self.easy.capitalize()} as the difficulty level\n"
                    )
                elif self.difficulty_level == 2:
                    print(
                        f"\nyou choose {self.intermediate.capitalize()} as the difficulty level\n"
                    )
                elif self.difficulty_level == 3:
                    print(
                        f"\nyou choose {self.difficult.capitalize()} as the difficulty level\n"
                    )
                WordSelector(self.difficulty_level, WordBank().words)
                return self.difficulty_level

            except ValueError:
                print("Invalid choice number, please enter either 1,2 or 3:")
