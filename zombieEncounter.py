from random import choice

from models.CombatTracker import CombatTracker
from characters.Tiaq import Tiaq
from characters.Zombie import Zombie

def zombieEncounter(numZombies=1):
    combatTracker = CombatTracker()
    tiaq = Tiaq()
    tiaq.target = tiaq

    combatTracker.clean()
    combatTracker.addMember(tiaq)

    for i in range(numZombies):
        zombie = Zombie(name=f'Zombie{i+1}')
        combatTracker.addMember(zombie)

    combatTracker.start()

    combatContinue = True

    while combatContinue:
        current = combatTracker.current


        # Choose Target
        if current.name == 'Tiaq':
            if tiaq.target.dead or tiaq.target == tiaq:
                target = tiaq
                while target.name == 'Tiaq':
                    target = choice(combatTracker.members)
                    tiaq.target = target
            else:
                target = tiaq.target
        else:
            target = tiaq

        # Attack Target
        #   Roll
        attack = current.attack()
        #   To Hit
        if attack['To Hit']>= target.ac:
            #   Damage
            target.takeDamage(attack['Damage'])

        # End Turn
        combatTracker.endTurn()

        # Check if combat is over
        if tiaq.dead:
            print('Combat Over, Tiaq is dead')
            combatContinue = False
        if len(combatTracker.members) <= 1:
            print('Combat Over, one member remaining')
            combatContinue = False

    winner = combatTracker.members[0]

    print(f'Winner is {winner.name} with {winner.hp}hp remaining!')

    return winner

if __name__ == '__main__':
    winners = {}
    numEncounters = 100
    numZombies = 5

    for i in range(numEncounters):
        winner = zombieEncounter(numZombies)

        if winner.name == 'Tiaq':
            name = winner.name
        else:
            name = 'Zombies'

        if name in winners.keys():
            winners[name] += 1
        else:
            winners[name] = 1

    print()
    print(f'Across {numEncounters} encounters with {numZombies} zombies:')
    print(winners)
