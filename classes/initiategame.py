import os
from getch import pause
from classes.player import Player
from classes.gamemixins import GameMixins


class InitiateGame(GameMixins):
    """
    Intiate the game by a welcome message and instructions
    Then clear the screen upon user order
    Intiate the Player class
    """

    def __init__(self):
        self.welcome()
        self.intructions()

    def welcome(self):
        """
        Print out a welcome message
        """
        print("\nWelcome to the Word Guess Game!")

    def intructions(self):
        """
        Display the game rules and instructions
        then pause and wait for the user action to proceed
        """
        print(
            """
        The job is to guess an English word by entering its letters one by one.
        You have three difficulty levels to choose from:\n
        - Easy for 3-letter words 
        - Intermediate for 5-letter words 
        - Difficult for 6-letter words \n
        Based on the difficulty level, you will have 3, 5 or 6 chances respectively. 
        Choose wisely!.\n
        Have fun!\n
        """
        )
        pause()
        self.clear_screen()
        Player()
