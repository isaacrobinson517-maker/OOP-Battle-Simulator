from enemy import Enemy


class The_Ancient_Dragon(Enemy):
    def dragons_breath(self):
        print(f"{self.name} uses Dragon's Breath! 🔥🔥🔥")
        self.attack_power = self.attack_power * 2
        self.health = 250

    def receive_damage(self, damage):
        # TODO Implement take_damage
        self.health -= damage
        # TODO We should prevent health from going into the NEGATIVE
        if (self.health < 0):
            self.health = 0
            print(f"{self.name} takes {damage} damage - Critical health, U died 🫵 😂 {self.health}.")
        else:
            print(f"{self.name} takes {damage} damage  {self.health}.")
