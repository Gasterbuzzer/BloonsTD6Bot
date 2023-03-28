import pyautogui
import time
import winsound
from ahk import AHK

monkey_towers_names_key = {"dart_monkey": "q", "boomerang_monkey": "w", "bomb_shooter": "e", "tack_shooter": "r",
                           "ice_monkey": "t", "glue_gunner": "y", "sniper_monkey": "z", "monkey_sub": "x",
                           "monkey_buccaneer": "c", "monkey_ace": "v", "heli_pilot": "b", "mortar_monkey": "n",
                           "dartling_gunner": "m", "wizard_monkey": "a", "super_monkey": "s", "ninja_monkey": "d",
                           "alchemist": "f", "druid": "g", "banana_farm": "h", "engineer_monkey": "l",
                           "spike_factory": "j", "monkey_village": "k", "heroes": "u"}

monkey_towers_names_id = {"0": "dart_monkey", "1": "boomerang_monkey", "2": "bomb_shooter", "3": "tack_shooter",
                          "4": "ice_monkey", "5": "glue_gunner", "6": "sniper_monkey", "7": "monkey_sub",
                          "8": "monkey_buccaneer", "9": "monkey_ace", "10": "heli_pilot", "11": "mortar_monkey",
                          "12": "dartling_gunner", "13": "wizard_monkey", "14": "super_monkey", "15": "ninja_monkey",
                          "16": "alchemist", "17": "druid", "18": "banana_farm", "19": "engineer_monkey",
                          "20": "spike_factory", "21": "monkey_village", "22": "heroes"}

monkey_tower_options = {"upgrade_path_1": ",", "upgrade_path_2": ".", "upgrade_path_3": "/", "change_targeting": "tab",
                        "reverse_change_targeting": "ctrl + tab", "monkey_special": "PageDown"}

game_options = {"sell": "Backspace", "next_round_race": "shift + space"}

tower_abilities_options = {"activated_ability_1": "1", "activated_ability_2": "2", "activated_ability_3": "3",
                           "activated_ability_4": "4", "activated_ability_5": "5", "activated_ability_6": "6",
                           "activated_ability_7": "7", "activated_ability_8": "8", "activated_ability_9": "9",
                           "activated_ability_10": "0", "activated_ability_11": "-", "activated_ability_12": "="}

play_options = {"play": "space", "fast_forward": "space", "pause": "backquote", "pause_alt": "`"}

click_locations = {"settings_button_ingame": {"x": 1601, "y": 35}, "settings_home": {"x": 844, "y": 833},
                   "play_main_menu": {"x": 833, "y": 936}, "beginner_button_select": {"x": 566, "y": 967},
                   "intermediate_button_select": {"x": 832, "y": 961},
                   "advanced_button_select": {"x": 1089, "y": 981}, "expert_button_select": {"x": 1338, "y": 975},
                   "easy_difficulty": {"x": 616, "y": 432}, "medium_difficulty": {"x": 962, "y": 427},
                   "hard_difficulty": {"x": 1279, "y": 410}, "standard": {"x": 636, "y": 590},
                   "primary_only": {"x": 957, "y": 452}, "deflation": {"x": 1284, "y": 446},
                   "sandbox_easy": {"x": 963, "y": 731}, "military_only": {"x": 950, "y": 438},
                   "apopalypse": {"x": 1292, "y": 446}, "reverse": {"x": 957, "y": 735},
                   "sandbox_medium": {"x": 1275, "y": 728}, "sandbox_hard": {"x": 302, "y": 587},
                   "magic_monkeys_only": {"x": 954, "y": 452}, "double_hp_moabs": {"x": 1269, "y": 458},
                   "half_cash": {"x": 1612, "y": 458}, "alternate_bloons_rounds": {"x": 951, "y": 741},
                   "impoppable": {"x": 1293, "y": 751}, "chimps": {"x": 1604, "y": 745}}

level_click_locations = {0: {"x": 516, "y": 251}, 1: {"x": 956, "y": 254}, 2: {"x": 1396, "y": 267},
                         3: {"x": 530, "y": 577}, 4: {"x": 962, "y": 563}, 5: {"x": 1387, "y": 562}}


def select_place_monkey_tower(tower_name="None", tower_number="-1", ahk=None):
    """Places tower by using the corresponding key, can only use one thing to call."""

    # We check if invalid.
    if tower_name == "None" and tower_number == "-1":
        print(f"Error SelectPlace: No tower information given.\n")
        return

    if tower_name != "None":
        keypress = monkey_towers_names_key[tower_name]
        print(f"Pressing the key '{keypress}'.\n")

        ahk.send_input(keypress)
        time.sleep(0.3)

        return

    elif tower_number != "-1":
        keypress = monkey_towers_names_key[monkey_towers_names_id[tower_number]]
        print(f"Pressing the key '{keypress}'.\n")

        ahk.send_input(keypress)
        time.sleep(0.3)

        return

    else:
        print(f"Error SelectPlace: Unknown tower : {tower_name} and {tower_number}.\n")
        return


