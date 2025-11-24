import random
from scripts import welcome, help
from player import Player
from utils import clear_screen
from world import build_world
from constants import *


class Game:
    def __init__(self):
        self.moves = 0  # Track the moves that a player makes
        self.world = build_world()
        self.command = None
        self.player = None
        self.level = self.world["home"]

    def start(self):
        welcome.welcome_message()
        self.setup_player()
        print(f"\nYou're at {self.level.name}")

        while self.command != -1:
            self.command = input("\n=========\nYour move: ")
            print()
            self.parse_command()
            self.moves += 1

    def setup_player(self):
        player_name = input("So, player, go ahead and enter your name: ")
        self.player = Player(player_name)

    def parse_command(self):
        words = self.command.lower().split(" ")
        verb = words[0]
        args = words[1] if len(words) > 1 else None
        # print(words, verb, args)

        if verb in HELP_COMMANDS:
            help.show_help(self.player)
        elif verb in OBSERVE_VERBS:
            self.show_observation()
        elif verb in MOVE_VERBS:
            self.move_player(args)
        elif verb in GRAB_VERBS:
            self.grab(args)
        elif verb in HUNT_VERBS:
            self.hunt_turkey()
        elif verb in INVENTORY_COMMANDS:
            self.show_inventory()
        elif verb in EXIT_VERBS:
            self.exit_game()

    def show_observation(self):
        print(self.level.get_observation())
    
    def show_inventory(self):
        print(self.player.get_inventory())

    def move_player(self, args):
        if not args:
            print("Move where?")
        else:
            if args in self.level.get_adjacent_levels().keys():
                self.level = self.level.get_adjacent_level(args)
                print(self.level.get_observation())
            else:
                print(f"{args} is not a valid destination.")

    def hunt_turkey(self):
        # Check for turkeys
        if self.level.turkeys == 0:
            print("There are no turkeys to hunt here, try another park.")
            return
        # Check for arrows
        if self.player.inventory["arrow"] == 0:
            print("You've run out of arrows, take what you have to the butcher.")
            return
        # Proceed with the hunt
        self.player.shoot_arrow()
        self.level.remove_turkey()
        self.player.add_turkey()
        print(f"You successfully bag a turkey! {self.player.get_turkey_status()}")

    def grab(self, args):
        if args == None:
            print("Grab what?")
            return
        if args == "turkey":
            if self.level.turkeys > 0:
                damage_points = random.choice([1, 2, 3])
                self.player.take_damage(damage_points)
                print(
                    f"Grabbing a turkey turns out to be a poor idea. You lose {damage_points} points of health!"
                )
                print(self.player.get_health_status())
            else:
                print(
                    "There are no turkeys to grab, and even if there were, it's not a good idea. (hint hint)"
                )
        else:
            print(f"You cannot grab {args}")

    def exit_game(self):
        print(f"You made a total of {self.moves} moves.")
        exit()
