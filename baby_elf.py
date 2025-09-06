from enemy import Enemy

class BabyElf(Enemy):
    #new ability
    def cry(self):
        print("WAHHHHHH WAHHHHHH")
        print("The baby elf's cry is so loud it stuns the hero for one turn! 😭")
        self.negate_next_damage = True
        return self.attack_power * .5

    #overide take damage
    def take_damage(self, damage):
        if hasattr(self, 'negate_next_damage') and self.negate_next_damage:
            print(f"{self.name} negates all damage this turn with a powerful cry!")
            self.negate_next_damage = False
        else:
            print("YOU HIT A BABY ELF! HOW DARE YOU! 🫵")
            super().take_damage(damage)
