from classes.wordselector import WordSelector
from classes.gamemixins import GameMixins
from getch import pause


class DifficultySelection(GameMixins):
    """
    Presents the user the three game difficulty options
    Get the choice from the user
    """

    def __init__(self, name):
        self.dif_level_msgs = {
            "Difficulty Levels": None,
            "Player Choice": None,
            "Value Error": None,
            "Ctrl C key": None,
            "Ctrl D key": None
        }
        self.name = name
        self.game_main_loop()

    def game_main_loop(self):
        """
        Presets the three difficulty levels
        to the player
        It loops inifintly as long as the player
        keep reseting the game
        """

        while True:

            self.dif_levels = {"easy": 1, "intermediate": 2, "difficult": 3}
            self.dif_level_msgs[
                "Difficulty Levels"
            ] = f"""
            ---------------------------------------------------
            Please type either 1, 2 or 3 for the
            difficulty level:
                1. Easy
                2. Intermediate
                3. Difficult
            ---------------------------------------------------
            """
            print(self.dif_level_msgs["Difficulty Levels"])
            self.get_dif_level()

    def get_dif_level(self):
        """
        Allow the user to input the difficulty choice
        Check if the user input is valid
        If input is not valid, raise the error to the user
        If the input is valid, display the user choice
        Go to the WordSelector
        """
        while True:
            for dif_key, dif_value in self.dif_level_msgs.items():
                self.dif_level_msgs[dif_key] = None
            try:
                self.dif_level_choice = int(input())
                loop = True
                for dif_key, dif_value in self.dif_levels.items():
                    if dif_value == self.dif_level_choice and loop is True:
                        self.dif_level_msgs["Player Choice"] = (
                            f"You chose the '{dif_key.capitalize()}' level!"
                        )
                        self.display()
                        pause()
                        WordSelector(self.name, dif_key, dif_value,
                                     self.words_bank())
                        loop = False
                        return loop
                    elif self.dif_level_choice not in self.dif_levels.values():
                        raise ValueError
                    else:
                        continue
            except ValueError:
                self.dif_level_msgs["Value Error"] = (
                    "Invalid choice, Please type either 1, 2 or 3"
                )
                self.display()
            except KeyboardInterrupt:
                self.dif_level_msgs["Ctrl C key"] = (
                    "Ctrl C is not allowed! Please type either 1, 2 or 3"
                )
                self.display()

    def display(self):
        for dif_key, dif_value in self.dif_level_msgs.items():
            if dif_value is not None:
                print(
                    f"""
            ---------------------------------------------------
            {dif_value}
            ---------------------------------------------------
                    """
                )
