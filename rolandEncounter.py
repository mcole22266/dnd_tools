from random import choice

from models.CombatTracker import CombatTracker
from characters.Tiaq import Tiaq
from characters.SirElliotRoland import SirElliotRoland
from utils.dice import rollDice

def rolandEncounter():
    combatTracker = CombatTracker()

    # Create Combatants
    tiaq = Tiaq()
    roland = SirElliotRoland()

    # Set Targets
    tiaq.target = roland
    roland.target = tiaq

    # Add Members to combat tracker
    combatTracker.clean()
    combatTracker.addMember(tiaq)
    combatTracker.addMember(roland)

    # Start Combat
    combatTracker.start()

    combatContinue = True

    # Loop through turns until victory
    while combatContinue:
        current = combatTracker.current

        # Determine number of attacks
        numAttacks = 1
        if current.action_surge_slots > 0:
            roll = rollDice(4)
            if roll == 1:
                # 1/4th chance to Surge
                numAttacks += 1
                if combatTracker.log:
                    print(f'{current.name} ACTION SURGED')

        # Attack Target
        for _ in range(numAttacks):
            #   Roll
            attack = current.attack()
            #   To Hit
            if attack['To Hit']>= current.target.ac:
                #   Damage
                current.target.takeDamage(attack['Damage'])

        # End Turn
        combatTracker.endTurn()

        # Check if combat is over
        if tiaq.dead:
            print('Combat Over, Tiaq is dead')
            combatContinue = False
        if roland.dead:
            print('Combat Over, Sir Elliot Roland is dead')
            combatContinue = False

    winner = combatTracker.members[0]

    print(f'Winner is {winner.name} with {winner.hp}hp remaining!')

    return winner

if __name__ == '__main__':
    winners = {}
    numEncounters = 100

    for i in range(numEncounters):
        winner = rolandEncounter()

        if winner.name in winners.keys():
            winners[winner.name] += 1
        else:
            winners[winner.name] = 1


    print()
    print(f'Across {numEncounters} encounters')
    print(winners)

