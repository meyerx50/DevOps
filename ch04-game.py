import random

class Human:

    def __init__(self):
        self.data = []
        self.life_points = 0
        self.sword_skills = 0
        self.shield_skills = 0
        self.name = "Undefined"

    def attack(self):
        damage = random.randint(1, self.sword_skills)
        return damage

    def defense(self):
        block = random.randint(1, self.shield_skills)
        return block

    def damage(self, attack):
        result = attack - self.defense()
        if (result > 0):
            self.life_points -= result
        # print(f'{self.name} has now {self.life_points}.')

    def alive(self):
        if self.life_points > 0:
            return True
        else:
            # print(f'{self.name} is now dead')
            return False

games = 100000
amazon_wins = 0
knight_wins = 0

for x in range(games):
    Knight = Human()
    Knight.name = "Bolsonaro"
    Knight.life_points = 101
    Knight.sword_skills = 15
    Knight.shield_skills = 5

    Amazon = Human()
    Amazon.name = "Dilma"
    Amazon.life_points = 50
    Amazon.sword_skills = 10
    Amazon.shield_skills = 26

    while Amazon.alive() and Knight.alive():
        Knight.damage(Amazon.attack())
        Amazon.damage(Knight.attack())

    if Amazon.alive():
        amazon_wins += 1
    else:
        knight_wins +=1

print(f'{Amazon.name} won {round(amazon_wins * 100 / games, 2)} % of the '
      f'times, while {Knight.name} won {round(knight_wins * 100 / games, 2)} '
      f'% of the times')