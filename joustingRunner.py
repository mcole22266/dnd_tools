from utils.dice import rollDice
from utils.randomizer import greek_name as random_name
from time import sleep
from random import randint, choice

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

        if self.maneuver in (2, 5, 6):
            to_hit += 5
        elif self.maneuver in (3, 4):
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
        if self.maneuver==2:
            self.ac -= 5
        elif self.maneuver==3:
            self.ac += 5

        if attack >= self.ac:
            self.hits_taken += 1
            return True
        else:
            return False

    def brace_check(self):
        if self.maneuver==4:
            self.animal_handling += 5
        elif self.maneuver==5:
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


def character_creator(randomize=False, simulate=False):
    print()
    name = input('Input name for this character: ')

    if randomize:
        print()
        print('[1] Easy\n[2] Medium\n[3] Hard\n')
        difficulty = input('Difficulty: ')
        if simulate:
            roll_dice = 'Y'
        else:
            roll_dice = input('Auto-roll Dice? [Y/n]: ')

        if difficulty=='1':
            difficulty = 'easy'
        elif difficulty=='2':
            difficulty = 'medium'
        elif difficulty=='3':
            difficulty = 'hard'

        ac, strength, animal_handling = generateStats(difficulty)

    else:
        ac = int(input(f'Input AC for {name}: '))
        strength = int(input(f'Input STR Mod for {name}: '))
        animal_handling = int(input(f'Input Animal Handling Mod for {name}: '))
        roll_dice = input('Auto-roll Dice? [Y/n]: ')

    char = Character(name, ac, strength, animal_handling, roll_dice)
    return char

def joust(char1, char2, max_hits=3, simulate=False):
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
        if not simulate:
            char1.maneuver = int(input(f'{char1.name} Manuever: '))
            char2.maneuver = int(input(f'{char2.name} Manuever: '))
        else:
            char1.manuever = choice(manuevers)
            char2.manuever = choice(manuevers)

    #   - Roll for Attack
        print(f'\n{char1.name} ({char1.ac}) Rolls an attack!')
        char1_attack = char1.attack()
        print(f'{char1.name} rolls a {char1_attack}')

        print(f'\n{char2.name} ({char2.ac}) Rolls an attack!')
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

        if not simulate:
            print(f'Calculating...')
            sleep(2)

        # Check if jousting should cease
        if char1.dismounted or char2.dismounted or char1.hits_taken == max_hits or char2.hits_taken == max_hits:
            joust_continues = False

        if joust_continues:
            print(f'Both {char1.name} and {char2.name} have managed to hang on. The jousting continues!')
        elif char1.dismounted and char2.dismounted:
            print('Both characters have been dismounted')
            if char1.hits_taken>char2.hits_taken:
                winner = char2
            elif char2.hits_taken>char1.hits_taken:
                winner = char1
            else:
                winner = None
        elif char1.dismounted:
            print(f'{char1.name} has been dismounted')
            winner = char2
        elif char2.dismounted:
            print(f'{char2.name} has been dismounted')
            winner = char1
        elif char1.hits_taken == max_hits:
            print(f'{char1.name} loses after reaching {max_hits} hits')
            winner = char2
        elif char2.hits_taken == max_hits:
            print(f'{char2.name} loses after reaching {max_hits} hits')
            winner = char1

    #   - Return stats to default
        char1.reset_stats()
        char2.reset_stats()
    
    return winner


def charVchar(max_hits=3, simulate=False, char1=None, char2=None):
    print()
    # Create Characters
    if not char1:
        randomize_char1 = input('Randomize Character 1? [Y/n] ')
    if not char2:
        randomize_char2 = input('Randomize Character 2? [Y/n] ')

    print()

    if not char1:
        if randomize_char1.lower() == 'n':
            char1 = character_creator(randomize=False, simulate=simulate)
        else:
            char1 = character_creator(randomize=True, simulate=simulate)

    print()

    if not char2:
        if randomize_char2.lower() == 'n':
            char2 = character_creator(randomize=False, simulate=simulate)
        else:
            char2 = character_creator(randomize=True, simulate=simulate)

    print(char1)
    print()
    print(char2)

    winner = joust(char1, char2, max_hits=max_hits, simulate=simulate)

    return winner, char1, char2


def generateStats(diff):
    if diff.lower()=='easy':
        ac = randint(12, 15)
        strength = randint(1, 2)
        animal_handling = randint(1, 2)
    elif diff.lower()=='medium':
        ac = randint(14, 17)
        strength = randint(2, 4)
        animal_handling = randint(2, 4)
    elif diff.lower()=='hard':
        ac = randint(16, 19)
        strength = randint(3, 6)
        animal_handling = randint(3, 6)

    return ac, strength, animal_handling


def generateCharacters():
    characters = []
    print()
    print('Provide the number of characters of each difficulty (Easy, Medium, Hard) that you want to have created.')
    print('For example, to create 5 easy, 10 medium, and 15 hard characters input: 5, 10, 15')
    num_characters = input('>> ')

    num_easy, num_med, num_hard = num_characters.split(',')
    num_easy = int(num_easy.strip())
    num_med = int(num_med.strip())
    num_hard = int(num_hard.strip())

    for _ in range(num_easy):

        if randint(1, 2) == 1:
            name = random_name(male=True)
        else:
            name = random_name(male=False)

        ac, strength, animal_handling = generateStats('easy')
        characters.append(Character(name, ac, strength, animal_handling, 'Y'))

    for _ in range(num_med):

        if randint(1, 2) == 1:
            name = random_name(male=True)
        else:
            name = random_name(male=False)

        ac, strength, animal_handling = generateStats('medium')
        characters.append(Character(name, ac, strength, animal_handling, 'Y'))

    for _ in range(num_hard):

        if randint(1, 2) == 1:
            name = random_name(male=True)
        else:
            name = random_name(male=False)

        ac, strength, animal_handling = generateStats('hard')
        characters.append(Character(name, ac, strength, animal_handling, 'Y'))

    for character in characters:
        favorite_maneuver = choice([
            'None', 'Aggressive', 'Aggressive', 'Aggressive', 'Defensive',
            'Defensive', 'Defensive', 'Braced', 'High in Saddle'
            ])
        print(character)
        print(f'Favorite Maneuver: {favorite_maneuver}')

if __name__ == '__main__':
    max_hits = 10

    print('\n===== Jousting Runner =====\n')

    print('[1] Character Vs Character')
    print('[2] Simulate Joust')
    print('[3] Generate Characters')

    option = input('>> ')

    if option == '1':
        charVchar(max_hits=max_hits)
    elif option == '2':
        num_simulations = int(input('\nHow many simulations? '))
        winners = {}
        char1 = None
        char2 = None
        for _ in range(num_simulations):
            winner, char1, char2 = charVchar(max_hits=max_hits, simulate=True, char1=char1, char2=char2)
            if not winner:
                if winner not in winners.keys():
                    winners[winner] = 1
                else:
                    winners[winner] += 1
            else:
                if winner.name not in winners.keys():
                    winners[winner.name] = 1
                else:
                    winners[winner.name] += 1
            char1.hits_taken = 0
            char1.dismounted = False
            char2.hits_taken = 0
            char2.dismounted = False
        print(winners)
    elif option == '3':
        generateCharacters()
