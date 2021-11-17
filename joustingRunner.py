from utils.dice import rollDice
from time import sleep
from random import randint

class Character:

    def __init__(self, name, ac, strength, animal_handling, roll_dice):
        self.name = name
        self.ac = ac
        self.strength = strength
        self.animal_handling = animal_handling
        self.maneuver = None
        self.dismounted = False
        self.hits_taken = 0

        if roll_dice.lower() == 'n':
            self.roll_dice = False
        else:
            self.roll_dice = True

        self.memory = self.memorize()

    def memorize(self):
        memory = {
            'name': self.name,
            'ac': self.ac,
            'strength': self.strength,
            'animal_handling': self.animal_handling,
            'roll_dice': self.roll_dice,
            'maneuver': self.maneuver
        }
        return memory

    def reset_stats(self):
        self.name = self.memory['name']
        self.ac = self.memory['ac']
        self.strength = self.memory['strength']
        self.animal_handling = self.memory['animal_handling']
        self.roll_dice = self.memory['roll_dice']
        self.maneuver = self.memory['maneuver']

    def attack(self):
        if not self.roll_dice:
            rolled = input('d20 Roll: ')
            to_hit = int(rolled) + self.strength
        else:
            to_hit = rollDice(numSides=20, numDice=1, modifier=self.strength)

        if self.maneuver in ('2', '5', '6'):
            to_hit += 5
        elif self.maneuver in ('3', '4'):
            to_hit -= 5

        return to_hit

    def hit(self):
        if not self.roll_dice:
            rolled = input(f'{self.name} rolls d12: ')
            damage = int(rolled) + self.strength
        else:
            damage = rollDice(numSides=12, numDice=1, modifier=self.strength)
        return damage

    def is_hit(self, attack):
        if self.maneuver=='2':
            self.ac -= 5
        elif self.maneuver=='3':
            self.ac += 5

        if attack >= self.ac:
            self.hits_taken += 1
            return True
        else:
            return False

    def brace_check(self):
        if self.maneuver=='4':
            self.animal_handling += 5
        elif self.maneuver=='5':
            self.animal_handling -= 5

        # pick highest between strength and animal handling
        mod = max([self.strength, self.animal_handling])

        if not self.roll_dice:
            rolled = input('d20 Roll: ')
            check = int(rolled) + mod
        else:
            check = rollDice(numSides=20, numDice=1, modifier=mod)
        return check

    def __str__(self):
        return f'''
== {self.name} ==
AC: {self.ac} | Str: {self.strength} | Animal Handling: {self.animal_handling}
        '''


def character_creator(randomize=False):
    print()
    name = input('Input name for this character: ')

    if randomize:
        print()
        print('[1] Easy\n[2] Medium\n[3] Hard\n')
        difficulty = input('Difficulty: ')
        roll_dice = input('Auto-roll Dice? [Y/n]: ')

        if difficulty=='1':
            ac = randint(13, 16)
            strength = randint(1, 3)
            animal_handling = randint(1, 3)
        elif difficulty=='2':
            ac = randint(14, 18)
            strength = randint(2, 4)
            animal_handling = randint(2, 4)
        elif difficulty=='3':
            ac = randint(17, 20)
            strength = randint(4, 6)
            animal_handling = randint(4, 6)

    else:
        ac = int(input(f'Input AC for {name}: '))
        strength = int(input(f'Input STR Mod for {name}: '))
        animal_handling = int(input(f'Input Animal Handling Mod for {name}: '))
        roll_dice = input('Auto-roll Dice? [Y/n]: ')

    char = Character(name, ac, strength, animal_handling, roll_dice)
    return char

def joust(char1, char2, max_hits=3):
    joust_continues = True
    round = 0

    while joust_continues:
        round += 1
        print()
        print(f'==== Round {round} ====')
        print(f'\n{char1.name}: {char1.hits_taken}\n{char2.name}: {char2.hits_taken}')
        print()
    # Start Joust
    #   - Choose Maneuver
        manuevers = [None, 'Aggressive', 'Defensive', 'Braced', 'High in Saddle', 'Eyes Fixed']
        for i,manuever in enumerate(manuevers):
            print(f'[{i+1}] {manuever}')
        print()
        char1.maneuver = int(input(f'{char1.name} Manuever: '))
        char2.maneuver = int(input(f'{char2.name} Manuever: '))

    #   - Roll for Attack
        print(f'\n{char1.name} Rolls an attack!')
        char1_attack = char1.attack()
        print(f'{char1.name} rolls a {char1_attack}')

        print(f'\n{char2.name} Rolls an attack!')
        char2_attack = char2.attack()
        print(f'{char2.name} rolls a {char2_attack}')

    #       - If Hit, roll damage and brace checks
        char1_hit = char1.is_hit(char2_attack)
        char2_hit = char2.is_hit(char1_attack)

    #   - Resolve Pass
        print() 
        if char1_hit:
            print(f'{char1.name} was hit!')
            if not char1.brace_check() >= char2.hit():
                char1.dismounted = True
        if char2_hit:
            print(f'{char2.name} was hit!')
            if not char2.brace_check() >= char1.hit():
                char2.dismounted = True

        print(f'Calculating...')
        sleep(2)

        # Check if jousting should cease
        if char1.dismounted or char2.dismounted or char1.hits_taken == max_hits or char2.hits_taken == max_hits:
            joust_continues = False

        if joust_continues:
            print(f'Both {char1.name} and {char2.name} have managed to hang on. The jousting continues!')
        elif char1.dismounted and char2.dismounted:
            print('Both characters have been dismounted')
        elif char1.dismounted:
            print(f'{char1.name} has been dismounted')
        elif char2.dismounted:
            print(f'{char2.name} has been dismounted')
        elif char1.hits_taken == max_hits:
            print(f'{char1.name} loses after reaching {max_hits} hits')
        elif char2.hits_taken == max_hits:
            print(f'{char2.name} loses after reaching {max_hits} hits')

    #   - Return stats to default
        char1.reset_stats()
        char2.reset_stats()


if __name__ == '__main__':
    # Create Characters
    char1 = character_creator()
    char2 = character_creator(randomize=True)

    print(char1)
    print()
    print(char2)

    joust(char1, char2, max_hits=3)

    # ================================================
