from classes.gamemixins import GameMixins


class PlayerGuess(GameMixins):
    """
    This class gets player guesses
    and then processes the inputs
    """

    def __init__(self, name, dif_value, word_len, word):
        self.name = name
        self.dif_value = dif_value
        self.word = word
        self.word_len = word_len
        self.correct_lett = ["_"] * word_len
        self.wrong_lett = []
        self.count = 0
        self.duplication_msg = None
        self.correct_msg = None
        self.wrong_msg = None
        self.value_err_msg = None
        self.ctrl_c_msg = None
        self.won_msg = None
        self.lost_msg = None
        self.ctrl_d_msg = None
        self.reset_signal = False
        self.clear_screen()
        self.game_dashboard()
        self.get_player_guess()

    def get_player_guess(self):
        """
        Gets the plyer guess
        then it checks for its validity
        then it handovers the guessed letter
        to evaluate the guessed letters method
        """
        while True:
            self.duplication_msg = None
            self.correct_msg = None
            self.wrong_msg = None
            self.won_msg = None
            self.lost_msg = None
            self.value_err_msg = None
            self.ctrl_c_msg = None
            self.ctrl_d_msg = None
            if self.game_over(self.reset_signal):
                break
            try:
                self.guessed_lett = input(
                    "Please enter a letter:\n "
                    )
                if (self.guessed_lett.isalpha()
                   and len(self.guessed_lett)) == 1:
                    self.evaluate_guessed_letters()
                else:
                    raise ValueError
            except ValueError:
                self.value_err_msg = "Please enter ONLY ONE and Valid LETTER."
            except KeyboardInterrupt:
                self.ctrl_c_msg = "Ctrl C is not allowed!"
            self.clear_screen()
            self.game_dashboard()

    def evaluate_guessed_letters(self):
        """
        Evaluates the player guess
        and it handovers the result to
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
        then it hands over a counter
        to check if game lose occures
        """

        if self.guessed_lett in self.wrong_lett:
            self.duplication_msg = "You have already chosen this letter"
        else:
            self.wrong_lett.append(self.guessed_lett)
            self.wrong_msg = "You have chosen the worng letter"
        self.game_status()

    def letter_is_correct(self):
        """
        Checks if the letter is already guesssed
        if not, it adds it to the correct letters storage
        then it hands over a counter
        to check if game win occurs
        """

        if self.guessed_lett in self.correct_lett:
            self.duplication_msg = "You have already chosen this letter"
        else:
            for index, letter in enumerate(self.word):
                if self.guessed_lett == letter:
                    self.count += 1
                    self.correct_lett[index] = letter
            self.correct_msg = "You have chosen the correct letter"
        self.game_status()

    def game_status(self):
        """
        checks if win or lose occures
        if so, it announces
        the final game status
        """

        if len(self.wrong_lett) == self.word_len:
            self.lost_msg = f"""
            You lost! The word is {''.join(self.word).capitalize()}
            """
            self.clear_screen()
            self.game_dashboard()
            self.reset_game()
            self.reset_signal = True
            self.game_over(self.reset_signal)
        elif self.count == self.word_len:
            self.won_msg = f"""
            Great Job! The word is {''.join(self.word).capitalize()}
            """
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
        messges
        """

        self.dashboard_msg = {
            "Correct Letter": self.correct_msg,
            "Wrong Letter": self.wrong_msg,
            "Letter Duplication": self.duplication_msg,
            "Game is won": self.won_msg,
            "Game is lost": self.lost_msg,
            "Value Error": self.value_err_msg,
            "Ctrl C Key": self.ctrl_c_msg
        }
        game_msg = ""
        for msg_key, msg_value in self.dashboard_msg.items():
            if msg_value is not None:
                game_msg = msg_value
        print(
            f"""
            ###################################################
                            Game Dashboard
            ###################################################
            ---------------------------------------------------
                             Game Setting
            ---------------------------------------------------

            Player Name       : {self.name.capitalize()}
            Difficulty Level  : {self.dif_value.capitalize()}
            Chances           : {self.word_len}
            ---------------------------------------------------
                              Game Satus
            ---------------------------------------------------

            Correct Guesses   : {self.correct_lett}
            Worng Guesses     : {self.wrong_lett}
            Current chances   : {self.word_len-len(self.wrong_lett)}

            ----------------------------------------------------
                              Game Messages
            ----------------------------------------------------
            {game_msg}
            ####################################################
            """
        )

    def game_over(self, reset_signal):
        """
        It is used to signal a reset 
        is needed
        """
        if reset_signal:
            return True
        else:
            return False
