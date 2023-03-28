import pyautogui
from ahk import AHK
import bot
import time


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

    elif command[:5] == "level":
        print("Starting bot...\n")

        # Getting arguments
        args = command.split()

        if len(args) != 4:
            print("ERROR: Incorrect format. See 'help' for usage.\n")
            return response

        level = int(args[1])
        difficulty = int(args[2])
        gamemode = args[3]

        ahk = AHK()

        # Timer before bot start.
        time.sleep(5)
        bot.small_beep()

        # Bot playing.
        bot.play_level(ahk, 0, 0, "standard")

        return response

    elif command[:4] == "loop":
        print("Starting looping bot...\n")

        # Getting arguments
        args = command.split()

        if len(args) != 5:
            print("ERROR: Incorrect format. See 'help' for usage.\n")
            return response

        level = int(args[1])
        difficulty = int(args[2])
        gamemode = args[3]
        loop_amount = args[4]

        ahk = AHK()

        print(f"Starting to loop {loop_amount} times. Starting in 5 seconds...\n")
        # Timer before bot start.
        time.sleep(5)
        bot.small_beep()

        # Bot playing.
        for number in range(loop_amount):
            bot.play_level(ahk, 0, 0, "standard")

        print(f"Loop: Finished looping {loop_amount} times.\n")

        return response

    else:
        print(f"ERROR: Unknown command '{command}'.\n")
        return response


def help_print():
    """Prints all commands to console"""
    print("\nAll commands: ")
    print("\t\t'h' or 'help'                                             : Shows all commands (currently)")
    print("\t\t'q' or 'quit'                                             : Quit the program")
    print("\t\t'level %level% %difficulty %gamemode%'                    : Starts playing level. (Example: 'level 0 0 "
          "standard')")
    print("\t\t'level %level% %difficulty %gamemode% %loopamount%'       : Starts looping a level. (Example: 'level 0 "
          "0 standard 10')")

    print("\n")


if __name__ == "__main__":
    main()
