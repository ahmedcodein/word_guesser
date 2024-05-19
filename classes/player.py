from classes.difficultyselection import DifficultySelection


class Player:
    """
    Ask for user first name
    Check if the first name is not lengthy
    Check if the user gave a name, if not assume one
    """

    def __init__(self):
        self.first_name()
        self.welcome_the_player()

    def first_name(self):
        """
        The method for input the first name
        and for checking the name validity
        """
        while True:
            try:
                self.first_name = input("Please enter your first name:\n ").lower().strip("")
                if len(self.first_name) > 10:
                    print("\nPlease enter a name with less than 11 letters\n")
                else:
                    break
            except KeyboardInterrupt:
                print("\nCtrl C is not allowed!")

    def welcome_the_player(self):
        """
        Print out the welcome message with the first name
        """
        self.welcome_the_player = print(f"\nWelcome {self.first_name.capitalize()}!\n")
        DifficultySelection()
