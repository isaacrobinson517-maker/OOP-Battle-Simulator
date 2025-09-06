import random
from goblin import Goblin
from hero import Hero
from Boss import The_Ancient_Dragon

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Bilblo")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")
    if hero.is_alive():
        print("BOSS TIME!!!!!!!!!!")
        dragon = The_Ancient_Dragon("Ancient Dragon")
        while hero.is_alive() and dragon.is_alive():
            print("\nNew Round!")
            damage = hero.strike()
            print(f"Hero attacks {dragon.name} for {damage} damage!")
            dragon.receive_damage(damage)
            if dragon.is_alive():
                dragon_damage = dragon.attack_power  # You may want to use a method for attack
                print(f"{dragon.name} attacks hero for {dragon_damage} damage!")
                hero.receive_damage(dragon_damage)
        if not dragon.is_alive():
            print(f"{dragon.name} has been defeated! 🐉")
            print("Hero has received ability 💪  MIGHT OF THE DRAGON - All attack damage is doubled")
            randomgobnum = random.randint(1, 100)
            baby_elves = []
            if randomgobnum >= 60:
                print("Killing The Ancient Dragon has summoned 3 baby elves to fight you!")
                from baby_elf import BabyElf
                baby_elves = [BabyElf(f"Baby Elf {i+1}") for i in range(3)]
                baby_elf_alive = True
                turn = 0
                while hero.is_alive() and any(baby_elf.is_alive() for baby_elf in baby_elves):
                    print("\nNew Baby Elf Round!")
                    # Each baby elf has a chance to use cry (negate damage for one turn)
                    for baby_elf in baby_elves:
                        if baby_elf.is_alive() and random.random() < 0.5:
                            baby_elf.cry()
                    # Hero attacks a random living baby elf
                    target_baby_elf = random.choice([be for be in baby_elves if be.is_alive()])
                    damage = hero.strike()
                    print(f"Hero attacks {target_baby_elf.name} for {damage} damage!")
                    target_baby_elf.take_damage(damage)
                    # Baby elves attack hero
                    for baby_elf in baby_elves:
                        if baby_elf.is_alive():
                            elf_damage = random.randint(1, 10)
                            print(f"{baby_elf.name} attacks hero for {elf_damage} damage!")
                            hero.receive_damage(elf_damage)
                    turn += 1
                if not hero.is_alive():
                    print("The baby elves have defeated the hero! 😭")
                else:
                    print("The hero has defeated all the baby elves! 🎉")

    # Final tally of goblins defeated
   

if __name__ == "__main__":
    main()
