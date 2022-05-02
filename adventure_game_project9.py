# sources for class color, check_input and parts of print_slow.
# Were modeled after examples and suggestions from the first udacity reviewer.
# 3/14/22 https:review.udacity.com/#!/reviews/3447011
import time
import random
import enum
import string


class color(enum.Enum):
    red = '\033[91m'
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    black = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


def print_slow(print_message):
    print_message = (color.get_color() + print_message)
    for char in print_message:
        print(char, end="")
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)


def check_input(prompt, anwsers):
    while True:
        anwser = input(prompt).lower()
        if anwser in anwsers:
            return anwser
        print_slow("Sorry, invaild response. Please try again!")


def intro():
    print_slow("You are traveling on a ship at sea.\n"
               "On a well earned vacation.\n")
    print_slow("When a great storm hits.\n"
               "While you are in the middle of the ocean.\n")
    print_slow("The ship holds together for a time.\n"
               "But the storm is too great.\n"
               "The ship succumbs to the might of the storm.\n")
    print_slow("You awaken on a beach with white sand.\n"
               "The waves are crashing down in the background.\n"
               "The sun is high in the sky.\n")
    print_slow("You see no other survivors on the beach.\n"
               "You appear to be alone.\n")


def beach(inventory, sea_creatures, weapon_list, sea_creature, weapon):
    print_slow("To your left is a vast ocean as far as the eye can see.\n"
               "With a calm surf and crystal clear blue waters.\n")
    print_slow("To your right is a recent shipwreck.\n"
               "The remnants of the ship you were traveling on.\n")
    choice1 = check_input("Enter 1 for the right and the shipwreck.\n"
                          "Enter 2 for the left and the vast ocean.\n",
                          ["1", "2"])
    if choice1 == "1":
        shipwreck(inventory, sea_creatures, weapon_list, sea_creature, weapon)
    elif choice1 == "2":
        vast_ocean(inventory, sea_creatures, weapon_list, sea_creature, weapon)


def vast_ocean(inventory, sea_creatures, weapon_list, sea_creature, weapon):
    print_slow("You enter the crystal clear blue waters.\n")
    print_slow(f"Out from the water jumps a {sea_creature}.\n")
    print_slow(f"The {sea_creature} attacks.\n")
    choice2 = check_input("Enter 1 to attack.\n"
                          "Enter 2 to run away.\n", ["1", "2"])
    if choice2 == "1":
        if "weapon" in inventory:
            print_slow("Luckily you found a weapon in the shipwreck.\n")
            print_slow(f"You attack the {sea_creature} with the {weapon}.\n")
            print_slow("You have successfully survived and live"
                       " another day!\n")
            play_again()
        else:
            print_slow(f"You attack the {sea_creature}"
                       " but unfortunately you do not have a weapon.\n")
            print_slow("You have been defeated.\n")
            play_again()
    elif choice2 == "2":
        print_slow("You luckily dodge the attack.\n"
                   "Running back to the safety of the beach.\n")
        beach(inventory, sea_creatures, weapon_list, sea_creature, weapon)


def shipwreck(inventory, sea_creatures, weapon_list, sea_creature, weapon):
    print_slow("You enter the shipwreck.\n"
               "Not much is left of the vessel.\n"
               "You are very lucky to have survived.\n")
    if "weapon" in inventory:
        print_slow("You look around and see nothing of use.\n"
                   "Somberly you walk back to the beach.\n")
        beach(inventory, sea_creatures, weapon_list, sea_creature, weapon)
    else:
        print_slow("You lift a broken piece of the ship and"
                   f" find a {weapon}.\n")
        print_slow(f"You pick up the {weapon}.\n")
        inventory.append("weapon")
        print_slow("You have salavaged all you can from the"
                   " wrecked vessel.\n"
                   "You return to the beach.\n")
        beach(inventory, sea_creatures, weapon_list, sea_creature, weapon)


def play_again():
    print_slow("Thank you for playing!\nWould you like to play again?\n")
    choice3 = check_input("Enter y for Yes.\n"
                          "Enter n for No.\n", ["y", "n"])
    if choice3 == "y":
        print_slow("New Game will begin soon!\n")
        start_game()
    elif choice3 == "n":
        print_slow("Thank you for playing!\nHave a great day!\n")


def start_game():
    inventory = []
    sea_creatures = ["Giant Octopus", "Tiger Shark", "Sea Serpent",
                     "Giant Piranha", "Salt Water Crocodile",
                     "Killer Whale", "Great White Shark"]
    weapon_list = ["Spear Gun", "Hand Gun", "Shotgun", "Harpoon",
                   "Small Hand Axe", "Long Bladed Knife", "Flare Gun"]
    sea_creature = random.choice(sea_creatures)
    weapon = random.choice(weapon_list)
    intro()
    beach(inventory, sea_creatures, weapon_list, sea_creature, weapon)


start_game()
