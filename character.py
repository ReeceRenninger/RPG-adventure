# base character creator
class Character:
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health
        self.inventory = []
    
    def add_item(self, item):
        self.inventory.append(item)

        # look into other methods for possibly item breaking, expand inventory to be larger, etc.
class Barbarian(Character):
    def __init__(self, name):
        super().__init__(name, health = 150)

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health = 120)

class Ranger(Character):
    def __init__(self, name):
        super().__init__(name, health = 100)

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


# base item creator
class Items:
    def __init__(self, name):
        self.name = name
       


def main():
    player = choose_character_class()
    print(f"Welcome, {player.name}!")
    print(f"You've chosen the {type(player).__name__} class.) class with {player.health} health.))")

if __name__ == "__main__":
    main()
