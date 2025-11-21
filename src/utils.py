import os

def clear_screen():
    """Clears the terminal screen in a platform-agnostic way."""
    # Check the operating system name
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For macOS and Linux
        _ = os.system('clear')