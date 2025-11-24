from textwrap import dedent
from constants import *

PLACE_DESC = "_place_: this can be a whole or partial name of an adjacent area"

def show_help(player):
    message = f"""\
    Ok {player.name}, here's the 411:

    - {' | '.join(MOVE_VERBS)}
        usage: "move (direction, e.g. north, south, east, west)"
    
    - {' | '.join(OBSERVE_VERBS)}
        purpose: Provide a description of the current or surrounding area(s)
        usage: "look", "look (direction)"
    
    - {' | '.join(GRAB_VERBS)}
        purpose: Grab something
        usage: "grab turkey"

    - {' | '.join(HUNT_VERBS)}
        purpose: Hunt turkeys in a location, if there are any

    - {' | '.join(INVENTORY_COMMANDS)}
        purpose: Take stock of what you have in your backpack
    
    - {' | '.join(EXIT_VERBS)}
        purpose: Exit the game and provide the number of moves taken
    """
    print(dedent(message))