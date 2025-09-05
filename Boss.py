from enemy import Enemy


class The_Ancient_Dragon(Enemy):
    def dragons_breath(self):
        print(f"{self.name} uses Dragon's Breath! 🔥🔥🔥")
        return 30
    
    def dragon_stomp(self):
        print(f"{self.name} uses Dragon Stomp! 🦶")
        return 20