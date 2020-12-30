import random

weapon_type = ['Fist', 'Axe', 'Sword', 'Shield', 'Wand']

class Weapon:

    def __init__(self):
        self.data = []
        self.name = "Undefined"
        self.attack = 0
        self.defense = 0
        self.type = weapon_type[0]


class Human:

    def __init__(self):
        self.data = []
        self.life_points = 0
        self.name = "Undefined"
        self.left_hand = ""
        self.right_hand = ""
        self.weapon_skills = 0

    def attack(self):
        total_attack = round((self.right_hand.attack + self.left_hand.attack) * self.weapon_skills)
        damage = random.randint(1, total_attack)
        return damage

    def defense(self):
        total_defense = round((self.right_hand.defense + self.left_hand.defense) * self.weapon_skills)
        block = random.randint(1, total_defense)
        return block

    def damage(self, Attacker):
        result = Attacker.attack() - self.defense()
        if (result > 0):
            self.life_points -= result
            print(f'{self.name} suffered an attack from {Attacker.name} with damage'
                  f' of {result} hit points and has now {self.life_points} life points.')
        else:
            print(f'{self.name} successfully blocked an attack from {Attacker.name}.')

    def alive(self):
        if self.life_points > 0:
            return True
        else:
            print(f'{self.name} is now dead.')
            return False

fst_bare = Weapon()
fst_bare.name = "Bare Fist"
fst_bare.type = weapon_type[0]
fst_bare.attack = 2
fst_bare.defense = 1

swd_justice = Weapon()
swd_justice.name = "Great Sword of Justice"
swd_justice.type = weapon_type[2]
swd_justice.attack = 18
swd_justice.defense = 2

shd_guardian = Weapon()
shd_guardian.name = "Guardian Shield"
shd_guardian.type = weapon_type[2]
shd_guardian.attack = 1
shd_guardian.defense = 15

shd_demon = Weapon()
shd_demon.name = "Demon Shield"
shd_demon.type = weapon_type[2]
shd_demon.attack = 1
shd_demon.defense = 20

Knight = Human()
Knight.name = "Johnny Lawrence"
Knight.life_points = 101
Knight.right_hand = swd_justice
Knight.left_hand = shd_guardian
Knight.weapon_skills = 1.1

Hunter = Human()
Hunter.name = "Daniel Larusso"
Hunter.life_points = 50
Hunter.right_hand = fst_bare
Hunter.left_hand = shd_demon
Hunter.weapon_skills = 24.2


while Hunter.alive() and Knight.alive():
    Knight.damage(Hunter)
    Hunter.damage(Knight)
