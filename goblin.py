import random

class Goblin:
    """
    This is our goblin blueprint 
    
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    """
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.attack_power = random.randint(5, 15)

    def attack(self):
        critical = random.randint(1,100)
        if critical >= 95:
            self.attack_power = self.attack_power * 9999999999999999999999999999999999999999999999999999999
        
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health -= damage
        if (self.health <= 0):
            (f"{self.name} takes {damage} damage. Health is now {0}.")
        else:
            print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0
