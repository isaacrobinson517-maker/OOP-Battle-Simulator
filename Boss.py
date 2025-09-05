from enemy import Enemy


class The_Ancient_Dragon(Enemy):
    def dragons_breath(self):
        print(f"{self.name} uses Dragon's Breath! 🔥🔥🔥")
        self.attack_power = self.attack_power * 2
        self.health = 250
    

        