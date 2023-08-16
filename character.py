import random

# base character creator
class Character:
    def __init__(self, name, health=100, weapon=None, damage_range=(1, 4)):
        self.name = name
        self.health = health
        self.inventory = []
        self.weapon = weapon
        self.damage_range = damage_range

    def add_item(self, item):
        self.inventory.append(item)

        # look into other methods for possibly item breaking, expand inventory to be larger, etc.

class Barbarian(Character):
    def __init__(self, name):
        super().__init__(name, health = 140, weapon="Great Axe", damage_range=(1, 12))

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health = 120, weapon="Spiked Mace", damage_range=(1, 6))

class Ranger(Character):
    def __init__(self, name):
        super().__init__(name, health = 100, weapon="Long Bow", damage_range=(1, 8))

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

    choice = input("Enter the number of your choice:")
    name = input("Enter your character's name: ")

    if choice == "1":
        return Barbarian(name)
    elif choice == "2":
        return Paladin(name)
    elif choice == "3":
        return Ranger(name)
    else:
        print("Invalid choice. Please try again.")
        return choose_character_class()


def main():
    player = choose_character_class()
    print(f"Welcome, {player.name}!")
    print(f"You've chosen the {type(player).__name__} class. You will start with {player.health} health.")
    if player.weapon:
        print(f"You have a {player.weapon} equipped.")
    else:
        print("You have no weapon equipped.")
if __name__ == "__main__":
    main()
