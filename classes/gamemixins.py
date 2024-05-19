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
        # If Machine is running on Windows, use cls
        if os.name in ("nt", "dos"):
            command = "cls"
        os.system(command)

    def reset_game(self):
        """
        This method resets or exits the game
        upon the player request
        """
        print(
            "\nWould you like to reset the game? "
            "\nPlease type either yes or no: "
            )
        loop = True
        while True:
            if not loop:
                break
            try:
                player_input = input().lower().strip("")
                if player_input == "yes" or player_input == "y":
                    print("The game is reseting ... ")
                    pause()
                    self.clear_screen()
                    loop = False
                    return loop
                elif player_input == "no" or player_input == "n":
                    self.clear_screen()
                    print(
                        """
                         ██████╗ ██████╗ ██████╗██████╗
                        ██╔════╝██╔═══████╔═══████╔══██╗
                        ██║  █████║   ████║   ████║  ██║
                        ██║   ████║   ████║   ████║  ██║
                        ╚██████╔╚██████╔╚██████╔██████╔╝
                         ╚═════╝ ╚═════╝ ╚═════╝╚═════╝
                        ██████╗██╗   █████████╗
                        ██╔══██╚██╗ ██╔██╔════╝
                        ██████╔╝╚████╔╝█████╗
                        ██╔══██╗ ╚██╔╝ ██╔══╝
                        ██████╔╝  ██║  ███████╗
                        ╚═════╝   ╚═╝  ╚══════╝
                        """
                    )
                    exit()
                else:
                    raise ValueError
            except ValueError:
                print(
                    "\nNot a valid input!\n"
                    "Please type: "
                    "'yes' for reset "
                    ", 'no' for leaving the game."
                )
            except KeyboardInterrupt:
                print(
                    "\nCtrl C is not allowed!\n"
                    "Please type: "
                    "'yes' for reset "
                    ", 'no' for leaving the game."
                )
