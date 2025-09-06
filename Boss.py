from enemy import Enemy
import random


class The_Ancient_Dragon(Enemy):
    def dragons_breath(self):
        print(f"{self.name} uses Dragon's Breath! 🔥🔥🔥")
        self.health = 250
        attack_random = random.randint(1, 100)
        if attack_random >= 90:
            print("It's super effective! The hero is scorched! 🔥")
            return self.attack_power * 3
        else:
            print("The hero narrowly avoids the flames! 😅")
            return self.attack_power
        

    def receive_damage(self, damage):
        # TODO Implement take_damage
        self.health -= damage
        # TODO We should prevent health from going into the NEGATIVE
        if (self.health < 0):
            self.health = 0
            print(f"{self.name} takes {damage} damage - Remaining health is 0")
        else:
            print(f"{self.name} takes {damage} damage  {self.health}.")
