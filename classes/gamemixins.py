import os
from getch import pause


class GameMixins:
    """
    This class contains all mixins
    methods that can be used by other
    classes
    """

    def clear_screen(self):
        """
        The method clears the game screen
        """
        # The following 4 lines of code is taken from:
        # https://www.delftstack.com/howto/python/python-clear-console/
        # and https://github.com/dnlbowers/battleships
        command = "clear"
        if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
            command = "cls"
        os.system(command)

    def reset_game(self):
        """
        This method resets or exits the game 
        upon the player request
        """

        player_input = input(
            "\nWould you like to reset the game" "\nPlease type either yes or no "
        )
        if player_input == "yes":
            print("The game is reseting ... ")
            pause()
            self.clear_screen()
        else:
            exit()
