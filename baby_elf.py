from enemy import Enemy

class BabyElf(Enemy):
    #new ability
    def cry():
        print("WAHHHHHH WAHHHHHH")

    #overide take damage
    def take_damage(self, damage):
        print("YOU HIT A BABY ELF! HOW DARE YOU! 🫵")
        return super().take_damage(damage)
