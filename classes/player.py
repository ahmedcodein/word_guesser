import colorama
from classes.difficultyselection import DifficultySelection
from classes.gamemixins import GameMixins
from colorama import Fore

colorama.init(autoreset=True)


class Player(GameMixins):
    """
    Ask for user first name
    Check if the first name is not lengthy
    Check if the user gave a name, if not assume one
    """

    def __init__(self):
        self.name()

    def name(self):
        """
        The method for input the first name
        and for checking the name validity
        """
        self.name_err_msg = {
            "Long Name": None,
            "Spaces": None,
            "Numbers": None,
            "Non-alphabetic": None,
            "Ctrl C Key": None,
            "Ctrl D Key": None,
        }
        self.name_msg = f"""
            ---------------------------------------------------
            Please enter your first name:
            ---------------------------------------------------
            """
        print(self.name_msg)
        while True:
            for name_err_key, name_err_value in self.name_err_msg.items():
                self.name_err_msg[name_err_key] = None
            try:
                self.name = input().lower().strip("")
                if len(self.name) > 10:
                    self.name_err_msg["Long Name"] = "Please no more than 10 letters."
                elif any(i.isspace() for i in self.name):
                    self.name_err_msg["Spaces"] = "Please no empty name or spaces."
                elif any(i.isdigit() for i in self.name):
                    self.name_err_msg["Numbers"] = "Please only letters, no numbers."
                elif not any(i.isalpha() for i in self.name):
                    self.name_err_msg["Non-alphabetic"] = (
                        "Please only alphabetic letters."
                    )
                else:
                    self.welcome()
                    break
            except KeyboardInterrupt:
                self.name_err_msg["Ctrl C Key"] = "Ctrl C is not allowed!."
            self.display()

    def display(self):
        for name_err_key, name_err_value in self.name_err_msg.items():
            if name_err_value is not None:
                self.clear_screen()
                print(
                    f"""
            ---------------------------------------------------
            {Fore.RED}{name_err_value}
            {Fore.RESET}Please enter your first name again here:
            ---------------------------------------------------
                    """
                )

    def welcome(self):
        """
        Print out the welcome message with the first name
        """
        self.clear_screen()
        self.welcome = f"""
            ---------------------------------------------------
            Welcome {self.name.capitalize()}!
            ---------------------------------------------------
            """
        print(self.welcome)
        DifficultySelection(self.name)
