# from scripts.welcome import *
from utils import clear_screen
from game import Game

def main():
    clear_screen()
    # TODO: Load Save File when I create it
    game = Game()
    game.start()


if __name__ == "__main__":
    main()