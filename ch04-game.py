import random

class Human:

    def __init__(self):
        self.data = []
        self.life_points = 100
        self.sword_skills = 0
        self.shield_skills = 0

    def attack(self):
        damage = random.randint(1, self.sword_skills)
        return damage

    def defense(self):
        block = random.randint(1, self.shield_skills)
        return block

Knight = Human()
Knight.life_points = 100
Knight.sword_skills = 10
Knight.shield_skills = 10

Amazon = Human()
Amazon.life_points = 50
Amazon.sword_skills = 15
Amazon.shield_skills = 20

while Amazon.life_points > 0 and Knight.life_points > 0:
    damage = Knight.attack() - Amazon.defense()
    if damage >= 0:
        Amazon.life_points -= damage
    print(f'Amazon has now {Amazon.life_points}')
    damage = Amazon.attack() - Knight.defense()
    if damage >= 0:
        Knight.life_points -= damage
    print(f'Knight has now {Knight.life_points}')

