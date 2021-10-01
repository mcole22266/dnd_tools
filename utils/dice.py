from random import randint

def rollDice(numSides=20, numDice=1, modifier=0):
    total = 0
    for _ in range(numDice):
        rolled = randint(1, numSides)
        total += rolled
    total += modifier
    return total
