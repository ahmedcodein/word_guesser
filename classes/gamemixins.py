import os
from colorama import Fore


class GameMixins:
    """
    This class contains all the game
    mixin methods used by other
    classes
    """
    @staticmethod
    def clear_screen():
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

    @staticmethod
    def words_bank():
        """
        This method contains a list
        of all the game words
        """
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
        self.msgs = {
            "Restart Message": "Restart the game? yes/no?",
            "Value Error": None,
            "Ctrl C Key": None,
            "Ctrl D Key": None,
        }
        print(
            f"""
            ---------------------------------------------------
            {self.msgs["Restart Message"]}
            ---------------------------------------------------
            """
        )
        while True:
            for msg_key in self.msgs.keys():
                self.msgs[msg_key] = None
            try:
                player_input = input().lower().strip("")
                if player_input == "yes" or player_input == "y":
                    break
                elif player_input == "no" or player_input == "n":
                    self.clear_screen()
                    print(Fore.LIGHTCYAN_EX + """

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
                self.msgs["Value Error"] = f"{Fore.RED}Not a valid input!"
            except KeyboardInterrupt:
                self.msgs["Ctrl C Key"] = f"{Fore.RED}Ctrl C is not allowed!"
            except EOFError:
                self.msgs["Ctrl D Key"] = f"{Fore.RED}Ctrl D is not allowed!"
            for msg_value in self.msgs.values():
                if msg_value is not None:
                    self.clear_screen()
                    print(
                        f"""
            ---------------------------------------------------
            {msg_value}{Fore.RESET}
            Please type:
            - 'Yes' for resetting the game.
            - 'No' for leaving the game.
            ---------------------------------------------------
                    """
                    )
