import random
### Global Variables ###
# Names the weapon types available in the game
weapon_type = ['Fist', 'Paw', 'Axe', 'Sword', 'Shield', 'Wand']

### Classes ###
class Weapon:

    def __init__(self):
        self.data = []
        self.name = "Undefined"
        # Maximum damage delivered by the weapon considering the player skill 1.0
        self.damage = 0
        # Maximum protection delivered by the weapon considering the player skill 1.0
        self.protection = 0
        self.type = weapon_type[0]


class Creature:

    def __init__(self):
        self.data = []
        self.life_points_max = 0
        self.life_points_current = 0
        self.mana_points_max = 0
        self.mana_points_current = 0
        self.name = "Undefined"
        self.left_hand = ""
        self.right_hand = ""
        # How good the player can handle weapons. Increases attack and defense
        self.weapon_skills = 0.0
        # How good the player can use magic skills (e.g. Cure)
        self.magic_skills = 0.0
        # Required amount of mana to use cure
        self.mana_for_cure = 0
        # Factor to calculate the amount of life points got through cure
        self.life_per_cure = 0.0
        self.can_attack = False
        self.can_defend = False


    # Calculates a random damage value a player can delivered based on weapons and skills
    def attack(self):
        # Sum all weapons attack points and multiply by the skill factor
        total_attack = round((self.right_hand.damage + self.left_hand.damage) * self.weapon_skills)
        damage = random.randint(1, total_attack)
        return damage

    # Calculates a random block value a player can reduce from an attack based on weapons and skills
    def defense(self):
        # Sum all weapons defense points and multiply by the skill factor
        total_defense = round((self.right_hand.protection + self.left_hand.protection) * self.weapon_skills)
        block = random.randint(1, total_defense)
        return block

    # Delivers damage to a victim
    def engage(self, Victim):
        # Is the attacker alive?
        if self.alive() and self.can_attack:
            # Is the victim alive?
            if Victim.alive():
                result = self.attack()
                # Result can be minimized if the victim is able to defend him/herself
                if Victim.can_defend:
                    result -= Victim.defense()
                # Any harm?
                if (result > 0):
                    Victim.life_points_current -= result
                    print(f'{Victim.name} suffered an attack from {self.name} with damage'
                          f' of {result} hit points and has now {Victim.life_points_current} life points.')
                    if Victim.alive() == False:
                        print(f'{Victim.name} is now dead')
                else:
                    print(f'{self.name} successfully blocked an attack from {Victim.name}.')

    # Restore life points for the player him/herself
    def cure(self):
        if self.alive():
            if (self.mana_points_current >= self.mana_for_cure) or self.life_points_current > 0:
                self.mana_points_current -= self.mana_for_cure
                total_cure = round(self.life_points_max * random.uniform(0.1, self.life_per_cure))
                if (self.life_points_current + total_cure) > self.life_points_max:
                    self.life_points_current = self.life_points_max
                else:
                    self.life_points_current += total_cure
                print(f'{self.name} has conjured the cure spell and restored {total_cure} life points.')
            else:
                print(f'Not enough mana or already dead.')

    # Is the player still alive?
    def alive(self):
        if self.life_points_current > 0:
            return True
        else:
            return False

### Game ###
# Creating game objects

# Creating weapons
fst_bare = Weapon()
fst_bare.name = "Bare Fist"
fst_bare.type = weapon_type[0]
fst_bare.damage = 2
fst_bare.protection = 1

swd_justice = Weapon()
swd_justice.name = "Great Sword of Justice"
swd_justice.type = weapon_type[3]
swd_justice.damage = 18
swd_justice.protection = 2

shd_guardian = Weapon()
shd_guardian.name = "Guardian Shield"
shd_guardian.type = weapon_type[4]
shd_guardian.damage = 1
shd_guardian.protection = 15

shd_demon = Weapon()
shd_demon.name = "Demon Shield"
shd_demon.type = weapon_type[4]
shd_demon.damage = 1
shd_demon.protection = 20

paw_rabbit = Weapon()
paw_rabbit.name = "Sweet White Rabbit Paw"
paw_rabbit.type = weapon_type[2]
paw_rabbit.damage = 0
paw_rabbit.protection = 0

# Creating Players
Knight = Creature()
Knight.name = "Johnny Lawrence"
Knight.life_points_max = 100
Knight.life_points_current = Knight.life_points_max
Knight.mana_points = 50
Knight.right_hand = swd_justice
Knight.left_hand = shd_guardian
Knight.weapon_skills = 1.1
Knight.mana_for_cure = 10
Knight.life_per_cure = 0.3
Knight.can_attack = True
Knight.can_defend = True

Hunter = Creature()
Hunter.name = "Daniel Larusso"
Hunter.life_points_max = 100
Hunter.life_points_current = Hunter.life_points_max
Hunter.right_hand = fst_bare
Hunter.left_hand = shd_demon
Hunter.weapon_skills = 24.2
Hunter.mana_for_cure = 10
Hunter.life_per_cure = 0.2
Hunter.can_attack = True
Hunter.can_defend = True

Rabbit = Creature()
Rabbit.name = "Innocent White Rabbit"
Rabbit.life_points_max = 10
Rabbit.life_points_current = Rabbit.life_points_max
Rabbit.right_hand = paw_rabbit
Rabbit.left_hand = paw_rabbit
Rabbit.can_attack = False
Rabbit.can_defend = False

# Fight!
while Hunter.alive() and Knight.alive():

    Knight.engage(Hunter)
    # Conjure cure when life points are below 50%
    if Hunter.life_points_current <= round(Hunter.life_points_max * 0.5):
        Hunter.cure()

    Hunter.engage(Knight)
    if Knight.life_points_current <= round(Knight.life_points_max * 0.5):
        Knight.cure()

print("### Next fight of the night! ###")
# Fight II!
while Hunter.alive() and Rabbit.alive():
    Hunter.engage(Rabbit)

