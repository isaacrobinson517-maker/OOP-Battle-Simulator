import random
from Boss import The_Ancient_Dragon
class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    
    def __init__(self, name):
        #TODO Set the hero's name.
        self.name = name
        #TODO Set the hero's health. You might give the hero more health than a goblin.
        self.health = 300
         #TODO Set the hero's attack power. Should it be more consistent than the goblin's?
        self.attack_power = random.randint(30, 40)

    def strike(self):
        if The_Ancient_Dragon.is_alive == False:
            return self.attack_power * 3
        
        # TODO Implement the hero's attack logic. It could be stronger or more consistent than a goblin's.
        return (self.attack_power)
    
    def punch(self):
        if The_Ancient_Dragon.is_alive == False:
            return self.attack_power * 3 * .75
        return (self.attack_power * .75)
    
    def dragon_sword_slash(self):
        if The_Ancient_Dragon.is_alive == False:
            return self.attack_power * 3 * 1.25
        return (self.attack_power * 1.25)
   
    def dropkick(self):
        randomnum = random.randint(1, 100)
        if The_Ancient_Dragon.is_alive == False:
            return self.attack_power * 3
        if randomnum >= 70:
            self.negate_next_damage = True
            print("The dropkick stuns the enemy for one turn! 🦵😵")
        return self.attack_power

    
    def receive_damage(self, damage):
        if hasattr(self, 'negate_next_damage') and self.negate_next_damage:
            print(f"{self.name} negates all damage this turn with a powerful cry!")
            self.negate_next_damage = False
        # TODO Implement take_damage
        self.health -= damage
        # TODO We should prevent health from going into the NEGATIVE
        if (self.health < 0):
            self.health = 0
            print(f"{self.name} takes {damage} damage - Critical health, U died 🫵 😂 {self.health}.")
        else:
            print(f"{self.name} takes {damage} damage  {self.health}.")

    
    #TODO define is_alive
    def is_alive(self):
        return self.health > 0
