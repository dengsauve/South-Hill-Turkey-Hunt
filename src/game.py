from scripts import welcome
from player import Player
from utils import clear_screen
from world import build_world

class Game():
    def __init__(self):
        self.moves = 0 # Track the moves that a player makes
        self.world = build_world()
        self.choice = None
        self.player = None
        self.level = self.world["home"]


    def start(self):
        welcome.welcome_message()
        self.setup_player()

        while(self.choice != -1):
            # Print the level name
            print(f"\nYou're at: {self.level.name}")

            self.choice = input("\n\nYour move: ")
            clear_screen()
            # Check for "help", "instructions"
            if self.choice == "help" or self.choice == "instructions" or self.choice == "moves":
                help.show_help(self.player)
            
            # Check for "look"
            if self.choice == "look":
                print(f"\n{self.level.description}")
                print(f"\nAround you you see:")
                for direction, level in (self.level.get_adjacent_levels()).items():
                    print (f"- {direction}: {level.get_name()}")
            
            # Check for "move", "go", "go to", "get in", "enter"
            if self.choice.lower() in ['move', '']

            # Check for "exit", "quit", etc.
            if self.choice == "exit" or self.choice == "quit":
                print(f"You made a total of {self.moves} moves.")
                exit()
            
            self.moves += 1
    

    def setup_player(self):
        player_name = input("So, player, go ahead and enter your name: ")
        self.player = Player(player_name)