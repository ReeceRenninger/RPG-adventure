# base character creator
class Character:
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health
        self.inventory = []
    
    def add_item(self, item):
        self.inventory.append(item)

        # look into other methods for possibly item breaking, expand inventory to be larger, etc.

# base item creator
class Items:
    def __init__(self, name):
        self.name = name
       



