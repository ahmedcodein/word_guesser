import os
import time
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

    def words_bank(self):
        return [
            "cat",
            "dog",
            "sun",
            "sky",
            "red",
            "run",
            "fun",
            "car",
            "bat",
            "mat",
            "box",
            "boy",
            "owl",
            "ant",
            "bee",
            "cow",
            "fox",
            "pie",
            "hat",
            "jar",
            "map",
            "mud",
            "pen",
            "pig",
            "rat",
            "wax",
            "yak",
            "zip",
            "rug",
            "wet",
            "urn",
            "tea",
            "leg",
            "jug",
            "jam",
            "ice",
            "gem",
            "fan",
            "egg",
            "dip",
            "cut",
            "bay",
            "arc",
            "age",
            "dye",
            "elm",
            "fit",
            "gum",
            "hen",
            "ink",
            "apple",
            "bread",
            "crisp",
            "dairy",
            "eagle",
            "fruit",
            "grape",
            "house",
            "ivory",
            "joker",
            "knife",
            "lemon",
            "mango",
            "night",
            "olive",
            "piano",
            "queen",
            "river",
            "sugar",
            "train",
            "umbra",
            "vocal",
            "whale",
            "xenon",
            "yacht",
            "zebra",
            "alarm",
            "beach",
            "cliff",
            "draft",
            "elbow",
            "flint",
            "ghost",
            "heart",
            "ideal",
            "judge",
            "kneel",
            "light",
            "moral",
            "nerve",
            "opera",
            "proud",
            "quest",
            "robin",
            "sheep",
            "tiger",
            "uncle",
            "value",
            "wreck",
            "youth",
            "beauty",
            "bubble",
            "candle",
            "damage",
            "effort",
            "frozen",
            "guitar",
            "hammer",
            "island",
            "jungle",
            "kitten",
            "liquid",
            "magnet",
            "number",
            "orange",
            "purple",
            "quartz",
            "ribbon",
            "sphere",
            "temple",
            "united",
            "violet",
            "wallet",
            "xylene",
            "yellow",
            "zipper",
            "answer",
            "branch",
            "circle",
            "danger",
            "effect",
            "flight",
            "growth",
            "heaven",
            "injury",
            "jockey",
            "kernel",
            "lumber",
            "moment",
            "needle",
            "object",
            "puzzle",
            "quiver",
            "record",
            "silver",
            "turtle",
            "update",
            "vision",
            "wonder",
            "yonder",
        ]


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
                    self.clear_screen()
                    time.sleep(1)
                    print("The Game is reseting ... ")
                    time.sleep(1)
                    print("The Game is reset!")
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
