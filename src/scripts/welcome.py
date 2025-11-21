from textwrap import dedent

def welcome_message():
    # TODO: Make this scroll out like an RPG. Maybe not. IDK
    message = """\
    You wake up early in the morning, the Wednesday before Thanksgiving.
    You head to the kitchen to pour a bowl of Muesli and turn on the TV.
    
    There's a breaking news story!!

    All of the turkeys donated to Tom's Turkey Drive are tainted with salmonella, botchelism,
    influenza, and have heavy metal poisoning.

    Sources aren't sure as to what caused this, but the outcome is now there are no turkeys for
    families in need across Spokane County.

    The call is out to the public: Please donate any and all spare turkeys so that no family has to
    go without this Thanksgiving.


    You stare at the screen, saddened. You don't have any spare turkeys, and cash is a little tight.
    You want to help out, but you cannot afford to.

    However...

    ...you do have your prize hunting bow and a dozen arrows in the garage.
    """
    print(dedent(message))