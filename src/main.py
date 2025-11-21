from scripts.welcome import *
from player import Player
from levels.level_0 import *

def main():
    # TODO: Load Save File when I create it
    welcome_message()
    level_zero = load_level_0()
    player_name = input("So, player, go ahead and enter your name: ")
    player = Player(player_name, level_zero)
    choice = None
    moves = 0

    while(choice != -1):
        # Print the level name
        print(player.level.name)

        choice = input("Your move: ")
        # Check for "move", "go", "go to", "get in", "enter"

        # Check for "exit", "quit", etc.
        if choice == "exit" or choice == "quit":
            print(f"You made a total of {moves} moves.")
            exit()
        
        moves += 1


    


if __name__ == "__main__":
    main()