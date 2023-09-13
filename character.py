import random

# base character creator
class Character:
    def __init__(self, name, health=100, weapon=None, damage_range=(1, 4)):
        self.name = name
        self.health = health
        #!! updated weapon to be none by default was weapon
        self.weapon = None
        self.damage_range = damage_range
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

        # look into other methods for possibly item breaking, expand inventory to be larger, etc.

class Barbarian(Character):
    def __init__(self, name, weapon):
        super().__init__(name, health = 140, weapon=weapon, damage_range=(1, 12))
        self.weapon = weapon

class Paladin(Character):
    def __init__(self, name, weapon):
        super().__init__(name, health = 120, weapon=weapon, damage_range=(1, 6))
        self.weapon = weapon

class Ranger(Character):
    def __init__(self, name, weapon):
        super().__init__(name, health = 100, weapon=weapon, damage_range=(1, 8))
        self.weapon = weapon

# base item creator
class Items:
    def __init__(self, name):
        self.name = name

# weapon class
class Weapon(Items):
    def __init__(self, name, damage_range):

        super().__init__(name)
        # damage range is a tuple of min and max damage
        self.damage_range = damage_range

    def roll_damage(self):
            # return a random value between the min and max damage that breaks down a "tuple" into two arguments to be
            # fed into the random.randint function
         return random.randint(*self.damage_range)

       


def choose_character_class():
    print("Choose your class: ")
    print("1. Barbarian")
    print("2. Paladin")
    print("3. Ranger")


    while True:
        choice = input("Enter the number of your choice:")
        name = input("Enter your character's name: ")

    #!! needed to add weapon class to the character selection to be able to run the dmg roll function on main file?
        if choice == "1":
            return Barbarian(name, Weapon("Great Axe", (1, 12)))
        elif choice == "2":
            return Paladin(name, Weapon("Spiked Mace", (1, 6)))
        elif choice == "3":
            return Ranger(name, Weapon("Long Bow", (1, 8)))
        else:
            print("Invalid choice. Please try again.")
            # return choose_character_class()

#! this is for testing purposes only to see if the character class is working properly
def main():
    player = choose_character_class()
    print(f"Welcome, {player.name}!")
    print(f"You've chosen the {type(player).__name__} class. You will start with {player.health} health.")
    if player.weapon:
        print(f"You have a {player.weapon.name} equipped.")
    else:
        print("You have no weapon equipped.")
if __name__ == "__main__":
    main()
