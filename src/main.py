# from scripts.welcome import *
from scripts import welcome, help
from levels.level_0 import *
from player import Player
from utils import clear_screen

def main():
    clear_screen()
    # TODO: Load Save File when I create it
    welcome.welcome_message()
    level_zero = load_level_0()
    player_name = input("So, player, go ahead and enter your name: ")
    player = Player(player_name, level_zero)
    choice = None
    moves = 0

    while(choice != -1):
        # Print the level name
        print(f"\nYou're at: {player.level.name}")

        choice = input("\n\nYour move: ")
        clear_screen()
        # Check for "help", "instructions"
        if choice == "help" or choice == "instructions" or choice == "moves":
            help.show_help(player)
        
        # Check for "look"
        if choice == "look":
            print(f"\n{player.level.description}")
            print(f"\nAround you you see:")
            for lvl in player.level.adjacent_levels:
                print (f"- {lvl.name}")
        
        # Check for "move", "go", "go to", "get in", "enter"

        # Check for "exit", "quit", etc.
        if choice == "exit" or choice == "quit":
            print(f"You made a total of {moves} moves.")
            exit()
        
        moves += 1


    


if __name__ == "__main__":
    main()