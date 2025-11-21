from textwrap import dedent

PLACE_DESC = "_place_: this can be a whole or partial name of an adjacent area"

def show_help(player):
    message = f"""\
    Ok {player.name}, here's the 411:

    - move
        usage: "move _place_"
        {PLACE_DESC}
    
    - look
        purpose: Provide a description of the current or surrounding area(s)
        usage: "look", "look _place_"
        {PLACE_DESC}
    
    - quit | exit
        purpose: Exit the game and provide the number of moves taken
        usage: "quit", "exit"
    """
    print(dedent(message))