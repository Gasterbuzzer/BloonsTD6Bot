import pyautogui
from ahk import AHK


# Interactive loop
def main():
    """Main Function"""
    screen_resolution = pyautogui.size()

    active = True

    # im = pyautogui.screenshot()
    # pix = pyautogui.pixel(115, 275)
    # print(pix)

    print("Running console... (Use 'q' or 'quit' to exit) ('h' or 'help' for all commands)\n")

    while active:

        # Get command and handle
        print("CMD: ", end="")
        user_input = input()
        response = handle_input(user_input)

        # If the user wants to quit
        if not response:
            active = False
            break


def handle_input(command):
    """Handles user Input"""

    response = True

    if command == "help" or command == "h":
        # Handle help command.
        help_print()
        return response

    elif command == "quit" or command == "q":
        response = False
        return response

    elif command[:5] == "start":
        print("Starting\n")
        return response

    else:
        print(f"ERROR: Unknown command '{command}'.\n")
        return response


def help_print():
    """Prints all commands to console"""
    print("\nAll commands: ")
    print("\t\t'h' or 'help' : Shows all commands (currently)")
    print("\t\t'q' or 'quit' : Quit the program")

    print("\n")


if __name__ == "__main__":
    main()
