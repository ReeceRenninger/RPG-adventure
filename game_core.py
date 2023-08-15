# Base file for the game contains the main game code

# import time module to delay text, this is needed to manipulate the speed of the text
import time
from character import Character, Items, Barbarian, Paladin, Ranger, choose_character_class

# create sample character

#step One: create character and items
player = Character("Starter Character")
sword = Items("Sword")
potion = Items("Health Potion")

#step Two: add items to character inventory
player.add_item(sword)
player.add_item(potion)


# delay print function
def print_delay(text,delay):
    print(text, end='', flush=True)
    time.sleep(delay)
    print()

delay_time = 0.5

def game_intro():
    intro_text = "Welcome to the game!"
    print_delay(intro_text, 0.5)
    print_delay("This is a text based adventure game where you will be given a series of choices to make.", delay_time)
    print_delay("These choices will determine the outcome of the game.", delay_time)
    print_delay("Good luck!", delay_time)

def main_game_logic(player):
    # game_intro();
    print_delay(f"Welcome, {player.name}!", 1)
    print_delay(f"Your adventure is about to begin {player.name}, prepare yourself", 1)

    # This is the first choice the player will make
    #!! continue the introduction to be more in depth and figure out if I can delay the text to be more like reading an actual story
    print("You are walking down a path and you come to a fork in the road.")
    print("Do you go left or right?")
    print("Type 'left' or 'right' and press enter to choose.")
    pathChoice = input()

    # This is the first outcome of the game
    if pathChoice == "left":
        print("You chose to go left, you see the path continue deeper into forest.")
        print("You continue down the path and you come to a clearing.")
        print("You see a small house in the clearing.")
        print("Do you go inside the house or continue down the path?")
        print("Type 'house' or 'path' and press enter to choose.")
        houseChoice = input()
    if houseChoice == "house":
        print("You head towards the door of the house and check if it is unlocked.")

    if pathChoice == "right":
        print("You chose to go right, you see the path continue toward a clearing.")
        print("You see a cart flipped on its side on the path.")
        print("Do you investigate the cart or continue on the path?.")
        print("Type 'investigate' or 'path' and press enter to choose.")
        cartChoice = input()

# indentation of this is very important or it will all break
if __name__ == "__main__":
    game_intro()

    player = choose_character_class()

    main_game_logic(player)