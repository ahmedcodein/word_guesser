import colorama
import os
from getch import pause
from colorama import Fore
from classes.player import Player
from classes.gamemixins import GameMixins
colorama.init(autoreset=True)


class InitiateGame(GameMixins):
    """
    Intiate the game by a welcome message and instructions
    Then clear the screen upon user order
    Intiate the Player class
    """

    def __init__(self):
        self.general_welcome()

    def general_welcome(self):
        """
       Diplays a welcome message
        """
        self.clear_screen()
        self.general_welcome = Fore.LIGHTCYAN_EX + """

            ██╗    ███████████╗     ██████╗██████╗███╗   ██████████╗
            ██║    ████╔════██║    ██╔════██╔═══██████╗ ██████╔════╝
            ██║ █╗ ███████╗ ██║    ██║    ██║   ████╔████╔███████╗
            ██║███╗████╔══╝ ██║    ██║    ██║   ████║╚██╔╝████╔══╝
            ╚███╔███╔██████████████╚██████╚██████╔██║ ╚═╝ █████████╗
            ╚══╝╚══╝╚══════╚══════╝╚═════╝╚═════╝╚═╝     ╚═╚══════╝
            ████████╗██████╗     ██╗    ██╗██████╗██████╗██████╗
            ╚══██╔══██╔═══██╗    ██║    ████╔═══████╔══████╔══██╗
               ██║  ██║   ██║    ██║ █╗ ████║   ████████╔██║  ██║
               ██║  ██║   ██║    ██║███╗████║   ████╔══████║  ██║
               ██║  ╚██████╔╝    ╚███╔███╔╚██████╔██║  ████████╔╝
               ╚═╝   ╚═════╝      ╚══╝╚══╝ ╚═════╝╚═╝  ╚═╚═════╝
             ██████╗██╗   ████████████████████████████████████╗
            ██╔════╝██║   ████╔════██╔════██╔════██╔════██╔══██╗
            ██║  █████║   ███████╗ ███████████████████╗ ██████╔╝
            ██║   ████║   ████╔══╝ ╚════██╚════████╔══╝ ██╔══██╗
            ╚██████╔╚██████╔██████████████████████████████║  ██║
             ╚═════╝ ╚═════╝╚══════╚══════╚══════╚══════╚═╝  ╚═╝
        """
        print(self.general_welcome)
        pause()
        self.intructions()

    def intructions(self):
        """
        Display the game rules and instructions
        then pause and wait for the user action to proceed
        """
        self.clear_screen()
        instructions_rules = Fore.LIGHTCYAN_EX + """

                            GAME INSTRUCTIONS
        ########################################################

                - Your job is to guess an English word
                  by entering its letters one by one.

                - You have three difficulty levels to
                  choose from:

                    # Easy for 3-letter words
                    # Intermediate for 5-letter words
                    # Difficult for 6-letter words

                - Based on the difficulty level, you will
                  have:

                    # 3 or 5 or 6 chances respectively.

                Have fun!
        """
        print(instructions_rules)
        pause()
        Player()
