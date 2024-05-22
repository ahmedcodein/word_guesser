import colorama
from classes.gamemixins import GameMixins
from colorama import Fore

colorama.init(autoreset=True)


class PlayerGuess(GameMixins):
    """
    This class represents the core
    of the game.
    from getting the player guess till
    resetting or exiting the game
    """

    def __init__(self, name, dif_value, word_len, word):
        self.name = name
        self.dif_value = dif_value
        self.word = word
        self.word_len = word_len
        self.correct_lett = ["_"] * word_len
        self.wrong_lett = []
        self.count = 0
        self.game_msgs = {
            "Multiple Letters": None,
            "Correct Letter": None,
            "Wrong Letter": None,
            "Lost Message": None,
            "Won Message": None,
            "Value Error": None,
            "Ctrl C key": None,
            "Ctrl D key": None,
        }
        self.reset_signal = False
        self.clear_screen()
        self.game_dashboard()
        self.get_player_guess()

    def get_player_guess(self):
        """
        Gets the plyer guess
        then it checks for its validity
        then it handovers the guessed letter
        to evaluate-guessed-letters method
        """
        while True:
            for msg_key in self.game_msgs.keys():
                self.game_msgs[msg_key] = None
            if self.game_over(self.reset_signal):
                break
            try:
                self.guessed_lett = input("Please enter a letter:\n ")
                if (self.guessed_lett.isalpha()
                   and len(self.guessed_lett)) == 1:
                    self.evaluate_guessed_letters()
                else:
                    raise ValueError
            except ValueError:
                value_err_msg = "Please enter ONLY ONE and Valid LETTER."
                self.game_msgs["ValueError"] = Fore.LIGHTRED_EX + value_err_msg
            except KeyboardInterrupt:
                ctrl_c_msg = "Ctrl C is not allowed!"
                self.game_msgs["Ctrl C key"] = Fore.LIGHTRED_EX + ctrl_c_msg
            self.clear_screen()
            self.game_dashboard()

    def evaluate_guessed_letters(self):
        """
        Evaluates the player guess
        then it handovers the result to
        the respective method based
        on the guess correctness
        """

        if self.guessed_lett not in self.word:
            self.letter_is_wrong()
        else:
            self.letter_is_correct()

    def letter_is_wrong(self):
        """
        Checks if the letter is already guessed
        if not, it adds it to wrong letters storage
        then it hands over game status
        to check if game lose occurs
        """

        if self.guessed_lett in self.wrong_lett:
            duplication_msg = "You have already chosen this letter"
            self.game_msgs["Multiple Letters"] = (Fore.LIGHTYELLOW_EX +
                                                  duplication_msg)
        else:
            self.wrong_lett.append(self.guessed_lett)
            self.game_msgs["Wrong Letter"] = (
                Fore.RED + "You have chosen the wrong letter"
            )
        self.game_status()

    def letter_is_correct(self):
        """
        Checks if the letter is already guessed
        if not, it adds it to the correct letters storage
        then it hands over a counter
        to check if game win occurs
        """

        if self.guessed_lett in self.correct_lett:
            duplication_msg = "You have already chosen this letter"
            self.game_msgs["Multiple Letters"] = (Fore.LIGHTYELLOW_EX +
                                                  duplication_msg)
        else:
            for index, letter in enumerate(self.word):
                if self.guessed_lett == letter:
                    self.count += 1
                    self.correct_lett[index] = letter
            correct_msg = "You have chosen the correct letter"
            self.game_msgs["Correct Letter"] = Fore.LIGHTGREEN_EX + correct_msg
        self.game_status()

    def game_status(self):
        """
        checks if win or lose occurs
        if so, it announces
        the final game status
        """

        if len(self.wrong_lett) == self.word_len:
            self.game_msgs["Lost Message"] = (
                Fore.RED
                + f"""
            You lost! The word is {''.join(self.word).capitalize()}
            """
            )
            self.clear_screen()
            self.game_dashboard()
            self.reset_game()
            self.reset_signal = True
            self.game_over(self.reset_signal)
        elif self.count == self.word_len:
            self.game_msgs["Won Message"] = (
                Fore.GREEN
                + f"""
            Great Job! The word is {''.join(self.word).capitalize()}
            """
            )
            self.clear_screen()
            self.game_dashboard()
            self.reset_game()
            self.reset_signal = True
            self.game_over(self.reset_signal)
        else:
            self.clear_screen()
            self.game_dashboard()

    def game_dashboard(self):
        """
        The method is used to display
        the game setup, status and error
        messages
        """
        real_time_chances = self.word_len - len(self.wrong_lett)
        dashboard_msg = ""
        for msg_value in self.game_msgs.values():
            if msg_value is not None:
                dashboard_msg = msg_value
        print(
            Fore.LIGHTCYAN_EX
            + f"""
                            Game Dashboard
            ###################################################
                             Game Setting

            Player Name         : {self.name.capitalize()}
            Difficulty Level    : {self.dif_value.capitalize()}
            Chances             : {self.word_len}
            ---------------------------------------------------
                              Game Satus

            {Fore.GREEN}Correct Guesses     : {self.correct_lett}
            {Fore.RED}Worng Guesses       : {self.wrong_lett}
            {Fore.BLUE}Current chances     : {real_time_chances}
            {Fore.LIGHTCYAN_EX}----------------------------------------------------
                             Game Messages

            {dashboard_msg}
            """
        )

    def game_over(self, reset_signal):
        """
        It is used to signal a game 
        reset is needed
        """
        if reset_signal:
            return True
        else:
            return False
