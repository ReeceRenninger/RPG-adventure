# Base file for the game contains the main game code

print("Hello and welcome to the game!")
print("This is a text based adventure game where you will be given a series of choices to make.")
print("These choices will determine the outcome of the game.")
print("Good luck!")

# This is the first choice the player will make
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