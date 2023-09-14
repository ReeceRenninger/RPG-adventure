# Base file for the game contains the main game code
# Ctrl + f5 to run the game
# import time module to delay text, this is needed to manipulate the speed of the text
import time
import sys
import random
from character import Character, Items, Weapon, Barbarian, Paladin, Ranger, choose_character_class

# create sample character

#step One: create character and items
player = Character("Starter Character")


# delay print function
def print_delay(text,delay):
    print(text, end='', flush=True)
    time.sleep(delay)
    print()

delay_time = 0.5

# single character delay print, https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
def slow_print(string):
    for char in string: # for each character in the string
        sys.stdout.write(char) # writes the character to the console using write method of sys.stdout
        sys.stdout.flush() # after each character is written, flush the output buffer to immediately display the character rather than waiting for the buffer to fill
        time.sleep(0.05) # this is the delay time between each character, change this to change the speed of the text (.05 is fast)


def game_intro():
    intro_text = "Welcome to the game!"
    print_delay(intro_text, 0.5)
    print_delay("This is a text based adventure game where you will be given a series of choices to make.", delay_time)
    print_delay("These choices will determine the outcome of the game.", delay_time)
    print_delay("Good luck!", delay_time)

def main_game_logic(player):
    ##!! trying to figure out to get player dmg rolls

    print_delay(f"Welcome, {player.name}!", 1)
    print(f"You've chosen the {type(player).__name__} class. You will start with {player.health} health.")
    if player.weapon:
        print(f"The {type(player).__name__} class will have access to {player.weapon.name} it has a damage range of {player.weapon.damage_range}.")
       
    else:
        print("You have no weapon equipped.")
    print_delay(f"Your adventure is about to begin {player.name}, prepare yourself", 1)
    # slow_print(f"You awaken in a dark cave, you have no memory of how you got here. As you stand up, you realize there is a small light coming from a distant corner of the cave. As you begin to move toward the light, you see a {player.weapon.name} leaning against the side of the cave near the light. You pick up {player.weapon.name} and continue into the light.  As you emerge from the cave, you see a path leading into a forest. You begin to walk down the path...")
    # This is the first choice the player will make
    #!! continue the introduction to be more in depth and figure out if I can delay the text to be more like reading an actual story
    print_delay("You are walking down a path and you come to a fork in the road.", delay_time)
    print_delay("Do you go left or right?", delay_time)
    print_delay("Type 'left' or 'right' and press enter to choose.", delay_time)
    pathChoice = input()

    # if pathChoice != "left" or pathChoice != "right":
    #     print_delay("You must choose left or right.")
    #     print_delay("Type 'left' or 'right' and press enter to choose.")
    #     pathChoice = input()

    # This is the first outcome of the game
    if pathChoice == "left":
        print_delay("You chose to go left, you see the path continue deeper into forest.", delay_time)
        print_delay("You continue down the path and you come to a clearing.", delay_time)
        print_delay("You see a small house in the clearing.", delay_time)
        print_delay("Do you go inside the house or continue down the path?", delay_time)
        print_delay("Type 'house' or 'path' and press enter to choose.", delay_time)
        houseChoice = input()

    elif pathChoice == "right":
        print_delay("You chose to go right, you see the path continue toward a clearing.", delay_time)
        print_delay("You see a cart flipped on its side on the path.", delay_time)
        print_delay("Do you investigate the cart or continue on the path?.", delay_time)
        print_delay("Type 'investigate' or 'path' and press enter to choose.", delay_time)
        cartChoice = input()

    if houseChoice == "house":
        print_delay("You head towards the door of the house and check if it is unlocked.", delay_time)
        print_delay("The door is unlocked and you enter the house.", delay_time)
        goblin_health = 5
        print_delay("You are immediately attacked by a goblin!", delay_time)
        print_delay(f"You pull out your {player.weapon.name} and strike the goblin!", delay_time)
        print_delay(f"You deal {player_damage} damage to the goblin!", delay_time)
        if player_damage >= goblin_health:
            print_delay("You have defeated the goblin!", delay_time)
        elif player_damage < goblin_health:
            print_delay(f"The goblin has {goblin_health} health remaining!", delay_time)
            def goblin_dmg():
                goblin_damage = random.randint(1, 4)
                return goblin_damage
            print_delay(f"The goblin strikes back at you! He strikes you for {goblin_dmg()} damage!")
            print_delay(f"Your total health is now {player.health - goblin_dmg()}")
            print_delay(f"You strike back at the goblin! Dealing {player_damage} damage!")
            if goblin_health == 0:
                print_delay("You have defeated the goblin!")





# indentation of this is very important or it will all break
if __name__ == "__main__":
    game_intro()

    #!! global player variable
    player = choose_character_class()

    #!! global dmg roll for player
    player_damage = player.weapon.roll_damage()

    main_game_logic(player)