def place_monkey_tower(tower_name="None", tower_number="-1", coordinates=None, ahk=None):
    """Places the tower selected."""

    if coordinates is None:
        coordinates = {"x": 0, "y": 0}

    select_place_monkey_tower(tower_name, tower_number, ahk)
    pyautogui.moveTo(coordinates["x"], coordinates["y"])
    click(coordinates)


def check_current_menu():
    """Checks where the current user is located at. Returns a dictionary containing the info."""

    # Trying to locate
    play_dec = pyautogui.pixelMatchesColor(838, 940, (255, 255, 255))

    game_dec = pyautogui.pixelMatchesColor(1776, 25, (114, 232, 0))

    select_01_dec = pyautogui.pixelMatchesColor(613, 946, (0, 213, 227))  # Easy selected
    select_02_dec = pyautogui.pixelMatchesColor(612, 956, (0, 255, 236))  # Easy not selected
    select_03_dec = pyautogui.pixelMatchesColor(814, 1007, (0, 221, 232))  # Medium selected
    select_04_dec = pyautogui.pixelMatchesColor(820, 1010, (0, 222, 233))  # Medium not selected

    if play_dec:
        return {"location": "main_menu"}
    elif game_dec:
        return {"location": "ingame"}
    elif (select_01_dec and select_02_dec) or (select_03_dec and select_04_dec):
        return {"location": "select_screen"}
    else:
        return {"location": "unknown"}


def small_beep():
    frequency = 2000  # Set Frequency To 2500 Hertz
    duration = 200  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


def check_ingame_window():
    """Checks if the current Window is bloons or not."""

    status = pyautogui.getActiveWindowTitle()

    if status == "BloonsTD6":
        return True
    else:
        return False


def check_level(level):
    """Checks if the level is visible"""
    # level_click_locations[0]
    match level:
        case 0:
            result = pyautogui.pixelMatchesColor(650, 253, (134, 196, 38))
            print(result)
            return result
        case _:
            print(False)
            return False


def select_level(level=0, difficulty=0, game_mode="standard"):
    """Selects the corresponding level to play, mostly hard coded."""
    menu = check_current_menu()

    if menu["location"] != "select_screen":
        print("Error SelectLevel: Not in select screen. Going to select screen...\n")
        go_select_level()

    match level:
        case 0:
            while not check_level(level):
                click(click_locations["beginner_button_select"])
            click(level_click_locations[0])
        case 1:
            while not check_level(level):
                click(click_locations["beginner_button_select"])
            click(level_click_locations[1])
        case 2:
            while not check_level(level):
                click(click_locations["beginner_button_select"])
            click(level_click_locations[2])
        case 3:
            while not check_level(level):
                click(click_locations["beginner_button_select"])
            click(level_click_locations[3])
        case 4:
            while not check_level(level):
                click(click_locations["beginner_button_select"])
            click(level_click_locations[4])
        case 5:
            while not check_level(level):
                click(click_locations["beginner_button_select"])
            click(level_click_locations[5])
        case _:
            print("ERROR: Level is not available.\n")
            return

    match difficulty:
        case 0:
            click(click_locations["easy_difficulty"])
        case 1:
            click(click_locations["medium_difficulty"])
        case 2:
            click(click_locations["hard_difficulty"])
        case _:
            print(f"ERROR: Difficulty {difficulty} is unknown.\n")

    game_mode_check = click_locations[game_mode]
    if game_mode_check is None:
        print(f"ERROR: Unknown Game Mode {game_mode}.\n")
        return
    else:
        click(game_mode_check)

    time.sleep(2)


def go_select_level():
    """Goes to select level screen"""

    if not check_ingame_window():
        print("Error GoSelectScreen: Not in game.")
        return

    menu = check_current_menu()

    match menu["location"]:

        case "select_screen":
            reset_cursor()
            return

        case "ingame":
            click(click_locations["settings_button_ingame"])
            click(click_locations["settings_home"])
            long_wait_click(click_locations["play_main_menu"])
            reset_cursor()
            return

        case "main_menu":
            click(click_locations["play_main_menu"])
            reset_cursor()
            return

        case _:
            print("Error GoSelectScreen: Not in known menu.")
            return


def click(coords=None):
    """Clicks at given coordinates, used to avoid other formats."""
    if coords is None:
        coords = {"x": 0, "y": 0}

    pyautogui.click(coords["x"], coords["y"])
    time.sleep(0.3)


def wait_click(coords=None):
    """Clicks at given coordinates, used to avoid other formats. Waits 1 second before."""
    if coords is None:
        coords = {"x": 0, "y": 0}

    time.sleep(1)
    pyautogui.click(coords["x"], coords["y"])
    time.sleep(0.3)


def long_wait_click(coords=None):
    """Clicks at given coordinates, used to avoid other formats. Waits 3 seconds before."""
    if coords is None:
        coords = {"x": 0, "y": 0}

    time.sleep(3)
    pyautogui.click(coords["x"], coords["y"])
    time.sleep(0.3)


def reset_cursor():
    pyautogui.moveTo(1, 1)


if __name__ == "__main__":
    ahks = AHK()

    time.sleep(5)
    small_beep()

    select_level(0, 0, "standard")
    #check_level(0)

    place_monkey_tower(tower_name="None", tower_number="1", coordinates={"x": 900, "y": 400}, ahk=ahks)
