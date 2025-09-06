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
        attack_choice = input("Do you want to Punch the goblin (1) or Strike the Goblin (2) ")
        if attack_choice == "1":
            damage = hero.punch()
        elif attack_choice == "2":
            damage = hero.strike()
        else:
            print("Invalid choice! Hero misses the attack.")
            damage = 0
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
        print(f"\nBilbo has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
        print("Bilbo has unlocked the ability 'DROPKICK' - A powerful attack that deals 75% of normal damage but has a chance to stun the enemy for one turn.")
    else:
        print(f"\n Bilbo has been defeated. Game Over. (｡•́︿•̀｡)")
    if hero.is_alive():
        print("BOSS TIME!!!!!!!!!!")
        dragon = The_Ancient_Dragon("Ancient Dragon")
        while hero.is_alive() and dragon.is_alive():
            print("\nNew Round!")
            dragon_attack_choice = input("Do you want to Punch (1), Strike (2) or Dropkick (3) the Dragon ")
            if dragon_attack_choice == "1":
                damage = hero.punch()
            elif dragon_attack_choice == "2":
                damage = hero.strike()
            elif dragon_attack_choice == "3":
                damage = hero.dropkick()
            else:
                print("Invalid choice! Hero misses the attack.")
                damage = 0
            print(f"Bilbo attacks {dragon.name} for {damage} damage!")
            dragon.receive_damage(damage)
            if dragon.is_alive():
                dragon_damage = dragon.attack_power  # You may want to use a method for attack
                print(f"{dragon.name} attacks Bilbo for {dragon_damage} damage!")
                hero.receive_damage(dragon_damage)
        if not dragon.is_alive():
            print(f"{dragon.name} has been defeated! 🐉")
            print("Bilbo has received ability 💪  MIGHT OF THE DRAGON - All attack damage is doubled")
            print("Bilbo has unlocked the ability 'DRAGON SWORD SLASH' - A powerful attack that deals 125% of normal damage.")
            randomgobnum = random.randint(1, 100)
            baby_elves = []
            if randomgobnum >= 40:
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
                    elf_attack_choice = input("Do you want to Strike (1) Punch (2), Dropkick (4), or Dragon Slash (3) the baby elf ")
                    if elf_attack_choice == "1":
                        damage = hero.strike()
                    elif elf_attack_choice == "2":
                        damage = hero.punch()
                    elif elf_attack_choice == "3":
                        damage = hero.dragon_sword_slash()
                    elif elf_attack_choice == "4":
                        damage = hero.dropkick()
                    else:
                        print("Invalid choice! Bilbo missed the attack.")
                        damage = 0
                    print(f"Bilbo attacks {target_baby_elf.name} for {damage} damage!")
                    target_baby_elf.take_damage(damage)
                    # Baby elves attack hero
                    for baby_elf in baby_elves:
                        if baby_elf.is_alive():
                            elf_damage = random.randint(1, 10)
                            print(f"{baby_elf.name} attacks Bilbo for {elf_damage} damage!")
                            hero.receive_damage(elf_damage)
                    turn += 1
                if not hero.is_alive():
                    print("The baby elves have defeated Bilbo! 😭")
                else:
                    print("Bilbo has defeated all the baby elves! 🎉")

    # Final tally of goblins defeated
   

if __name__ == "__main__":
    main()
