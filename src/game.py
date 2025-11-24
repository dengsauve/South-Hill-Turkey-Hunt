from scripts import welcome, help
from player import Player
from utils import clear_screen
from world import build_world

MOVE_VERBS = ("move", "go", "travel", "walk", "drive")
EXIT_VERBS = ("quit", "exit", "e", "q")
OBSERVE_VERBS = ("look", "l")
HELP_COMMANDS = ("help", "instructions", "h")


class Game():
    def __init__(self):
        self.moves = 0 # Track the moves that a player makes
        self.world = build_world()
        self.command = None
        self.player = None
        self.level = self.world["home"]


    def start(self):
        welcome.welcome_message()
        self.setup_player()

        while(self.command != -1):
            # Print the level name
            print(f"\nYou're at: {self.level.name}")

            self.command = input("\n\nYour move: ")
            # clear_screen()
            self.parse_command()
            
            self.moves += 1
    

    def setup_player(self):
        player_name = input("So, player, go ahead and enter your name: ")
        self.player = Player(player_name)
    

    def parse_command(self):
        words = self.command.lower().split(' ')
        verb = words[0]
        args = words[1] if len(words) > 1 else None
        print(words, verb, args)
        
        # Check for "help", "instructions"
        if verb in HELP_COMMANDS:
            help.show_help(self.player)
        
        # Check for "look"
        if verb in OBSERVE_VERBS:
            print(f"\n{self.level.description}")
            print(f"\nAround you you see:")
            for direction, level in (self.level.get_adjacent_levels()).items():
                print (f"- {direction}: {level.get_name()}")
        
        # Check for "move", "go", "go to", "get in", "enter"
        if verb in MOVE_VERBS:
            print(args)
            if not args:
                print("Move where?")
            else:
                self.level = self.level.get_adjacent_level(args)

        # Check for "exit", "quit", etc.
        if verb in EXIT_VERBS:
            print(f"You made a total of {self.moves} moves.")
            exit()