from textwrap import dedent


def welcome_message():
    # TODO: Make this scroll out like an RPG. Maybe not. IDK
    message = """\n\n\
    =========
    You wake up early in the morning, the Wednesday before Thanksgiving.
    You head to the kitchen to pour a bowl of Muesli and turn on the TV.
    
    There's a breaking news story!!

    All of the turkeys donated to Tom's Turkey Drive are tainted with salmonella,
    botchelism, influenza, and have heavy metal poisoning.

    Sources aren't sure as to what caused this, 
    but the outcome is now there are no turkeys for
    families in need across Spokane County.

    The call is out to the public: Please donate any and all spare turkeys!


    You stare at the screen, saddened.
    You don't have any spare turkeys,
    and cash is a little tight.
    You want to help out, but you cannot afford to.

    However...
    ...you do have your prize hunting bow and a dozen arrows in the garage.
    """
    print(dedent(message))


def splash_screen():
    width = 60
    line_0 = """
    ____                        _      
   / __ \___  ____  ____  __  _( )_____
  / / / / _ \/ __ \/ __ \/ / / /// ___/
 / /_/ /  __/ / / / / / / /_/ / (__  ) 
/_____/\___/_/ /_/_/ /_/\__, / /____/  
                       /____/          
"""
    line_1 = """
 _____             _   _       _   _ _ _ _ 
/  ___|           | | | |     | | | (_) | |
\ `--.  ___  _   _| |_| |__   | |_| |_| | |
 `--. \/ _ \| | | | __| '_ \  |  _  | | | |
/\__/ / (_) | |_| | |_| | | | | | | | | | |
\____/ \___/ \__,_|\__|_| |_| \_| |_/_|_|_|                                         
"""
    line_2 = """
 _____          _                _   _             _   
|_   _|        | |              | | | |           | |  
  | |_   _ _ __| | _____ _   _  | |_| |_   _ _ __ | |_ 
  | | | | | '__| |/ / _ \ | | | |  _  | | | | '_ \| __|
  | | |_| | |  |   <  __/ |_| | | | | | |_| | | | | |_ 
  \_/\__,_|_|  |_|\_\___|\__, | \_| |_/\__,_|_| |_|\__|
                          __/ |                        
                         |___/                         
"""
    prompt = "Press 'Enter' to Play".center(width)
    banner = line_0.center(width)
    title_1 = line_1.center(width)
    title_2 = line_2.center(width)

    print(banner, title_1, title_2)
    print(prompt)
    input()
    
